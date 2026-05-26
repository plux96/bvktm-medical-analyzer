"""
BVKTM - Buxoro Viloyat Ko'p Tarmoqli Tibbiy Markazi
Ma'lumot Kiritish Veb-Formasi
=====================================================
Ishga tushirish: streamlit run app.py
Brauzerda: http://localhost:8501
"""

import streamlit as st
import json
import os
import copy
import base64
import requests
from datetime import datetime
from data_schema import BARCHA_BOLIMLAR, _bolim_shablon, _raqobatchi_shablon
from field_guide import FIELD_LABELS, FIELD_HELP, SECTION_GUIDES

DATA_FILE = os.path.join(os.path.dirname(__file__), "bvktm_data.json")
GITHUB_REPO = "plux96/bvktm-medical-analyzer"
GITHUB_FILE = "bvktm_data.json"

# ============================================================================
# SECTION DISPLAY NAMES (32 bo'lim)
# ============================================================================
SECTION_LABELS = {
    "markaz_profili": "1. Markaz profili",
    "bolimlar": "2. Bo'limlar (27 ta)",
    "kadrlar": "3. Kadrlar",
    "tibbiy_jihozlar": "4. Tibbiy jihozlar",
    "toshak_fondi": "5. Toshak fondi",
    "poliklinika": "6. Poliklinika",
    "jarrohlik": "7. Jarrohlik",
    "diagnostika": "8. Diagnostika",
    "dori_darmon": "9. Dori-darmon",
    "moliya": "10. Moliya",
    "bemorlar_statistikasi": "11. Bemorlar statistikasi",
    "sifat_korsatkichlari": "12. Sifat ko'rsatkichlari",
    "shoshilinch_yordam": "13. Shoshilinch yordam",
    "infratuzilma": "14. Infratuzilma",
    "it_raqamlashtirish": "15. IT va raqamlashtirish",
    "xalqaro_hamkorlik": "16. Xalqaro hamkorlik",
    "talim_ilmfan": "17. Ta'lim va ilm-fan",
    "bemor_qoniqishi": "18. Bemor qoniqishi",
    "infeksiya_nazorati": "19. Infeksiya nazorati",
    "qon_banki": "20. Qon banki",
    "reanimatsiya_intensiv": "21. Reanimatsiya va intensiv",
    "reabilitatsiya": "22. Reabilitatsiya",
    "inson_resurslari": "23. Inson resurslari",
    "xavfsizlik": "24. Xavfsizlik",
    "ekologiya": "25. Ekologiya",
    "raqobatchilar": "26. Raqobatchilar",
    "hududiy_salomatlik": "27. Hududiy salomatlik",
    "davlat_dasturlari": "28. Davlat dasturlari",
    "telemedicina": "29. Telemedicina",
    "kelajak_rejalari": "30. Kelajak rejalari",
    "qonunchilik": "31. Qonunchilik",
    "simulyatsiya_maqsadlari": "32. Simulyatsiya maqsadlari",
}

SECTION_KEYS = list(SECTION_LABELS.keys())

# FIELD_LABELS, FIELD_HELP, SECTION_GUIDES imported from field_guide.py (17-qator)


# ============================================================================
# GITHUB HELPERS
# ============================================================================
def get_github_token():
    try:
        return st.secrets["GITHUB_TOKEN"]
    except Exception:
        return os.environ.get("GITHUB_TOKEN", "")


def load_from_github():
    try:
        url = "https://api.github.com/repos/{}/contents/{}".format(GITHUB_REPO, GITHUB_FILE)
        token = get_github_token()
        headers = {"Accept": "application/vnd.github.v3+json"}
        if token:
            headers["Authorization"] = "token " + token
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            content = base64.b64decode(resp.json()["content"]).decode("utf-8")
            return json.loads(content), resp.json().get("sha", "")
        return {}, ""
    except Exception:
        return {}, ""


def _is_filled(val):
    """Qiymat to'ldirilganmi (default emas)."""
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return val != 0
    if isinstance(val, str):
        return val.strip() != ""
    if isinstance(val, list):
        return len(val) > 0
    if isinstance(val, dict):
        return any(_is_filled(v) for v in val.values())
    return False


def _deep_merge(remote, local):
    """Remote + local ni birlashtirish. Local'da to'ldirilgan maydonlar ustunlik oladi.
    Remote'da to'ldirilgan lekin local'da bo'sh — remote qoladi."""
    if not isinstance(remote, dict) or not isinstance(local, dict):
        # Agar local to'ldirilgan bo'lsa — local oladi
        if _is_filled(local):
            return copy.deepcopy(local)
        return copy.deepcopy(remote)

    merged = copy.deepcopy(remote)
    for key, local_val in local.items():
        if key not in merged:
            merged[key] = copy.deepcopy(local_val)
            continue

        remote_val = merged[key]

        if isinstance(local_val, dict) and isinstance(remote_val, dict):
            merged[key] = _deep_merge(remote_val, local_val)
        elif isinstance(local_val, list) and isinstance(remote_val, list):
            # List: agar local uzunroq yoki to'ldirilgan — local oladi
            if len(local_val) > len(remote_val):
                merged[key] = copy.deepcopy(local_val)
            elif len(local_val) == len(remote_val):
                # Har bir elementni merge qilish
                result = []
                for i in range(len(local_val)):
                    if isinstance(local_val[i], dict) and isinstance(remote_val[i], dict):
                        result.append(_deep_merge(remote_val[i], local_val[i]))
                    elif _is_filled(local_val[i]):
                        result.append(copy.deepcopy(local_val[i]))
                    else:
                        result.append(copy.deepcopy(remote_val[i]))
                merged[key] = result
            else:
                # Remote uzunroq — remote qoladi, lekin local elementlarni merge
                result = copy.deepcopy(remote_val)
                for i in range(len(local_val)):
                    if isinstance(local_val[i], dict) and isinstance(result[i], dict):
                        result[i] = _deep_merge(result[i], local_val[i])
                    elif _is_filled(local_val[i]):
                        result[i] = copy.deepcopy(local_val[i])
                merged[key] = result
        else:
            # Oddiy qiymat: local to'ldirilgan bo'lsa — local oladi
            if _is_filled(local_val):
                merged[key] = copy.deepcopy(local_val)
            # Aks holda remote qoladi
    return merged


def save_to_github(data):
    token = get_github_token()
    if not token:
        return False, "GitHub token topilmadi. Secrets'ga GITHUB_TOKEN qo'shing."
    try:
        url = "https://api.github.com/repos/{}/contents/{}".format(GITHUB_REPO, GITHUB_FILE)
        headers = {
            "Authorization": "token " + token,
            "Accept": "application/vnd.github.v3+json",
        }
        # 1. Avval remote'dan oxirgi versiyani olish
        resp = requests.get(url, headers=headers, timeout=10)
        sha = ""
        remote_data = {}
        if resp.status_code == 200:
            sha = resp.json().get("sha", "")
            remote_content = base64.b64decode(resp.json()["content"]).decode("utf-8")
            remote_data = json.loads(remote_content)

        # 2. MERGE: remote + local = birlashtirilgan
        if remote_data:
            merged = _deep_merge(remote_data, data)
        else:
            merged = data

        # 3. Session state'ni ham yangilash (boshqa odam qo'shgan ma'lumotlar ko'rinsin)
        st.session_state["data"] = merged

        # 4. GitHub'ga saqlash
        content = base64.b64encode(
            json.dumps(merged, ensure_ascii=False, indent=2).encode("utf-8")
        ).decode("utf-8")
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        payload = {
            "message": "Data merged: " + now_str,
            "content": content,
        }
        if sha:
            payload["sha"] = sha
        resp = requests.put(url, headers=headers, json=payload, timeout=15)
        if resp.status_code in (200, 201):
            return True, "GitHub'ga saqlandi! (merge bilan)"
        return False, "Xatolik: " + str(resp.status_code)
    except Exception as e:
        return False, str(e)


# ============================================================================
# DATA HELPERS
# ============================================================================
def load_data():
    """Har doim GitHub'dan oxirgi versiyani olish. Lokal faylga ishonmaymiz."""
    gh_data, _ = load_from_github()
    if gh_data:
        return gh_data
    # GitHub'dan olish imkoni bo'lmasa — lokal fallback
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                local_data = json.load(f)
                if local_data:
                    return local_data
            except Exception:
                pass
    return copy.deepcopy(BARCHA_BOLIMLAR)


def save_data_local(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, ensure_ascii=False, indent=2, fp=f)


def save_data(data):
    save_data_local(data)


def get_val(key, default=None):
    keys = key.split(".")
    d = st.session_state.get("data", {})
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, default)
        elif isinstance(d, list):
            try:
                d = d[int(k)]
            except (ValueError, IndexError):
                return default
        else:
            return default
    return d if d is not None else default


def set_val(key, value):
    keys = key.split(".")
    d = st.session_state["data"]
    for k in keys[:-1]:
        if isinstance(d, dict):
            if k not in d:
                d[k] = {}
            d = d[k]
        elif isinstance(d, list):
            idx = int(k)
            d = d[idx]
    last_key = keys[-1]
    if isinstance(d, dict):
        d[last_key] = value
    elif isinstance(d, list):
        d[int(last_key)] = value


# ============================================================================
# WIDGET HELPERS
# ============================================================================
def _nice_label(field_key):
    """Convert field_key to human-readable label using FIELD_LABELS dict."""
    parts = field_key.split(".")
    name = parts[-1]
    # Look up in FIELD_LABELS first
    if name in FIELD_LABELS:
        return FIELD_LABELS[name]
    # Fallback: auto-generate from key
    label = name.replace("_", " ").capitalize()
    return label


def _get_help(field_key):
    """Get help text for a field from FIELD_HELP dict."""
    parts = field_key.split(".")
    name = parts[-1]
    return FIELD_HELP.get(name, "")


def num(label, key, min_val=0, max_val=None, step=1, is_float=False, help_text=""):
    default = get_val(key, 0.0 if is_float else 0)
    if is_float:
        val = st.number_input(
            label, value=float(default), min_value=0.0,
            step=0.1, help=help_text or None, key="w_" + key
        )
    else:
        kw = {
            "label": label,
            "value": int(default),
            "min_value": min_val,
            "step": step,
            "help": help_text or None,
            "key": "w_" + key,
        }
        if max_val is not None:
            kw["max_value"] = max_val
        val = st.number_input(**kw)
    set_val(key, val)
    return val


def txt(label, key, help_text=""):
    default = get_val(key, "")
    val = st.text_input(label, value=str(default), help=help_text or None, key="w_" + key)
    set_val(key, val)
    return val


def txtarea(label, key, help_text=""):
    default = get_val(key, "")
    val = st.text_area(label, value=str(default), help=help_text or None, key="w_" + key)
    set_val(key, val)
    return val


def yn(label, key, help_text=""):
    default = get_val(key, False)
    val = st.checkbox(label, value=bool(default), help=help_text or None, key="w_" + key)
    set_val(key, val)
    return val


def slider_widget(label, key, min_v=0, max_v=10, help_text=""):
    default = get_val(key, 0)
    clamped = max(min_v, min(max_v, int(default)))
    val = st.slider(label, min_v, max_v, clamped, help=help_text or None, key="w_" + key)
    set_val(key, val)
    return val


def tags(label, key, help_text=""):
    default = get_val(key, [])
    if isinstance(default, list):
        default = ", ".join(str(x) for x in default)
    val = st.text_input(
        label, value=str(default),
        help=(help_text or "") + " (vergul bilan ajrating)",
        key="w_" + key,
    )
    result = [x.strip() for x in val.split(",") if x.strip()] if val else []
    set_val(key, result)
    return result


def pct(label, key, help_text=""):
    default = get_val(key, 0.0)
    val = st.number_input(
        label, value=float(default), min_value=0.0, max_value=100.0,
        step=0.1, help=help_text or None, key="w_" + key,
    )
    set_val(key, val)
    return val


def money(label, key, help_text=""):
    default = get_val(key, 0)
    val = st.number_input(
        label, value=int(default), min_value=0,
        step=100000, help=(help_text or "") + " (so'mda)",
        key="w_" + key,
    )
    set_val(key, val)
    return val


# ============================================================================
# FIELD TYPE DETECTION AND AUTO-RENDERING
# ============================================================================

# Keys that should use money input (step=100000)
MONEY_KEYS = {
    "byudjet", "daromad", "xarajat", "maosh", "investitsiya", "subsidiya",
    "grantlar_summasi", "xarajati", "tannarxi", "byudjeti", "tolovlar",
    "summasi", "narxi", "fondi", "kompensatsiya", "jarimalar", "tejamlari",
    "paket", "tejash", "byudjet_max", "fondi_max",
}

# Keys where value is score 1-10
SCORE_KEYS = {
    "holat_bahosi", "bino_holati_bahosi", "ball",
}

# Keys with foiz (percentage) suffix
FOIZ_SUFFIX = "_foiz"


def _is_money_key(field_name):
    for mk in MONEY_KEYS:
        if mk in field_name:
            return True
    return False


def _is_score_key(field_name):
    for sk in SCORE_KEYS:
        if field_name == sk or field_name.endswith("_" + sk):
            return True
    return False


def auto_render_field(field_name, field_default, key_prefix):
    """Automatically render the right widget based on field name and default type."""
    full_key = key_prefix + "." + field_name
    label = _nice_label(full_key)
    help_text = _get_help(full_key)

    if isinstance(field_default, bool):
        yn(label, full_key, help_text=help_text)

    elif isinstance(field_default, list):
        tags(label, full_key, help_text=help_text)

    elif isinstance(field_default, str):
        txt(label, full_key, help_text=help_text)

    elif isinstance(field_default, float):
        if field_name.endswith(FOIZ_SUFFIX):
            pct(label, full_key, help_text=help_text)
        else:
            num(label, full_key, is_float=True, help_text=help_text)

    elif isinstance(field_default, int):
        if _is_money_key(field_name):
            money(label, full_key, help_text=help_text)
        elif _is_score_key(field_name):
            slider_widget(label, full_key, min_v=0, max_v=10, help_text=help_text)
        else:
            num(label, full_key, help_text=help_text)

    elif isinstance(field_default, dict):
        # Nested dict -- render as sub-expander
        exp_title = label
        with st.expander(exp_title, expanded=False):
            auto_render_dict(field_default, full_key)

    else:
        txt(label, full_key, help_text=help_text)


def auto_render_dict(schema_dict, key_prefix):
    """Render all fields of a dict schema in 2-column layout."""
    fields = list(schema_dict.items())

    # Separate booleans, lists, nested dicts, strings, numbers
    bool_fields = [(k, v) for k, v in fields if isinstance(v, bool)]
    list_fields = [(k, v) for k, v in fields if isinstance(v, list)]
    dict_fields = [(k, v) for k, v in fields if isinstance(v, dict)]
    str_fields = [(k, v) for k, v in fields if isinstance(v, str)]
    num_fields = [(k, v) for k, v in fields if isinstance(v, (int, float)) and not isinstance(v, bool)]

    # Numbers in 2 columns
    if num_fields:
        st.subheader("Raqamli ko'rsatkichlar")
        col_pairs = [num_fields[i:i+2] for i in range(0, len(num_fields), 2)]
        for pair in col_pairs:
            cols = st.columns(2)
            for idx, (fname, fdefault) in enumerate(pair):
                with cols[idx]:
                    auto_render_field(fname, fdefault, key_prefix)

    # Strings in 2 columns
    if str_fields:
        st.subheader("Matn maydonlari")
        col_pairs = [str_fields[i:i+2] for i in range(0, len(str_fields), 2)]
        for pair in col_pairs:
            cols = st.columns(2)
            for idx, (fname, fdefault) in enumerate(pair):
                with cols[idx]:
                    auto_render_field(fname, fdefault, key_prefix)

    # Booleans in 3 columns
    if bool_fields:
        st.subheader("Ha/Yo'q maydonlari")
        col_triples = [bool_fields[i:i+3] for i in range(0, len(bool_fields), 3)]
        for triple in col_triples:
            cols = st.columns(3)
            for idx, (fname, fdefault) in enumerate(triple):
                with cols[idx]:
                    auto_render_field(fname, fdefault, key_prefix)

    # Lists
    if list_fields:
        st.subheader("Ro'yxatlar")
        for fname, fdefault in list_fields:
            auto_render_field(fname, fdefault, key_prefix)

    # Nested dicts
    if dict_fields:
        st.subheader("Ichki bo'limlar")
        for fname, fdefault in dict_fields:
            auto_render_field(fname, fdefault, key_prefix)


def render_list_section(section_key, item_template_fn, item_name="element"):
    """Render a list-type section (bolimlar, raqobatchilar)."""
    data = st.session_state["data"]
    if section_key not in data:
        data[section_key] = copy.deepcopy(BARCHA_BOLIMLAR[section_key])

    current_list = data[section_key]
    count = len(current_list)

    label_for_count = item_name + " soni"
    new_count = st.number_input(
        label_for_count,
        value=count,
        min_value=0,
        max_value=100,
        step=1,
        key="w_" + section_key + "_count",
    )

    # Adjust list size
    if new_count > count:
        for _ in range(new_count - count):
            current_list.append(item_template_fn())
    elif new_count < count:
        data[section_key] = current_list[:new_count]
        current_list = data[section_key]

    # Render each item in an expander
    for i, item in enumerate(current_list):
        item_label = item.get("nomi", "") or (item_name + " " + str(i + 1))
        exp_title = str(i + 1) + ". " + item_label
        with st.expander(exp_title, expanded=False):
            item_key = section_key + "." + str(i)
            template = item_template_fn()
            auto_render_dict(template, item_key)


# ============================================================================
# SECTION-SPECIFIC HEADERS
# ============================================================================
SECTION_HEADERS = {
    "markaz_profili": "Markaz Profili - Umumiy ma'lumotlar",
    "bolimlar": "Bo'limlar - 27 bo'lim",
    "kadrlar": "Kadrlar - Xodimlar tarkibi",
    "tibbiy_jihozlar": "Tibbiy Jihozlar",
    "toshak_fondi": "Toshak Fondi - Karavotlar",
    "poliklinika": "Poliklinika - Ambulator xizmat",
    "jarrohlik": "Jarrohlik Xizmati",
    "diagnostika": "Diagnostika Xizmatlari",
    "dori_darmon": "Dori-Darmon Ta'minoti",
    "moliya": "Moliyaviy Ko'rsatkichlar",
    "bemorlar_statistikasi": "Bemorlar Statistikasi",
    "sifat_korsatkichlari": "Sifat Ko'rsatkichlari / WHO KPI",
    "shoshilinch_yordam": "Shoshilinch Tibbiy Yordam",
    "infratuzilma": "Infratuzilma",
    "it_raqamlashtirish": "IT va Raqamlashtirish",
    "xalqaro_hamkorlik": "Xalqaro Hamkorlik",
    "talim_ilmfan": "Ta'lim va Ilm-fan",
    "bemor_qoniqishi": "Bemor Qoniqishi",
    "infeksiya_nazorati": "Infeksiya Nazorati",
    "qon_banki": "Qon Banki",
    "reanimatsiya_intensiv": "Reanimatsiya va Intensiv Terapiya",
    "reabilitatsiya": "Reabilitatsiya Xizmati",
    "inson_resurslari": "Inson Resurslari Boshqaruvi",
    "xavfsizlik": "Xavfsizlik",
    "ekologiya": "Ekologiya va Atrof-muhit",
    "raqobatchilar": "Raqobatchilar Tahlili",
    "hududiy_salomatlik": "Hududiy Salomatlik Ko'rsatkichlari",
    "davlat_dasturlari": "Davlat Dasturlari",
    "telemedicina": "Telemedicina Xizmatlari",
    "kelajak_rejalari": "Kelajak Rejalari",
    "qonunchilik": "Qonunchilik va Regulyativ",
    "simulyatsiya_maqsadlari": "Simulyatsiya Maqsadlari",
}


# ============================================================================
# PROGRESS COUNTER
# ============================================================================
def count_filled(d):
    total = 0
    filled = 0
    if isinstance(d, dict):
        for v in d.values():
            t, f = count_filled(v)
            total += t
            filled += f
    elif isinstance(d, list):
        if len(d) > 0 and isinstance(d[0], dict):
            for item in d:
                t, f = count_filled(item)
                total += t
                filled += f
        else:
            total += 1
            if len(d) > 0:
                filled += 1
    elif isinstance(d, bool):
        total += 1
        if d:
            filled += 1
    elif isinstance(d, (int, float)):
        total += 1
        if d != 0:
            filled += 1
    elif isinstance(d, str):
        total += 1
        if d.strip():
            filled += 1
    return total, filled


# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="BVKTM Ma'lumot Tizimi",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load data
if "data" not in st.session_state:
    st.session_state["data"] = load_data()

# Ensure all sections exist in data
for sec_key in SECTION_KEYS:
    if sec_key not in st.session_state["data"]:
        st.session_state["data"][sec_key] = copy.deepcopy(BARCHA_BOLIMLAR[sec_key])


# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    st.title("BVKTM Tizimi")
    st.caption("Buxoro Viloyat Ko'p Tarmoqli Tibbiy Markazi")
    st.markdown("---")

    # Progress
    data = st.session_state["data"]
    total_f, filled_f = count_filled(data)
    pct_done = (filled_f / max(total_f, 1)) * 100

    st.metric("To'ldirilgan", str(filled_f) + "/" + str(total_f))
    st.progress(pct_done / 100)
    st.caption(str(round(pct_done, 1)) + "% tayyor")
    st.markdown("---")

    # SAVE button — FAQAT GitHub'ga merge bilan saqlaydi
    if st.button("SAQLASH", type="primary", use_container_width=True):
        ok, msg = save_to_github(st.session_state["data"])
        if ok:
            st.success(msg)
        else:
            st.error("Xato: " + msg)
            # Fallback: lokal saqlash
            save_data(st.session_state["data"])

    # Download JSON
    st.download_button(
        "JSON yuklab olish",
        data=json.dumps(st.session_state["data"], ensure_ascii=False, indent=2),
        file_name="bvktm_data.json",
        mime="application/json",
        use_container_width=True,
    )

    # Upload JSON
    uploaded = st.file_uploader("JSON yuklash (import)", type=["json"], key="json_upload")
    if uploaded is not None:
        try:
            imported = json.load(uploaded)
            st.session_state["data"] = imported
            save_data(imported)
            st.success("Yuklandi! " + str(len(str(imported))) + " bayt")
            st.rerun()
        except Exception as e:
            st.error("Xato: " + str(e))

    # Load from GitHub
    if st.button("GitHub'dan yuklash", use_container_width=True):
        gh_data, _ = load_from_github()
        if gh_data:
            st.session_state["data"] = gh_data
            save_data_local(gh_data)
            st.success("GitHub'dan yuklandi!")
            st.rerun()
        else:
            st.warning("GitHub'da ma'lumot topilmadi.")

    st.markdown("---")

    # Section selector
    section_labels_list = list(SECTION_LABELS.values())
    section = st.radio("Bo'limni tanlang:", section_labels_list)

# Get the selected section key
selected_idx = section_labels_list.index(section)
selected_key = SECTION_KEYS[selected_idx]


# ============================================================================
# MAIN AREA
# ============================================================================
header_text = SECTION_HEADERS.get(selected_key, selected_key)
st.header(header_text)

# Info box at the top of each section
_section_brief = {
    "markaz_profili": "Markazning rasmiy nomi, rahbariyat, manzil, reyting va umumiy sonlarni kiriting.",
    "bolimlar": "27 ta bo'limning har biri uchun boshlig'i, xodimlar, karavotlar va statistikani kiriting.",
    "kadrlar": "Xodimlar tarkibi, ilmiy darajalar, maoshlar va kadrlar yetishmasligini kiriting.",
    "tibbiy_jihozlar": "MRT, KT, UZI va barcha tibbiy jihozlar soni, holati va texnik xizmatini kiriting.",
    "toshak_fondi": "Bo'limlar bo'yicha karavotlar taqsimoti va oylik bandlik statistikasini kiriting.",
    "poliklinika": "Ambulator qabul sig'imi, tashriflar, kutish vaqti va xizmatlar mavjudligini kiriting.",
    "jarrohlik": "Operatsiya xonalari, operatsiyalar soni, sifat va anesteziya ko'rsatkichlarini kiriting.",
    "diagnostika": "Laboratoriya testlari, tasvir diagnostikasi va natija berish vaqtlarini kiriting.",
    "dori_darmon": "Dorixona, dori byudjeti, antibiotik siyosati va saqlash sharoitini kiriting.",
    "moliya": "Daromadlar, xarajatlar, investitsiyalar va moliyaviy audit ma'lumotlarini kiriting.",
    "bemorlar_statistikasi": "Statsionar/ambulator bemorlar, demografiya, o'lim va shikoyat statistikasini kiriting.",
    "sifat_korsatkichlari": "WHO KPI: o'lim, infeksiya, kutish vaqti, muvofiqlik ko'rsatkichlarini kiriting.",
    "shoshilinch_yordam": "Tez yordam, shoshilinch bo'lim, javob vaqtlari va ofat tayorgarligini kiriting.",
    "infratuzilma": "Bino, energiya, suv, yong'in xavfsizligi va yordamchi xizmatlarni kiriting.",
    "it_raqamlashtirish": "HIS, EMR, internet, kompyuterlar va kiberxavfsizlik ma'lumotlarini kiriting.",
    "xalqaro_hamkorlik": "Xalqaro hamkorlar, loyihalar, tibbiy turizm va sertifikatlarni kiriting.",
    "talim_ilmfan": "Ta'lim bazasi, ilmiy maqolalar, dissertatsiyalar va grantlarni kiriting.",
    "bemor_qoniqishi": "Qoniqish ballari, shikoyatlar, NPS va media eslatmalarni kiriting.",
    "infeksiya_nazorati": "Infeksiya foizlari, gigiena, sterilizatsiya va skrining ma'lumotlarini kiriting.",
    "qon_banki": "Qon toplash, komponentlar tayyorlash, skrining va zaxiralarni kiriting.",
    "reanimatsiya_intensiv": "RIT karavotlar, jihozlar, sifat va protokollar ma'lumotlarini kiriting.",
    "reabilitatsiya": "Reabilitatsiya turlari, kadrlar, jihozlar va natijalarni kiriting.",
    "inson_resurslari": "Yollash, saqlash, baholash va ijtimoiy ta'minot ma'lumotlarini kiriting.",
    "xavfsizlik": "Qorovul, kameralar, yong'in, ofat tayorgarligi va hodisalarni kiriting.",
    "ekologiya": "Chiqindi boshqarish, energiya tejash va ekologik audit ma'lumotlarini kiriting.",
    "raqobatchilar": "Raqobatchi kasalxonalar haqida taqqoslash ma'lumotlarini kiriting.",
    "hududiy_salomatlik": "Viloyat aholisi salomatligi, kasalliklar tarqalishi va resurslarni kiriting.",
    "davlat_dasturlari": "DSTI, bepul yordam kvotalari va milliy dasturlarga ishtirokni kiriting.",
    "telemedicina": "Telemedicina platformasi, konsultatsiyalar va qamrov ma'lumotlarini kiriting.",
    "kelajak_rejalari": "Qisqa, o'rta, uzoq muddatli rejalar va KPI maqsadlarini kiriting.",
    "qonunchilik": "Litsenziyalar, akkreditatsiya, audit va huquqiy muvofiqlikni kiriting.",
    "simulyatsiya_maqsadlari": "AI tahlil uchun maqsad vaznlari, cheklovlar va stsenariylarni kiriting.",
}
_brief = _section_brief.get(selected_key, "")
if _brief:
    st.info(_brief)

if selected_key == "bolimlar":
    render_list_section("bolimlar", _bolim_shablon, "Bo'lim")

elif selected_key == "raqobatchilar":
    render_list_section("raqobatchilar", _raqobatchi_shablon, "Raqobatchi")

elif selected_key == "simulyatsiya_maqsadlari":
    # This section has nested dicts (stsenariylar), handle with auto_render_dict
    schema = BARCHA_BOLIMLAR["simulyatsiya_maqsadlari"]
    auto_render_dict(schema, "simulyatsiya_maqsadlari")

else:
    # All other dict-based sections
    schema = BARCHA_BOLIMLAR[selected_key]
    if isinstance(schema, dict):
        auto_render_dict(schema, selected_key)
    else:
        st.warning("Bu bo'lim uchun maxsus renderer kerak.")

# Section guide at bottom
_guide_text = SECTION_GUIDES.get(selected_key, "")
if _guide_text:
    with st.expander("Yo'riqnoma - bu bo'limni qanday to'ldirish kerak", expanded=False):
        st.markdown(_guide_text)

# Auto-save after rendering
save_data(st.session_state["data"])

# Footer
st.markdown("---")
st.caption(
    "BVKTM Ma'lumot Tizimi | "
    + str(total_f) + " parametr | "
    + "Oxirgi yangilash: " + datetime.now().strftime("%Y-%m-%d %H:%M")
)
