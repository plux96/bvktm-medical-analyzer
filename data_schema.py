"""
BVKTM - Buxoro Viloyat Ko'p Tarmoqli Tibbiy Markazi
Data Schema - Ma'lumotlar sxemasi

Bukhara Regional Multidisciplinary Medical Center
455 karavot, 137 shifokor, 27 mutaxassislik

Barcha qiymatlar default: 0, "", False, []
Foydalanuvchi Streamlit orqali to'ldiradi.
"""

# =============================================================================
# 1. MARKAZ_PROFILI - Tibbiy markaz umumiy ma'lumotlari (60 parametr)
# =============================================================================

MARKAZ_PROFILI = {
    # Asosiy ma'lumotlar
    "nomi": "",
    "qisqa_nomi": "",
    "nomi_ru": "",
    "nomi_en": "",
    "turi": "",  # davlat / xususiy / aralash
    "tashkil_etilgan_yil": 0,
    "litsenziya_raqami": "",
    "litsenziya_berilgan_sana": "",
    "litsenziya_amal_qilish_muddati": "",
    "akkreditatsiya_darajasi": "",
    "akkreditatsiya_sanasi": "",
    "akkreditatsiya_muddati": "",

    # Bosh shifokor
    "bosh_shifokor_ismi": "",
    "bosh_shifokor_ilmiy_darajasi": "",
    "bosh_shifokor_telefon": "",
    "bosh_shifokor_email": "",
    "bosh_shifokor_ish_boshlagan_yil": 0,
    "bosh_shifokor_tajriba_yil": 0,

    # O'rinbosarlar
    "davolash_orinbosari": "",
    "ilmiy_orinbosari": "",
    "iqtisodiy_orinbosari": "",
    "xo_jalik_orinbosari": "",

    # Manzil
    "manzil": "",
    "shahar": "",
    "viloyat": "",
    "pochta_indeksi": "",
    "koordinata_lat": 0.0,
    "koordinata_lon": 0.0,
    "shahar_markazidan_masofa_km": 0.0,
    "aeroportdan_masofa_km": 0.0,
    "temir_yol_vokzalidan_masofa_km": 0.0,

    # Aloqa
    "veb_sayt": "",
    "email": "",
    "telefon_asosiy": "",
    "telefon_qabulxona": "",
    "telefon_tez_yordam": "",
    "faks": "",
    "telegram_kanal": "",
    "instagram": "",
    "facebook": "",

    # Reyting
    "google_reyting": 0.0,
    "yandex_reyting": 0.0,
    "twogis_reyting": 0.0,
    "google_sharhlar_soni": 0,
    "yandex_sharhlar_soni": 0,
    "twogis_sharhlar_soni": 0,

    # Xodimlar umumiy
    "jami_xodimlar": 0,
    "jami_shifokorlar": 0,
    "jami_hamshiralar": 0,
    "jami_karavotlar": 0,

    # Yuridik ma'lumotlar
    "inn": "",
    "okonx": "",
    "bank_nomi": "",
    "hisob_raqami": "",
    "mfo": "",

    # Ish tartibi
    "ish_vaqti_boshlanish": "",
    "ish_vaqti_tugash": "",
    "tez_yordam_24_7": False,
    "shanba_ishlaydi": False,
    "yakshanba_ishlaydi": False,

    # Missiya va qadriyatlar
    "missiya": "",
    "vizyon": "",
    "qadriyatlar": "",

    # Yutuqlar
    "mukofotlar": [],
    "yutuqlar": [],
    "sertifikatlar": [],
    "iso_sertifikat": False,
    "jci_akkreditatsiya": False,
}


# =============================================================================
# 2. BOLIMLAR - Bo'limlar ro'yxati (27 bo'lim, har biri 80+ parametr)
# =============================================================================

def _bolim_shablon():
    """Har bir bo'lim uchun default shablon"""
    return {
        "nomi": "",
        "nomi_ru": "",
        "nomi_en": "",
        "turi": "",  # statsionar / poliklinika / diagnostika / xizmat
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,  # 1-10
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    }


# 27 bo'lim - har biri to'liq parametrlar bilan
BOLIMLAR = [
    # 1. Kardiologiya
    {
        "nomi": "Kardiologiya",
        "nomi_ru": "Кардиология",
        "nomi_en": "Cardiology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 2. Nevrologiya
    {
        "nomi": "Nevrologiya",
        "nomi_ru": "Неврология",
        "nomi_en": "Neurology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 3. Gastroenterologiya
    {
        "nomi": "Gastroenterologiya",
        "nomi_ru": "Гастроэнтерология",
        "nomi_en": "Gastroenterology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 4. Pulmonologiya
    {
        "nomi": "Pulmonologiya",
        "nomi_ru": "Пульмонология",
        "nomi_en": "Pulmonology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 5. Allergologiya
    {
        "nomi": "Allergologiya",
        "nomi_ru": "Аллергология",
        "nomi_en": "Allergology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 6. Revmatologiya
    {
        "nomi": "Revmatologiya",
        "nomi_ru": "Ревматология",
        "nomi_en": "Rheumatology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 7. Nefrologiya va gemodializ
    {
        "nomi": "Nefrologiya va gemodializ",
        "nomi_ru": "Нефрология и гемодиализ",
        "nomi_en": "Nephrology and Hemodialysis",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 8. Endokrinologiya
    {
        "nomi": "Endokrinologiya",
        "nomi_ru": "Эндокринология",
        "nomi_en": "Endocrinology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 9. Gematologiya
    {
        "nomi": "Gematologiya",
        "nomi_ru": "Гематология",
        "nomi_en": "Hematology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 10. Terapiya
    {
        "nomi": "Terapiya",
        "nomi_ru": "Терапия",
        "nomi_en": "Internal Medicine",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 11. Jarrohlik (umumiy)
    {
        "nomi": "Jarrohlik (umumiy)",
        "nomi_ru": "Хирургия (общая)",
        "nomi_en": "General Surgery",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 12. Travmatologiya
    {
        "nomi": "Travmatologiya",
        "nomi_ru": "Травматология",
        "nomi_en": "Traumatology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 13. Urologiya
    {
        "nomi": "Urologiya",
        "nomi_ru": "Урология",
        "nomi_en": "Urology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 14. Ginekologiya
    {
        "nomi": "Ginekologiya",
        "nomi_ru": "Гинекология",
        "nomi_en": "Gynecology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 15. Akusherlik
    {
        "nomi": "Akusherlik",
        "nomi_ru": "Акушерство",
        "nomi_en": "Obstetrics",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 16. LOR (Otorinolaringologiya)
    {
        "nomi": "LOR (Otorinolaringologiya)",
        "nomi_ru": "ЛОР (Оториноларингология)",
        "nomi_en": "ENT (Otorhinolaryngology)",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 17. Oftalmologiya
    {
        "nomi": "Oftalmologiya",
        "nomi_ru": "Офтальмология",
        "nomi_en": "Ophthalmology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 18. Dermatologiya
    {
        "nomi": "Dermatologiya",
        "nomi_ru": "Дерматология",
        "nomi_en": "Dermatology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 19. Onkologiya
    {
        "nomi": "Onkologiya",
        "nomi_ru": "Онкология",
        "nomi_en": "Oncology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 20. Pediatriya
    {
        "nomi": "Pediatriya",
        "nomi_ru": "Педиатрия",
        "nomi_en": "Pediatrics",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 21. Anesteziologiya va reanimatsiya
    {
        "nomi": "Anesteziologiya va reanimatsiya",
        "nomi_ru": "Анестезиология и реанимация",
        "nomi_en": "Anesthesiology and Intensive Care",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 22. Endovaskulyar jarrohlik
    {
        "nomi": "Endovaskulyar jarrohlik",
        "nomi_ru": "Эндоваскулярная хирургия",
        "nomi_en": "Endovascular Surgery",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 23. Rentgenologiya
    {
        "nomi": "Rentgenologiya",
        "nomi_ru": "Рентгенология",
        "nomi_en": "Radiology",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 24. Funktsional diagnostika
    {
        "nomi": "Funktsional diagnostika",
        "nomi_ru": "Функциональная диагностика",
        "nomi_en": "Functional Diagnostics",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 25. Laboratoriya
    {
        "nomi": "Laboratoriya",
        "nomi_ru": "Лаборатория",
        "nomi_en": "Laboratory",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 26. Fizioterapiya
    {
        "nomi": "Fizioterapiya",
        "nomi_ru": "Физиотерапия",
        "nomi_en": "Physiotherapy",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
    # 27. Reabilitatsiya
    {
        "nomi": "Reabilitatsiya",
        "nomi_ru": "Реабилитация",
        "nomi_en": "Rehabilitation",
        "turi": "",
        "boshlig_ismi": "",
        "boshlig_ilmiy_darajasi": "",
        "boshlig_telefon": "",
        "boshlig_tajriba_yil": 0,
        "karavotlar_soni": 0,
        "xodimlar_soni": 0,
        "shifokorlar_soni": 0,
        "hamshiralar_soni": 0,
        "kichik_tibbiy_xodimlar": 0,
        "tashkil_etilgan_yil": 0,
        "qavat": 0,
        "xonalar_raqami": "",
        "maydon_m2": 0.0,
        "telefon": "",
        "ish_vaqti": "",
        "bemorlar_kuniga": 0,
        "bemorlar_oyiga": 0,
        "bemorlar_yiliga": 0,
        "operatsiyalar_yiliga": 0,
        "ortacha_yotish_kun": 0.0,
        "karavot_bandlik_foiz": 0.0,
        "o_lim_ko_rsatkich": 0.0,
        "qayta_yotqizish_foiz": 0.0,
        "infeksiya_ko_rsatkich": 0.0,
        "bemor_qoniqish_ball": 0.0,
        "jihozlar_royxati": [],
        "asosiy_protseduralar": [],
        "davolanadigan_kasalliklar": [],
        "reanimatsiya_bor": False,
        "operatsiya_xonasi_bor": False,
        "byudjet": 0,
        "daromad": 0,
        "akkreditatsiya_bor": False,
        "oxirgi_remont_yili": 0,
        "holat_bahosi": 0,
        "kunduzgi_statsionar": False,
        "navbatchilik_bor": False,
        "ilmiy_faoliyat": False,
        "talim_baza": False,
        "yangi_texnologiyalar": [],
        "rejalashtirilgan_yangiliklar": [],
    },
]


# =============================================================================
# 3. KADRLAR - Xodimlar tarkibi (70 parametr)
# =============================================================================

KADRLAR = {
    # Umumiy tarkib
    "jami_xodimlar": 0,
    "shifokorlar_soni": 0,
    "hamshiralar_soni": 0,
    "kichik_tibbiy_xodimlar": 0,
    "ma_muriy_xodimlar": 0,
    "texnik_xodimlar": 0,
    "farmatsevtlar": 0,
    "laborantlar": 0,

    # Ilmiy daraja bo'yicha
    "phd_soni": 0,
    "dsc_soni": 0,
    "professor_soni": 0,
    "dotsent_soni": 0,
    "oliy_toifa": 0,
    "birinchi_toifa": 0,
    "ikkinchi_toifa": 0,
    "toifasiz": 0,

    # Demografiya
    "ortacha_yosh": 0.0,
    "erkaklar_foiz": 0.0,
    "ayollar_foiz": 0.0,
    "kadrlar_almashinuvi_foiz": 0.0,
    "ortacha_ish_staji_yil": 0.0,

    # Maosh
    "shifokor_maosh_min": 0,
    "shifokor_maosh_max": 0,
    "shifokor_maosh_ortacha": 0,
    "hamshira_maosh_min": 0,
    "hamshira_maosh_max": 0,
    "hamshira_maosh_ortacha": 0,
    "ma_muriy_maosh_min": 0,
    "ma_muriy_maosh_max": 0,
    "ma_muriy_maosh_ortacha": 0,

    # Malaka oshirish
    "yillik_talim_soati": 0,
    "xalqaro_talim_soni": 0,
    "konferensiya_ishtirok_soni": 0,
    "sertifikat_olganlar_soni": 0,
    "onlayn_kurslar_soni": 0,

    # Bo'sh o'rinlar
    "vakansiyalar_soni": 0,
    "shifokor_yetishmaslik_foiz": 0.0,
    "hamshira_yetishmaslik_foiz": 0.0,

    # Ish tartibi
    "tungi_navbat_xodimlar": 0,
    "dam_olish_kuni_xodimlar": 0,
    "navbatchilik_shifokorlar": 0,
    "navbatchilik_hamshiralar": 0,

    # Chet el
    "xorijiy_shifokorlar": 0,
    "tashrif_buyuruvchi_mutaxassislar_yiliga": 0,
    "xorijda_tajriba_ortganlar": 0,

    # Qoniqish
    "xodimlar_qoniqish_ball": 0.0,
    "burnout_indeks": 0.0,
    "mehnat_muhofazasi_ball": 0.0,

    # Tillar
    "uzbek_tili_foiz": 0.0,
    "rus_tili_foiz": 0.0,
    "ingliz_tili_foiz": 0.0,
    "nemis_tili_foiz": 0.0,
    "boshqa_tillar_foiz": 0.0,

    # Qo'shimcha
    "rezidentlar_soni": 0,
    "internlar_soni": 0,
    "volontyorlar_soni": 0,
    "shartnomali_xodimlar": 0,
    "yarim_stavka_xodimlar": 0,
    "pensioner_xodimlar": 0,
    "yoshlar_30_yosh_gacha_foiz": 0.0,
    "ilmiy_rahbarlar_soni": 0,
    "dissertatsiya_himoya_qilganlar_yiliga": 0,
    "sportchilar_soni": 0,
    "kasaba_uyushmasi_azolar_soni": 0,
    "intizomiy_jazo_yiliga": 0,
    "mukofotlanganlar_yiliga": 0,
}


# =============================================================================
# 4. TIBBIY_JIHOZLAR - Tibbiy jihozlar (60 parametr)
# =============================================================================

TIBBIY_JIHOZLAR = {
    # Umumiy
    "jami_jihozlar_soni": 0,
    "jami_jihozlar_qiymati": 0,

    # MRT (MRI)
    "mrt_soni": 0,
    "mrt_brendi": "",
    "mrt_tesla": 0.0,
    "mrt_ishlab_chiqarilgan_yil": 0,
    "mrt_holati": "",
    "mrt_yillik_tekshiruvlar": 0,

    # KT (CT)
    "kt_soni": 0,
    "kt_brendi": "",
    "kt_srezlar_soni": 0,
    "kt_ishlab_chiqarilgan_yil": 0,
    "kt_holati": "",
    "kt_yillik_tekshiruvlar": 0,

    # Rentgen
    "rentgen_soni": 0,
    "rentgen_raqamli_analog": "",
    "rentgen_ishlab_chiqarilgan_yil": 0,
    "rentgen_yillik_tekshiruvlar": 0,

    # Ultratovush (UTT)
    "utt_soni": 0,
    "utt_brendlar": "",
    "utt_turlari": [],  # qorin, yurak, akusherlik, va h.k.
    "utt_yillik_tekshiruvlar": 0,

    # Endoskopiya
    "endoskopiya_soni": 0,
    "endoskopiya_turlari": [],

    # Funktsional diagnostika jihozlari
    "ekg_apparatlari_soni": 0,
    "eeg_apparatlari_soni": 0,
    "emg_apparatlari_soni": 0,
    "spirometr_soni": 0,

    # Laboratoriya jihozlari
    "bioximiya_analizator_soni": 0,
    "gematologiya_analizator_soni": 0,
    "immunologiya_analizator_soni": 0,
    "koagulyatsiya_analizator_soni": 0,
    "pcr_apparat_soni": 0,

    # Jarrohlik jihozlari
    "laparoskopik_to_plam_soni": 0,
    "artroskopik_to_plam_soni": 0,
    "jarrohlik_mikroskop_soni": 0,
    "elektrokoagulyator_soni": 0,

    # Anesteziologiya va reanimatsiya
    "narkoz_apparati_soni": 0,
    "sun_iy_nafas_apparati_soni": 0,
    "defibrillyator_soni": 0,
    "monitoring_tizimi_soni": 0,
    "infuzion_nasos_soni": 0,

    # Dializ
    "dializ_apparatlari_soni": 0,

    # Tez yordam
    "tez_yordam_mashinalari_soni": 0,
    "tez_yordam_turlari": [],
    "tez_yordam_jihozlangan": False,

    # Sterilizatsiya
    "sterilizatsiya_jihozlari_soni": 0,
    "avtoklav_soni": 0,

    # Umumiy ko'rsatkichlar
    "jihozlar_ortacha_yoshi": 0.0,
    "texnik_xizmat_byudjeti": 0,
    "ta_mirlash_ortacha_vaqti_kun": 0,
    "jihozlar_foydalanish_foiz": 0.0,
    "ishlamay_turish_soat_oyiga": 0,
    "rejalashtirilgan_xaridlar": [],
    "yangi_jihozlar_byudjeti": 0,
    "mammograf_soni": 0,
    "angiogiraf_soni": 0,
}


# =============================================================================
# 5. TOSHAK_FONDI - Karavot fondi (50 parametr)
# =============================================================================

TOSHAK_FONDI = {
    # Umumiy
    "jami_karavotlar": 0,
    "kardiologiya_karavotlar": 0,
    "nevrologiya_karavotlar": 0,
    "gastroenterologiya_karavotlar": 0,
    "pulmonologiya_karavotlar": 0,
    "allergologiya_karavotlar": 0,
    "revmatologiya_karavotlar": 0,
    "nefrologiya_karavotlar": 0,
    "endokrinologiya_karavotlar": 0,
    "gematologiya_karavotlar": 0,
    "terapiya_karavotlar": 0,
    "jarrohlik_karavotlar": 0,
    "travmatologiya_karavotlar": 0,
    "urologiya_karavotlar": 0,
    "ginekologiya_karavotlar": 0,
    "akusherlik_karavotlar": 0,
    "lor_karavotlar": 0,
    "oftalmologiya_karavotlar": 0,
    "dermatologiya_karavotlar": 0,
    "onkologiya_karavotlar": 0,
    "pediatriya_karavotlar": 0,

    # Maxsus karavotlar
    "reanimatsiya_karavotlar": 0,
    "jarrohlik_reanimatsiya_karavotlar": 0,
    "neonatal_karavotlar": 0,
    "shoshilinch_karavotlar": 0,
    "izolyatsiya_karavotlar": 0,

    # VIP / Pullik
    "vip_xonalar_soni": 0,
    "pullik_xonalar_soni": 0,
    "standart_xonalar_soni": 0,
    "bir_o_rinli_xonalar": 0,
    "ikki_o_rinli_xonalar": 0,
    "ko_p_o_rinli_xonalar": 0,

    # Ko'rsatkichlar
    "karavot_bandlik_umumiy_foiz": 0.0,
    "ortacha_yotish_kun_umumiy": 0.0,
    "karavot_aylanmasi": 0.0,

    # Mavsumiy bandlik (oylar bo'yicha)
    "bandlik_yanvar": 0.0,
    "bandlik_fevral": 0.0,
    "bandlik_mart": 0.0,
    "bandlik_aprel": 0.0,
    "bandlik_may": 0.0,
    "bandlik_iyun": 0.0,
    "bandlik_iyul": 0.0,
    "bandlik_avgust": 0.0,
    "bandlik_sentyabr": 0.0,
    "bandlik_oktyabr": 0.0,
    "bandlik_noyabr": 0.0,
    "bandlik_dekabr": 0.0,

    # Qo'shimcha
    "har_1000_aholiga_karavot": 0.0,
    "kengaytirish_rejasi": "",
    "kunduzgi_statsionar_o_rinlar": 0,
}


# =============================================================================
# 6. POLIKLINIKA - Ambulator poliklinika (50 parametr)
# =============================================================================

POLIKLINIKA = {
    # Sig'im
    "smenada_qabul_sig_imi": 0,
    "mutaxassisliklar_soni": 0,
    "mutaxassisliklar_royxati": [],

    # Xodimlar
    "poliklinika_shifokorlar": 0,
    "poliklinika_hamshiralar": 0,
    "registrator_soni": 0,

    # Tashrif statistikasi
    "kunlik_tashriflar_haqiqiy": 0,
    "oylik_tashriflar": 0,
    "yillik_tashriflar": 0,
    "yangi_bemorlar_foiz": 0.0,
    "qayta_tashriflar_foiz": 0.0,

    # Kutish vaqti
    "ortacha_kutish_vaqti_daqiqa": 0,
    "maksimal_kutish_vaqti_daqiqa": 0,

    # Navbat tizimi
    "onlayn_yozilish": False,
    "telefon_yozilish": False,
    "navbatsiz_qabul": False,
    "elektron_navbat_tizimi": False,

    # Uyga chaqirish
    "uyga_chaqirish_oyiga": 0,
    "uyga_chaqirish_shifokorlar": 0,

    # Dispanser
    "dispanser_bemorlar_soni": 0,
    "dispanser_kasalliklar": [],

    # Profilaktika
    "profilaktik_tekshiruvlar_yiliga": 0,
    "skrining_dasturlari": [],

    # Ish tartibi
    "ish_vaqti_boshlanish": "",
    "ish_vaqti_tugash": "",
    "shanba_ishlaydi": False,
    "shanba_ish_vaqti": "",

    # Bemor qoniqishi
    "bemor_qoniqish_ball": 0.0,
    "shikoyatlar_soni_oyiga": 0,

    # Daromad
    "pullik_xizmatlar_daromad": 0,
    "pullik_xizmatlar_royxati": [],
    "bepul_xizmatlar_hajmi": 0,

    # Yo'llanmalar
    "boshqa_muassasalarga_yollanma": 0,
    "respublika_darajasiga_yollanma": 0,

    # Surunkali kasalliklar
    "surunkali_kasallik_bemorlar": 0,
    "diabet_bemorlar": 0,
    "gipertoniya_bemorlar": 0,
    "bronxial_astma_bemorlar": 0,

    # Emlash
    "emlash_yiliga": 0,
    "bolalar_emlash": 0,
    "kattalar_emlash": 0,
    "gripp_emlash": 0,

    # Qo'shimcha
    "stomatologiya_xizmati": False,
    "fizioterapiya_xizmati": False,
    "ginekologik_qabul": False,
    "bolalar_qabul": False,
    "shoshilinch_qabul": False,
    "laboratoriya_xizmati": False,
    "utt_xizmati": False,
}


# =============================================================================
# 7. JARROHLIK - Jarrohlik xizmati (55 parametr)
# =============================================================================

JARROHLIK = {
    # Operatsiya xonalari
    "operatsiya_xonalari_soni": 0,
    "toza_operatsiya_xonalar": 0,
    "septik_operatsiya_xonalar": 0,
    "shoshilinch_operatsiya_xonalar": 0,

    # Umumiy statistika
    "jami_operatsiyalar_yiliga": 0,
    "jami_operatsiyalar_oyiga": 0,

    # Tur bo'yicha
    "rejali_operatsiyalar": 0,
    "shoshilinch_operatsiyalar": 0,
    "minimal_invaziv_operatsiyalar": 0,
    "endoskopik_operatsiyalar": 0,
    "laparoskopik_operatsiyalar": 0,
    "mikrojarrohlik_operatsiyalar": 0,

    # Bo'lim bo'yicha
    "umumiy_jarrohlik_operatsiyalar": 0,
    "travmatologiya_operatsiyalar": 0,
    "urologiya_operatsiyalar": 0,
    "ginekologiya_operatsiyalar": 0,
    "lor_operatsiyalar": 0,
    "oftalmologiya_operatsiyalar": 0,
    "kardiojarrohlik_operatsiyalar": 0,
    "tomir_jarrohlik_operatsiyalar": 0,
    "neyrojarrohlik_operatsiyalar": 0,
    "endovaskulyar_operatsiyalar": 0,
    "onkologik_operatsiyalar": 0,
    "pediatrik_operatsiyalar": 0,

    # Sifat ko'rsatkichlari
    "jarrohlik_olim_foiz": 0.0,
    "asoratlar_foiz": 0.0,
    "qayta_operatsiya_foiz": 0.0,
    "yara_infeksiyasi_foiz": 0.0,

    # Vaqt
    "ortacha_operatsiya_davomiyligi_daqiqa": 0,
    "kunduzgi_jarrohlik_foiz": 0.0,

    # Anesteziya turlari
    "umumiy_narkoz_foiz": 0.0,
    "spinal_anesteziya_foiz": 0.0,
    "mahalliy_anesteziya_foiz": 0.0,
    "sedatsiya_foiz": 0.0,
    "epidural_anesteziya_foiz": 0.0,

    # Eng ko'p bajariladigan operatsiyalar
    "eng_kop_operatsiyalar_royxati": [],

    # Transplantatsiya
    "transplantatsiya_imkoniyati": False,
    "transplantatsiya_turlari": [],

    # Robot-jarrohlik
    "robot_jarrohlik": False,
    "robot_jarrohlik_turi": "",

    # Kutish
    "rejali_operatsiya_kutish_kun": 0,
    "shoshilinch_operatsiya_reaktsiya_daqiqa": 0,

    # Qon
    "operatsiya_uchun_ortacha_qon_ml": 0,
    "qon_preparatlari_sarfi_yiliga": 0,

    # Qo'shimcha
    "operatsiyadan_keyingi_infeksiya_foiz": 0.0,
    "tromboemboliya_profilaktika_foiz": 0.0,
    "antibiotik_profilaktika_foiz": 0.0,
    "informed_consent_foiz": 0.0,
    "operatsiya_hisoboti_vaqti_soat": 0,
    "patologiya_tekshiruv_foiz": 0.0,
    "kriogenik_jarrohlik": False,
    "lazer_jarrohlik": False,
}


# =============================================================================
# 8. DIAGNOSTIKA - Diagnostika xizmatlari (65 parametr)
# =============================================================================

DIAGNOSTIKA = {
    # Laboratoriya umumiy
    "lab_testlar_kuniga": 0,
    "lab_testlar_turlari_soni": 0,
    "lab_natija_vaqti_soat": 0,
    "lab_aniqlik_foiz": 0.0,
    "lab_xodimlar_soni": 0,
    "lab_jihozlar_soni": 0,

    # Test turlari bo'yicha
    "bioximiya_testlar_kuniga": 0,
    "gematologiya_testlar_kuniga": 0,
    "koagulyatsiya_testlar_kuniga": 0,
    "immunologiya_testlar_kuniga": 0,
    "mikrobiologiya_testlar_kuniga": 0,
    "pcr_testlar_kuniga": 0,
    "sitologiya_testlar_kuniga": 0,
    "gistologiya_testlar_kuniga": 0,
    "siydik_tahlili_kuniga": 0,
    "parazitologiya_testlar_kuniga": 0,
    "gormon_testlar_kuniga": 0,
    "onkomarker_testlar_kuniga": 0,

    # Radiologiya
    "rentgen_kuniga": 0,
    "kt_tekshiruvlar_kuniga": 0,
    "mrt_tekshiruvlar_kuniga": 0,
    "utt_tekshiruvlar_kuniga": 0,
    "mammografiya_kuniga": 0,
    "angiografiya_oyiga": 0,
    "densitometriya_oyiga": 0,
    "flyuorografiya_kuniga": 0,

    # Funktsional diagnostika
    "ekg_kuniga": 0,
    "exokg_kuniga": 0,
    "eeg_kuniga": 0,
    "emg_kuniga": 0,
    "spirometriya_kuniga": 0,
    "stress_test_oyiga": 0,
    "xolter_monitoring_oyiga": 0,
    "smad_monitoring_oyiga": 0,
    "veloergometriya_oyiga": 0,

    # Endoskopiya
    "gastroskopiya_oyiga": 0,
    "kolonoskopiya_oyiga": 0,
    "bronxoskopiya_oyiga": 0,
    "sistoskopiya_oyiga": 0,
    "rektoromanoskopiya_oyiga": 0,

    # Patologiya
    "biopsiya_oyiga": 0,
    "tsitologiya_oyiga": 0,
    "gistologiya_oyiga": 0,
    "immunogistokimyo_oyiga": 0,

    # Sifat
    "diagnostika_aniqlik_foiz": 0.0,
    "lab_xato_foiz": 0.0,
    "natija_berish_vaqti_lab_soat": 0,
    "natija_berish_vaqti_rentgen_soat": 0,
    "natija_berish_vaqti_mrt_soat": 0,
    "natija_berish_vaqti_kt_soat": 0,

    # Raqamlashtirish
    "pacs_tizimi": False,
    "lis_tizimi": False,
    "raqamli_arxiv": False,

    # Sun'iy intellekt
    "ai_diagnostika": False,
    "ai_diagnostika_turlari": [],
    "ai_aniqlik_foiz": 0.0,

    # Tashqi yo'llanmalar
    "tashqi_lab_yollanmalar_oyiga": 0,
    "tashqi_diagnostika_yollanmalar_oyiga": 0,

    # Qo'shimcha
    "allergologik_testlar_oyiga": 0,
    "genetik_testlar_oyiga": 0,
    "toksikologiya_testlar_oyiga": 0,
    "bakteriologik_testlar_kuniga": 0,
}


# =============================================================================
# 9. DORI_DARMON - Dori-darmon ta'minoti (40 parametr)
# =============================================================================

DORI_DARMON = {
    # Dorixona
    "dorixona_mavjud": False,
    "dorixona_turi": "",  # kasalxona / chakana
    "dorixona_xodimlar": 0,
    "dorixona_farmatsevtlar": 0,

    # Byudjet
    "yillik_dori_byudjeti": 0,
    "haqiqiy_xarajat": 0,
    "bir_bemorga_ortacha_dori_xarajati": 0,

    # Assortiment
    "dori_nomenklatura_soni": 0,
    "muhim_dorilar_mavjudligi_foiz": 0.0,
    "formulyar_royxati_soni": 0,

    # Nazorat
    "narkotik_dorilar_litsenziya": False,
    "nazorat_ostidagi_dorilar_hisobi": False,
    "narkotik_dorilar_soni": 0,
    "psixotrop_dorilar_soni": 0,

    # Ta'minot
    "dori_taqchillik_chastotasi_oyiga": 0,
    "taqchillik_dorilari_royxati": [],
    "zaxira_kunlar": 0,

    # Narx
    "retsept_ortacha_narxi": 0,
    "generik_foiz": 0.0,
    "brend_foiz": 0.0,

    # Xavfsizlik
    "dori_ozaro_tasir_tizimi": False,
    "dori_xatolik_soni_oyiga": 0,
    "allergiya_tekshirish_tizimi": False,

    # Antibiotik nazorati
    "antibiotik_stewardship_dasturi": False,
    "antibiotik_sarfi_ddd": 0.0,
    "antibiotik_retseptsiz_foiz": 0.0,

    # Sovuq zanjir
    "sovuq_zanjir_dorilar_boshqarish": False,
    "muzlatgich_soni": 0,
    "harorat_monitoring": False,

    # Yaroqsiz dorilar
    "muddati_otgan_dorilar_foiz": 0.0,
    "utilizatsiya_tizimi": False,

    # Xarid
    "xarid_usuli": "",  # tender / to'g'ridan-to'g'ri
    "asosiy_yetkazuvchilar_soni": 0,
    "import_dorilar_foiz": 0.0,
    "mahalliy_dorilar_foiz": 0.0,

    # Saqlash
    "saqlash_sharoiti_mos": False,
    "ombor_maydoni_m2": 0.0,
    "raqamli_dori_hisobi": False,
    "shtrix_kod_tizimi": False,
}


# =============================================================================
# 10. MOLIYA - Moliyaviy ko'rsatkichlar (60 parametr)
# =============================================================================

MOLIYA = {
    # Umumiy byudjet
    "yillik_byudjet": 0,
    "davlat_byudjet": 0,
    "sugurta_daromad": 0,
    "pullik_xizmatlar_daromad": 0,
    "grantlar_daromad": 0,
    "xayriya_daromad": 0,
    "boshqa_daromad": 0,

    # Daromad tarkibi
    "statsionar_daromad": 0,
    "ambulator_daromad": 0,
    "diagnostika_daromad": 0,
    "jarrohlik_daromad": 0,
    "pullik_xizmatlar_umumiy": 0,
    "laboratoriya_daromad": 0,
    "reabilitatsiya_daromad": 0,

    # Xarajatlar
    "maosh_xarajati": 0,
    "jihozlar_xarajati": 0,
    "dori_xarajati": 0,
    "kommunal_xarajat": 0,
    "ta_mirlash_xarajat": 0,
    "ovqatlantirish_xarajat": 0,
    "transport_xarajat": 0,
    "it_xarajat": 0,
    "boshqa_xarajat": 0,

    # Birlik ko'rsatkichlar
    "bir_karavotga_daromad": 0,
    "bir_shifokorga_daromad": 0,
    "bir_bemorga_daromad": 0,
    "bir_bemor_kun_tannarxi": 0,
    "bir_operatsiya_tannarxi": 0,
    "bir_ambulator_tashrif_tannarxi": 0,

    # Foyda/zarar
    "foyda_zarar": 0,
    "rentabellik_foiz": 0.0,

    # Sug'urta
    "dsti_tolovlar": 0,
    "oms_daromad": 0,
    "sugurta_kompaniyalar_soni": 0,

    # Qarz
    "debitor_qarzlar": 0,
    "kreditor_qarzlar": 0,
    "muddati_otgan_qarzlar": 0,

    # Investitsiya
    "oxirgi_3_yil_investitsiya": 0,
    "2024_investitsiya": 0,
    "2025_investitsiya": 0,
    "2026_investitsiya": 0,
    "rejalashtirilgan_investitsiya": 0,

    # Bajarish
    "byudjet_bajarish_foiz": 0.0,
    "maosh_fondi_foiz": 0.0,
    "pullik_xizmatlar_ulushi_foiz": 0.0,

    # Aholiga
    "jon_boshiga_moliyalashtirish": 0,

    # Audit
    "moliyaviy_audit_natijasi": "",
    "oxirgi_audit_sanasi": "",
    "audit_buzilishlar_soni": 0,

    # Qo'shimcha
    "amortizatsiya_xarajati": 0,
    "kapital_xarajatlar": 0,
    "joriy_xarajatlar": 0,
    "soliq_imtiyozlari": 0,
    "tender_tejamlari": 0,
    "energiya_tejamlari": 0,
    "raqamlashtirish_xarajati": 0,
    "xodimlar_ijtimoiy_paket": 0,
}


# =============================================================================
# 11. BEMORLAR_STATISTIKASI - Bemorlar statistikasi (75 parametr)
# =============================================================================

BEMORLAR_STATISTIKASI = {
    # Statsionar
    "statsionar_yotqizilganlar_yiliga": 0,
    "statsionar_chiqarilganlar_yiliga": 0,
    "statsionar_ortacha_kuniga": 0,
    "statsionar_maksimal_kuniga": 0,

    # Ambulator
    "ambulator_tashriflar_yiliga": 0,
    "ambulator_ortacha_kuniga": 0,
    "ambulator_maksimal_kuniga": 0,

    # Shoshilinch
    "shoshilinch_hollar_yiliga": 0,
    "tez_yordam_kelganlar": 0,
    "o_zi_kelganlar_shoshilinch": 0,
    "shoshilinch_yotqizilganlar": 0,

    # Demografiya - yosh
    "yosh_0_14_foiz": 0.0,
    "yosh_15_24_foiz": 0.0,
    "yosh_25_44_foiz": 0.0,
    "yosh_45_64_foiz": 0.0,
    "yosh_65_plus_foiz": 0.0,
    "ortacha_yosh": 0.0,

    # Demografiya - jins
    "erkaklar_foiz": 0.0,
    "ayollar_foiz": 0.0,

    # Geografiya
    "buxoro_shahar_foiz": 0.0,
    "buxoro_viloyat_foiz": 0.0,
    "boshqa_viloyatlar_foiz": 0.0,
    "xorijiy_bemorlar_soni": 0,

    # Top 10 diagnozlar
    "top10_diagnoz_statsionar": [],
    "top10_diagnoz_ambulator": [],

    # O'lim
    "jami_o_lim_yiliga": 0,
    "kardiologiya_o_lim": 0,
    "nevrologiya_o_lim": 0,
    "jarrohlik_o_lim": 0,
    "reanimatsiya_o_lim": 0,
    "onkologiya_o_lim": 0,
    "pulmonologiya_o_lim": 0,
    "terapiya_o_lim": 0,

    # O'lim - kasallik guruhi bo'yicha
    "yurak_qon_tomir_o_lim": 0,
    "onkologik_o_lim": 0,
    "nafas_yo_llari_o_lim": 0,
    "jarohatlari_o_lim": 0,
    "infeksion_o_lim": 0,
    "ona_o_limi": 0,
    "chaqaloq_o_limi": 0,

    # Jarrohlik vs terapevtik
    "jarrohlik_bemorlar_foiz": 0.0,
    "terapevtik_bemorlar_foiz": 0.0,

    # Kunduzgi statsionar
    "kunduzgi_statsionar_bemorlar": 0,
    "kunduzgi_protseduralar_yiliga": 0,

    # Uyda davolash
    "uyda_davolash_bemorlar": 0,
    "uyda_tashriflar_oyiga": 0,

    # Yo'llanmalar
    "respublika_darajasiga_yuborilgan": 0,
    "tibbiy_evakuatsiya_soni": 0,
    "boshqa_kasalxonadan_qabul": 0,

    # Bemor qoniqishi
    "so_rovnoma_natijalari_ball": 0.0,
    "so_rovnomada_ishtirok_foiz": 0.0,
    "tavsiya_etadi_foiz": 0.0,
    "nps_ball": 0,

    # Shikoyatlar
    "shikoyatlar_soni_yiliga": 0,
    "shikoyat_turlari": [],
    "shikoyat_hal_qilish_vaqti_kun": 0,
    "ijobiy_fikrlar_soni": 0,

    # Yuridik
    "sud_davo_soni": 0,
    "tibbiy_xato_davo_soni": 0,
    "kompensatsiya_tolanganlar": 0,

    # Media
    "ommaviy_axborot_ijobiy": 0,
    "ommaviy_axborot_salbiy": 0,

    # Qo'shimcha
    "ko_chirib_keltirilgan_bemorlar": 0,
    "vafot_etganlar_autopsiya_foiz": 0.0,
    "nogironlik_belgilangan": 0,
    "mehnat_layoqatsizlik_kunlar": 0,
    "o_rtacha_kasallik_tarixi_varaqlari": 0,
    "elektron_tarixi_foiz": 0.0,
    "dispanser_hisobdagilar": 0,
    "dializ_bemorlar": 0,
    "ximiyaterapiya_bemorlar": 0,
}


# =============================================================================
# 12. SIFAT_KORSATKICHLARI - Sifat ko'rsatkichlari / WHO KPI (80 parametr)
# =============================================================================

SIFAT_KORSATKICHLARI = {
    # O'lim ko'rsatkichlari
    "umumiy_o_lim_foiz": 0.0,
    "standartlashtirilgan_o_lim_nisbati": 0.0,
    "kutilmagan_o_lim_soni": 0,

    # Infeksiya
    "jarrohlik_yara_infeksiya_foiz": 0.0,
    "kasalxona_infeksiya_foiz": 0.0,
    "mrsa_foiz": 0.0,
    "clostridium_difficile_foiz": 0.0,

    # Qayta yotqizish
    "30_kunlik_qayta_yotqizish_foiz": 0.0,
    "7_kunlik_qayta_yotqizish_foiz": 0.0,

    # Karavot
    "ortacha_yotish_kun": 0.0,
    "karavot_bandlik_foiz": 0.0,
    "karavot_aylanma_intervali_kun": 0.0,

    # Bemor qoniqishi
    "bemor_qoniqish_ball": 0.0,
    "davolash_sifati_ball": 0.0,
    "kommunikatsiya_sifati_ball": 0.0,
    "tozalik_ball": 0.0,
    "ovqat_sifati_ball": 0.0,
    "maxfiylik_ball": 0.0,

    # Kutish vaqtlari
    "yotqizishgacha_kutish_soat": 0.0,
    "operatsiyagacha_kutish_soat": 0.0,
    "ambulator_kutish_daqiqa": 0,
    "shoshilinch_kutish_daqiqa": 0,
    "lab_natija_kutish_soat": 0.0,

    # Diagnostika sifati
    "diagnostika_aniqlik_foiz": 0.0,
    "lab_xato_foiz": 0.0,
    "rentgen_xato_foiz": 0.0,

    # Dori xatoliklari
    "dori_xatolik_1000_bemorga": 0.0,
    "dori_allergiya_holatlari": 0,
    "noto_gri_dori_berish": 0,

    # Bemor xavfsizligi
    "yiqilish_1000_bemorga": 0.0,
    "bosim_yarasi_foiz": 0.0,
    "chuqur_vena_trombozi_foiz": 0.0,
    "ote_foiz": 0.0,

    # Kasalxona infeksiyalari (HAI)
    "markaziy_kateter_infeksiya_clabsi": 0.0,
    "sun_iy_nafas_pnevmoniya_vap": 0.0,
    "siydik_kateter_infeksiya_cauti": 0.0,

    # Gigiena
    "qol_gigiena_muvofiqlik_foiz": 0.0,
    "shaxsiy_himoya_muvofiqlik_foiz": 0.0,
    "sterilizatsiya_muvofiqlik_foiz": 0.0,

    # Jarrohlik
    "antibiotik_profilaktika_muvofiqlik_foiz": 0.0,
    "informed_consent_muvofiqlik_foiz": 0.0,
    "jarrohlik_xavfsizlik_tekshiruv_foiz": 0.0,

    # Hujjatlar
    "tibbiy_hujjat_to_liqligi_foiz": 0.0,
    "epikriz_vaqtida_foiz": 0.0,
    "autopsia_foiz": 0.0,

    # Shoshilinch
    "shoshilinch_javob_vaqti_daqiqa": 0,
    "tez_yordam_javob_vaqti_daqiqa": 0,
    "door_to_balloon_vaqti_daqiqa": 0,
    "door_to_needle_vaqti_daqiqa": 0,

    # Ona va bola
    "ona_o_limi_nisbati": 0.0,
    "yangi_tugulgan_o_lim_foiz": 0.0,
    "o_lik_tugulish_foiz": 0.0,
    "kesarevo_foiz": 0.0,
    "muddatidan_oldin_tug_ish_foiz": 0.0,

    # Qon
    "qon_quyish_reaktsiya_foiz": 0.0,
    "noto_gri_qon_quyish": 0,

    # Xodimlar xavfsizligi
    "igna_jarohat_soni": 0,
    "xodimlar_emlash_foiz": 0.0,
    "kasbiy_kasallik_soni": 0,

    # Yong'in va xavfsizlik
    "yong_in_mashqi_chastotasi_yiliga": 0,
    "jihozlar_kalibrlash_muvofiqlik_foiz": 0.0,
    "dori_saqlash_muvofiqlik_foiz": 0.0,

    # Klinik protokollar
    "klinik_protokol_muvofiqlik_foiz": 0.0,
    "klinik_yo_l_xaritasi_soni": 0,
    "standart_davolash_muvofiqlik_foiz": 0.0,

    # Qo'shimcha WHO ko'rsatkichlari
    "qon_bosim_nazorat_foiz": 0.0,
    "diabet_nazorat_hba1c_foiz": 0.0,
    "antikoagulyant_nazorat_foiz": 0.0,
    "og_riq_boshqarish_ball": 0.0,
    "ovqatlanish_skrining_foiz": 0.0,
    "reabilitatsiya_boshlash_vaqti_soat": 0,
    "klinik_audit_soni_yiliga": 0,
    "peer_review_soni_yiliga": 0,
    "morbidity_mortality_konferensiya_soni": 0,
    "evidence_based_medicine_foiz": 0.0,
    "bemor_identifikatsiya_muvofiqlik_foiz": 0.0,
    "critical_value_xabar_berish_daqiqa": 0,
}


# =============================================================================
# 13. SHOSHILINCH_YORDAM - Shoshilinch tibbiy yordam (40 parametr)
# =============================================================================

SHOSHILINCH_YORDAM = {
    # Umumiy
    "shoshilinch_bolim_24_7": False,
    "shoshilinch_karavotlar": 0,
    "shoshilinch_xodimlar": 0,
    "shoshilinch_shifokorlar": 0,
    "shoshilinch_hamshiralar": 0,

    # Statistika
    "yillik_shoshilinch_tashriflar": 0,
    "kunlik_ortacha_tashriflar": 0,
    "eng_ko_p_kun_tashriflar": 0,

    # Tez yordam mashinalar
    "tez_yordam_soni": 0,
    "tez_yordam_turlari": [],
    "tez_yordam_jihozlangan_foiz": 0.0,
    "tez_yordam_ortacha_yoshi": 0.0,
    "tez_yordam_km_yiliga": 0,

    # Javob vaqti
    "shahar_javob_vaqti_daqiqa": 0,
    "qishloq_javob_vaqti_daqiqa": 0,
    "kasalxona_ichida_javob_daqiqa": 0,

    # Travma markazi
    "travma_markazi_darajasi": 0,
    "travma_operatsiya_imkoniyati": False,

    # Triage
    "triage_tizimi_turi": "",
    "triage_hamshira_soni": 0,
    "triage_vaqti_daqiqa": 0,

    # Reanimatsiya
    "reanimatsiya_imkoniyati": False,
    "defibrillyator_soni_shoshilinch": 0,

    # Insult / MI
    "insult_davolash_imkoniyati": False,
    "miokard_infarkti_davolash": False,
    "door_to_needle_daqiqa": 0,
    "door_to_balloon_daqiqa": 0,
    "trombolitik_terapiya": False,

    # Shoshilinch jarrohlik
    "shoshilinch_jarrohlik_24_7": False,
    "shoshilinch_jarrohlar_soni": 0,

    # Ofat tayyorgarligi
    "ofat_tayorgarlik_rejasi": False,
    "ommaviy_halokat_sig_imi": 0,
    "ofat_mashqlari_yiliga": 0,

    # Vertolyot
    "vertolyot_maydoni": False,

    # Zaharlanish
    "zaharlanish_nazorati": False,
    "antidot_zaxirasi": False,

    # Qo'shimcha
    "pediatrik_shoshilinch": False,
    "akusherlik_shoshilinch": False,
    "psixiatrik_shoshilinch": False,
    "kuyish_davolash": False,
}


# =============================================================================
# 14. INFRATUZILMA - Infratuzilma (55 parametr)
# =============================================================================

INFRATUZILMA = {
    # Hudud
    "umumiy_maydon_gektar": 0.0,
    "bino_maydoni_m2": 0.0,
    "yashil_hudud_m2": 0.0,

    # Binolar
    "binolar_soni": 0,
    "qavatlar_soni": 0,
    "qurilgan_yil": 0,
    "oxirgi_remont_yili": 0,
    "bino_holati_bahosi": 0,  # 1-10

    # Avtoturargoh
    "avto_turargoh_joy": 0,
    "tez_yordam_turargoh": 0,

    # Elektr ta'minoti
    "asosiy_elektr_tarmoq": False,
    "zahira_generator_kvt": 0,
    "ups_tizimi": False,
    "ups_tanqidiy_bolimlar": False,
    "elektr_sarfi_kvt_oyiga": 0,

    # Suv ta'minoti
    "suv_ta_minoti": False,
    "suv_tozalash": False,
    "issiq_suv": False,
    "suv_sarfi_m3_oyiga": 0,
    "suv_zaxira_hajmi_m3": 0,

    # Isitish / Sovutish
    "isitish_turi": "",
    "konditsioner_tizimi": False,
    "markaziy_isitish": False,
    "qozonxona_mavjud": False,

    # Lift
    "liftlar_soni": 0,
    "zambil_lifti": 0,
    "yuk_lifti": 0,

    # Yong'in xavfsizligi
    "yong_in_xavfsizlik_tizimi": False,
    "yong_in_signalizatsiya": False,
    "sprinkler_tizimi": False,
    "yong_in_o_chirish_ballonlar": 0,
    "yong_in_chiqish_soni": 0,

    # Nogironlar uchun
    "nogironlar_uchun_qulay": False,
    "pandus_soni": 0,
    "maxsus_hojatxona_soni": 0,

    # Morg
    "morg_mavjud": False,
    "morg_sig_imi": 0,

    # Kir yuvish
    "kir_yuvish_mavjud": False,
    "kir_yuvish_kg_kuniga": 0,

    # Oshxona
    "oshxona_mavjud": False,
    "ovqat_sig_imi_kuniga": 0,
    "dieta_ovqat": False,

    # Chiqindilar
    "chiqindi_boshqaruv_tizimi": False,
    "tibbiy_chiqindi_qayta_ishlash": False,
    "chiqindi_saralash": False,

    # IT infratuzilma
    "server_xonasi": False,
    "tarmoq_infratuzilmasi": False,
    "optik_tolali": False,

    # Kuzatuv
    "kamera_soni": 0,
    "24_soat_kuzatuv": False,

    # Xavfsizlik
    "qorovul_postlari": 0,
    "kirish_nazorat_tizimi": False,
    "kirim_chiqim_tizimi": False,
}


# =============================================================================
# 15. IT_RAQAMLASHTIRISH - IT va raqamlashtirish (45 parametr)
# =============================================================================

IT_RAQAMLASHTIRISH = {
    # HIS
    "his_mavjud": False,
    "his_nomi": "",
    "his_ishlab_chiqaruvchi": "",
    "his_joriy_etilgan_yil": 0,

    # EMR
    "emr_mavjud": False,
    "emr_qamrov_foiz": 0.0,
    "emr_nomi": "",

    # LIS
    "lis_mavjud": False,
    "lis_nomi": "",

    # RIS/PACS
    "ris_mavjud": False,
    "pacs_mavjud": False,
    "pacs_hajmi_tb": 0,

    # Dorixona
    "dorixona_tizimi": False,
    "dori_buyurtma_elektron": False,

    # Navbat
    "navbat_boshqaruv_tizimi": False,
    "navbat_tizimi_nomi": "",

    # Telemedicina
    "telemedicina_platformasi": False,
    "telemedicina_nomi": "",

    # Internet
    "internet_tezlik_mbps": 0,
    "wifi_qamrov_foiz": 0.0,
    "wifi_bemorlar_uchun": False,

    # Kompyuterlar
    "kompyuterlar_soni": 0,
    "shifokorga_kompyuter_nisbati": 0.0,
    "planshet_soni": 0,
    "printer_soni": 0,

    # Serverlar
    "serverlar_soni": 0,
    "data_markaz": False,
    "zaxira_tizimi": False,
    "bulutli_xizmat": False,

    # Xavfsizlik
    "kiberxavfsizlik_tizimi": False,
    "antiviruslar": False,
    "firewall": False,
    "shifrlash": False,
    "parol_siyosati": False,

    # Elektron xizmatlar
    "e_retsept": False,
    "onlayn_yozilish_tizimi": False,
    "bemor_portali": False,
    "mobil_ilova": False,

    # Video kuzatuv
    "video_kuzatuv_tizimi": False,
    "kamera_saqlash_kunlar": 0,

    # Qo'ng'iroq markazi
    "call_center": False,
    "ivr_tizimi": False,

    # Arxiv
    "raqamli_arxiv": False,
    "arxiv_hajmi_tb": 0,

    # AI/ML
    "ai_ml_vositalari": False,
    "ai_turlari": [],

    # Byudjet
    "yillik_it_byudjet": 0,
    "it_xodimlar_soni": 0,
}


# =============================================================================
# 16. XALQARO_HAMKORLIK - Xalqaro hamkorlik (30 parametr)
# =============================================================================

XALQARO_HAMKORLIK = {
    # Hamkorlar
    "xalqaro_hamkorlar_soni": 0,
    "xalqaro_hamkorlar_royxati": [],

    # Tashkilotlar bilan
    "who_loyihalari": [],
    "who_loyiha_soni": 0,
    "germaniya_texnik_yordam": False,
    "germaniya_jihozlar_royxati": [],
    "jica_loyihalari": [],
    "koica_loyihalari": [],
    "usaid_loyihalari": [],
    "boshqa_xalqaro_loyihalar": [],

    # Akkreditatsiya
    "jci_akkreditatsiya": False,
    "iso_sertifikatlar": [],
    "xalqaro_sertifikatlar": [],

    # Tibbiy turizm
    "tibbiy_turizm_bemorlar_yiliga": 0,
    "tibbiy_turizm_mamlakatlar": [],
    "tibbiy_turizm_daromad": 0,
    "tibbiy_turizm_xizmatlar": [],

    # Xorijda talim
    "xorijda_talim_olganlar": 0,
    "talim_mamlakatlar": [],
    "xorijiy_stipendiyalar": 0,

    # Telemedicina
    "xalqaro_telekonsultatsiya_soni": 0,
    "telekonsultatsiya_mamlakatlar": [],

    # Ilmiy hamkorlik
    "xalqaro_ilmiy_hamkorlik": [],
    "birgalikdagi_tadqiqotlar": 0,
    "xalqaro_konferensiyalar_tashkil_etilgan": 0,

    # Qo'shimcha
    "xalqaro_ko_ngillilar_soni": 0,
    "xalqaro_ekspertlar_tashrifi_yiliga": 0,
    "ikki_tomonlama_shartnomalar": 0,
}


# =============================================================================
# 17. TALIM_ILMFAN - Ta'lim va ilm-fan (45 parametr)
# =============================================================================

TALIM_ILMFAN = {
    # Ta'lim baza
    "talim_kasalxona_maqomi": False,
    "buxdti_bilan_aloqa": False,
    "buxdti_kafedra_soni": 0,
    "tibbiy_kollej_bilan_aloqa": False,

    # Rezidentura
    "rezidentura_dasturlari_soni": 0,
    "rezidentura_mutaxassisliklari": [],
    "rezidentlar_soni": 0,
    "rezidentura_bitirganlar_yiliga": 0,

    # Internlar
    "internlar_yiliga": 0,
    "intern_mutaxassisliklari": [],

    # Ilmiy tadqiqot
    "faol_tadqiqot_loyihalari": 0,
    "tadqiqot_mavzulari": [],
    "tadqiqot_byudjeti": 0,

    # Nashrlar
    "milliy_maqolalar_yiliga": 0,
    "xalqaro_maqolalar_yiliga": 0,
    "scopus_maqolalar_yiliga": 0,
    "web_of_science_maqolalar": 0,
    "monografiyalar": 0,
    "darsliklar": 0,
    "metodik_qollanmalar": 0,

    # Dissertatsiyalar
    "phd_himoya_yiliga": 0,
    "dsc_himoya_yiliga": 0,
    "davom_etayotgan_dissertatsiyalar": 0,

    # Konferensiyalar
    "tashkil_etilgan_konferensiyalar_yiliga": 0,
    "xalqaro_konferensiyalar": 0,
    "ishtirok_etilgan_konferensiyalar": 0,

    # Kutubxona
    "kutubxona_mavjud": False,
    "kitoblar_soni": 0,
    "elektron_kutubxona": False,
    "jurnallar_obunasi": 0,

    # Simulyatsiya
    "simulyatsiya_markazi": False,
    "simulyatsiya_jihozlar": [],
    "simulyatsiya_mashg_ulotlar_yiliga": 0,

    # Malaka oshirish
    "cme_soat_shifokorga": 0,
    "cme_dasturlari_soni": 0,
    "onlayn_talim_platformasi": False,

    # Talaba qoniqishi
    "talaba_qoniqish_ball": 0.0,
    "rezident_qoniqish_ball": 0.0,

    # Grantlar
    "ilmiy_grantlar_soni": 0,
    "grantlar_summasi": 0,
    "xalqaro_grantlar": 0,

    # Innovatsiya
    "innovatsiya_loyihalari": 0,
    "patentlar": 0,
    "ratsionalizatorlik_takliflari": 0,
}


# =============================================================================
# 18. BEMOR_QONIQISHI - Bemor qoniqishi (50 parametr)
# =============================================================================

BEMOR_QONIQISHI = {
    # Umumiy
    "umumiy_qoniqish_ball": 0.0,

    # Bo'lim bo'yicha
    "kardiologiya_qoniqish": 0.0,
    "nevrologiya_qoniqish": 0.0,
    "jarrohlik_qoniqish": 0.0,
    "terapiya_qoniqish": 0.0,
    "ginekologiya_qoniqish": 0.0,
    "travmatologiya_qoniqish": 0.0,
    "lor_qoniqish": 0.0,
    "oftalmologiya_qoniqish": 0.0,
    "reanimatsiya_qoniqish": 0.0,
    "poliklinika_qoniqish": 0.0,
    "laboratoriya_qoniqish": 0.0,

    # Mezonlar
    "kommunikatsiya_sifati_ball": 0.0,
    "shifokor_etiborlilik_ball": 0.0,
    "hamshira_parvarish_ball": 0.0,
    "tozalik_ball": 0.0,
    "ovqat_sifati_ball": 0.0,
    "kutish_vaqti_qoniqish": 0.0,
    "og_riq_boshqarish_ball": 0.0,
    "chiqarish_jarayoni_ball": 0.0,
    "axborot_berish_ball": 0.0,
    "maxfiylik_hurmat_ball": 0.0,
    "shikoyat_hal_etish_ball": 0.0,
    "yo_l_ko_rsatish_ball": 0.0,
    "qulaylik_ball": 0.0,

    # Tavsiya
    "tavsiya_etadi_foiz": 0.0,
    "nps_ball": 0,

    # Google/onlayn
    "google_reyting": 0.0,
    "google_sharh_soni": 0,
    "yandex_reyting": 0.0,
    "yandex_sharh_soni": 0,

    # So'rovnoma
    "sorovnoma_javob_foiz": 0.0,
    "sorovnoma_soni_yiliga": 0,

    # Shikoyatlar
    "shikoyat_soni_oyiga": 0,
    "yozma_shikoyatlar": 0,
    "og_zaki_shikoyatlar": 0,
    "onlayn_shikoyatlar": 0,
    "ishonch_telefoni_qongiroqlar": 0,

    # Shikoyat turlari
    "kutish_vaqti_shikoyat_foiz": 0.0,
    "xodim_munosabat_shikoyat_foiz": 0.0,
    "davolash_sifati_shikoyat_foiz": 0.0,
    "tozalik_shikoyat_foiz": 0.0,
    "ovqat_shikoyat_foiz": 0.0,
    "boshqa_shikoyat_foiz": 0.0,

    # Ijobiy fikrlar
    "ijobiy_fikrlar_soni_oyiga": 0,
    "minnatdorchilik_xatlari": 0,

    # Media
    "media_ijobiy_eslatmalar": 0,
    "media_salbiy_eslatmalar": 0,
    "ijtimoiy_tarmoq_eslatmalar": 0,
}


# =============================================================================
# 19. INFEKSIYA_NAZORATI - Infeksiya nazorati (40 parametr)
# =============================================================================

INFEKSIYA_NAZORATI = {
    # Tuzilma
    "infeksiya_nazorat_qomitasi": False,
    "infeksiya_nazorat_shifokor": "",
    "infeksiya_nazorat_hamshira_soni": 0,
    "infeksiya_nazorat_xodimlar": 0,

    # Ko'rsatkichlar
    "kasalxona_infeksiya_foiz": 0.0,
    "jarrohlik_yara_infeksiya_foiz": 0.0,
    "mrsa_foiz": 0.0,
    "clostridium_difficile_foiz": 0.0,
    "esbl_foiz": 0.0,
    "vre_foiz": 0.0,

    # Gigiena
    "qol_gigiena_muvofiqlik_foiz": 0.0,
    "qol_antiseptik_sarfi_litr_oyiga": 0,
    "shaxsiy_himoya_muvofiqlik_foiz": 0.0,
    "sterilizatsiya_muvofiqlik_foiz": 0.0,

    # Muhit
    "havo_sifati_monitoring": False,
    "suv_sifati_tekshiruv": False,
    "sirt_dezinfeksiya_jadval": False,
    "dezinfeksiya_vositalari_sarfi": 0,

    # Decontaminatsiya
    "dezinfeksiya_protokollar": False,
    "avtoklav_nazorat": False,
    "sterilizatsiya_indikatorlar": False,

    # Izolyatsiya
    "izolyatsiya_xonalar_soni": 0,
    "manfiy_bosim_xonalar": 0,
    "izolyatsiya_protokollari": False,

    # Antibiogramma
    "antibiogramma_mavjud": False,
    "antibiotik_rezistentlik_monitoring": False,
    "antibiotik_stewardship": False,

    # Epidemiyalar
    "epidemiya_holatlari_yiliga": 0,
    "karantin_kunlari_yiliga": 0,

    # COVID-19
    "covid_tayorgarlik_ball": 0,
    "covid_izolyatsiya_xonalar": 0,

    # Skrining
    "tuberkuloz_skrining": False,
    "gepatit_skrining": False,
    "oiv_skrining": False,

    # Chiqindilar
    "tibbiy_chiqindi_saralash_muvofiqlik": 0.0,
    "o_tkir_chiqindi_boshqarish": False,

    # Xodimlar xavfsizligi
    "igna_jarohatlari_yiliga": 0,
    "xodimlar_emlash_foiz": 0.0,
    "infeksiya_nazorat_talim_soat": 0,

    # Qo'shimcha
    "infeksiya_nazorat_byudjeti": 0,
    "tashqi_audit_yiliga": 0,
}


# =============================================================================
# 20. QON_BANKI - Qon banki (25 parametr)
# =============================================================================

QON_BANKI = {
    # Umumiy
    "qon_banki_mavjud": False,
    "qon_banki_turi": "",  # stansiya / bo'lim
    "xodimlar_soni": 0,
    "shifokorlar_soni": 0,

    # To'plash
    "yillik_qon_toplash_birlik": 0,
    "donorlar_bazasi_soni": 0,
    "ko_ngilli_donorlar": 0,
    "doimiy_donorlar": 0,

    # Komponentlar
    "eritrotsit_massa_tayyorlash": 0,
    "plazma_tayyorlash": 0,
    "trombosit_tayyorlash": 0,
    "kriopresipitat_tayyorlash": 0,

    # Foydalanish
    "yillik_qon_foydalanish": 0,
    "kross_match_quyish_nisbati": 0.0,
    "qon_quyish_reaktsiyalar": 0,
    "noto_gri_qon_quyish": 0,

    # Taqchillik
    "qon_taqchillik_chastotasi_oyiga": 0,
    "zaxira_kunlar": 0,

    # Skrining
    "oiv_skrining": False,
    "gepatit_b_skrining": False,
    "gepatit_c_skrining": False,
    "zaxm_skrining": False,

    # Saqlash
    "sovuq_zanjir_muvofiqlik": False,
    "qon_saqlash_muzlatgichlar": 0,

    # Shoshilinch
    "shoshilinch_qon_ta_minot_protokoli": False,
    "autotransfuziya_imkoniyati": False,

    # Jihozlar
    "tsentrifuga_soni": 0,
    "separator_soni": 0,
}


# =============================================================================
# 21. REANIMATSIYA_INTENSIV - Reanimatsiya va intensiv terapiya (40 parametr)
# =============================================================================

REANIMATSIYA_INTENSIV = {
    # Karavotlar
    "rit_karavotlar_jami": 0,
    "umumiy_rit_karavotlar": 0,
    "kardiologik_rit_karavotlar": 0,
    "jarrohlik_rit_karavotlar": 0,
    "neonatal_rit_karavotlar": 0,

    # Xodimlar
    "rit_shifokorlar": 0,
    "rit_hamshiralar": 0,
    "hamshira_bemor_nisbati": "",
    "rit_texniklar": 0,

    # Jihozlar
    "sun_iy_nafas_apparatlari": 0,
    "monitorlar": 0,
    "infuzion_nasoslar": 0,
    "defibrillyatorlar": 0,
    "intraaortal_ballon_nasos": 0,

    # Statistika
    "rit_yotqizilganlar_yiliga": 0,
    "rit_ortacha_yotish_kun": 0.0,
    "rit_o_lim_foiz": 0.0,
    "rit_qayta_yotqizish_foiz": 0.0,

    # Ko'rsatkichlar
    "sun_iy_nafas_kunlari_1000_bemorga": 0.0,
    "apache_ortacha_ball": 0.0,
    "sofa_ortacha_ball": 0.0,
    "markaziy_kateter_kunlar": 0,
    "siydik_kateter_kunlar": 0,

    # Jamoalar
    "tez_javob_jamoasi": False,
    "code_blue_oyiga": 0,
    "reanimatsiya_muvaffaqiyat_foiz": 0.0,

    # Protokollar
    "sedatsiya_protokoli": False,
    "ovqatlantirish_protokoli": False,
    "erta_mobilizatsiya_protokoli": False,
    "og_riq_boshqarish_protokoli": False,

    # Oilaviy tashrif
    "oila_tashrif_siyosati": "",
    "oila_tashrif_soatlari": "",

    # Qo'shimcha
    "rit_bemor_qoniqish": 0.0,
    "sepsis_protokoli": False,
    "antikoagulyant_protokoli": False,
    "qon_glyukoza_protokoli": False,
    "rit_infeksiya_foiz": 0.0,
    "rit_byudjeti": 0,
    "ecmo_imkoniyati": False,
    "hemodializ_rit_da": False,
}


# =============================================================================
# 22. REABILITATSIYA - Reabilitatsiya xizmati (30 parametr)
# =============================================================================

REABILITATSIYA = {
    # Umumiy
    "reabilitatsiya_bolimi_mavjud": False,
    "reabilitatsiya_karavotlar": 0,

    # Turlari
    "fizioterapiya": False,
    "mehnat_terapiyasi": False,
    "nutq_terapiyasi": False,
    "kardioreabilitatsiya": False,
    "neyro_reabilitatsiya": False,
    "ortopedik_reabilitatsiya": False,
    "pulmonar_reabilitatsiya": False,

    # Xodimlar
    "fiziatrlar_soni": 0,
    "fizioterapevtlar_soni": 0,
    "mehnat_terapevtlari_soni": 0,
    "logopedlar_soni": 0,
    "psixologlar_soni": 0,
    "massajchilar_soni": 0,

    # Jihozlar
    "sport_zal": False,
    "basseyn": False,
    "elektroterapiya_jihozlari": 0,
    "utt_terapiya_jihozlari": 0,
    "lazer_terapiya": False,
    "magnit_terapiya": False,

    # Statistika
    "bemorlar_yiliga": 0,
    "ortacha_davomiylik_kun": 0,
    "funktsional_yaxshilanish_foiz": 0.0,
    "ishga_qaytish_foiz": 0.0,

    # Dasturlar
    "uyda_reabilitatsiya": False,
    "telemedicina_reabilitatsiya": False,
    "guruh_mashg_ulotlari": False,

    # Byudjet
    "reabilitatsiya_byudjeti": 0,
}


# =============================================================================
# 23. INSON_RESURSLARI - Inson resurslari boshqaruvi (50 parametr)
# =============================================================================

INSON_RESURSLARI = {
    # HR bo'limi
    "hr_bolimi_mavjud": False,
    "hr_xodimlar_soni": 0,

    # Yollash
    "vakansiyalar_soni": 0,
    "vakansiya_toldirish_vaqti_kun": 0,
    "yollash_manbalari": [],
    "yollash_xarajati": 0,

    # Adaptatsiya
    "adaptatsiya_davomiyligi_kun": 0,
    "mentor_tizimi": False,

    # Saqlash
    "xodimlar_saqlash_foiz": 0.0,
    "1_yil_ichida_ketganlar_foiz": 0.0,

    # Kadrlar almashinuvi
    "shifokor_almashinuvi_foiz": 0.0,
    "hamshira_almashinuvi_foiz": 0.0,
    "ma_muriy_almashinuvi_foiz": 0.0,
    "texnik_almashinuvi_foiz": 0.0,

    # Baholash
    "ish_baholash_tizimi": False,
    "baholash_chastotasi": "",
    "kpi_tizimi": False,
    "360_daraja_baholash": False,

    # Mansab
    "mansab_ko_tarish_mezonlari": "",
    "mansab_ko_tarilganlar_yiliga": 0,

    # Intizom
    "intizomiy_jazolar_yiliga": 0,
    "ogohlantirishlar": 0,
    "ishdan_bo_shatilganlar": 0,

    # Shikoyatlar
    "xodim_shikoyatlari_yiliga": 0,
    "shikoyat_hal_etish_vaqti_kun": 0,

    # Mehnat xavfsizligi
    "ish_joyidagi_hodisalar": 0,
    "kasbiy_kasalliklar": 0,
    "tibbiy_tekshiruv_foiz": 0.0,

    # Salomatlik
    "xodimlar_salomatlik_tekshiruv": False,
    "ruhiy_salomatlik_dasturi": False,
    "psixologik_yordam": False,
    "stress_boshqarish_dasturi": False,

    # Ish-hayot balansi
    "moslashuvchan_grafik": False,
    "masofaviy_ish": False,

    # Turdik imtiyozlar
    "turar_joy_yotoqxona": False,
    "turar_joy_o_rinlar": 0,
    "transport_xizmati": False,
    "bolalar_bog_chasi": False,
    "ovqatlanish_subsidiya": False,

    # Pensiya
    "pensiya_imtiyozlari": False,
    "qo_shimcha_sug_urta": False,

    # Kasaba uyushmasi
    "kasaba_uyushmasi_azolari": 0,
    "kasaba_uyushmasi_foiz": 0.0,

    # Tadbirlar
    "xodimlar_tadbirlari_yiliga": 0,
    "sport_musobaqalar": 0,
    "jamoa_qurilish_tadbirlari": 0,

    # Qo'shimcha
    "xodimlar_ma_lumotlar_bazasi": False,
    "elektron_hujjat_oboroti": False,
}


# =============================================================================
# 24. XAVFSIZLIK - Xavfsizlik (35 parametr)
# =============================================================================

XAVFSIZLIK = {
    # Qo'riqlash
    "xavfsizlik_xizmati": False,
    "qorovullar_soni": 0,
    "24_soat_qorovul": False,

    # Kuzatuv
    "cctv_kameralar": 0,
    "24_soat_monitoring": False,
    "video_saqlash_kunlar": 0,

    # Kirish nazorati
    "kirish_nazorat_turi": "",
    "karta_tizimi": False,
    "biometrik_tizim": False,
    "tashrif_buyuruvchi_hisobi": False,

    # Yong'in xavfsizligi
    "yong_in_signalizatsiya": False,
    "sprinkler_tizimi": False,
    "yong_in_o_chirish_ballonlar": 0,
    "yong_in_mashqlari_yiliga": 0,
    "yong_in_chiqish_yo_llari": 0,

    # Zilzila
    "zilzila_tayorgarlik": False,
    "bino_seysmik_darajasi": 0,

    # Evakuatsiya
    "shoshilinch_evakuatsiya_rejasi": False,
    "evakuatsiya_mashqlari_yiliga": 0,
    "evakuatsiya_xaritalar": False,

    # Xavfli moddalar
    "xavfli_moddalar_ombori": False,
    "kimyoviy_xavfsizlik": False,

    # Radiatsiya
    "radiatsiya_xavfsizlik_xodimi": False,
    "radiatsiya_monitoring": False,
    "dozimetriya": False,

    # Bemor xavfsizligi
    "bemor_xavfsizlik_qomitasi": False,
    "hodisa_hisoboti_tizimi": False,
    "ildiz_sabab_tahlili": False,
    "sentinel_hodisalar_yiliga": 0,

    # Deyarli sodir bo'lgan
    "deyarli_sodir_hodisalar": 0,
    "hodisa_hisoboti_madaniyati_ball": 0.0,

    # Xavfsizlik madaniyati
    "xavfsizlik_madaniyat_sorov_ball": 0.0,
    "xavfsizlik_talim_soat_yiliga": 0,
    "xavfsizlik_byudjeti": 0,

    # Qo'shimcha
    "terrorizm_tayorgarlik": False,
    "kiberxavfsizlik_hodisalar": 0,
}


# =============================================================================
# 25. EKOLOGIYA - Ekologiya va atrof-muhit (30 parametr)
# =============================================================================

EKOLOGIYA = {
    # Tibbiy chiqindilar
    "tibbiy_chiqindi_kg_kuniga": 0.0,
    "maishiy_chiqindi_kg_kuniga": 0.0,
    "saralash_tizimi": False,
    "rang_kodli_saralash": False,

    # O'tkir chiqindilar
    "o_tkir_chiqindi_boshqarish": False,
    "igna_konteynerlar_soni": 0,

    # Farmatsevtik chiqindilar
    "dori_chiqindi_utilizatsiya": False,
    "muddati_otgan_dori_kg_yiliga": 0,

    # Radioaktiv chiqindilar
    "radioaktiv_chiqindi": False,
    "radioaktiv_utilizatsiya": "",

    # Qayta ishlash
    "avtoklav_utilizatsiya": False,
    "insinerator_mavjud": False,
    "kimyoviy_dezinfeksiya": False,
    "utilizatsiya_tashkilot": "",

    # Oqova suvlar
    "oqova_suv_tozalash": False,
    "oqova_suv_tekshiruv": False,

    # Energiya
    "elektr_sarfi_kvt_oyiga": 0,
    "gaz_sarfi_m3_oyiga": 0,
    "energiya_tejash_dasturi": False,

    # Suv
    "suv_sarfi_m3_oyiga": 0,
    "suv_tejash_dasturi": False,

    # Yashil energiya
    "quyosh_panellari": False,
    "quyosh_panel_kvt": 0,

    # Sertifikatlar
    "yashil_bino_sertifikat": False,
    "ekologik_audit_chastotasi": "",

    # Uglerod izi
    "uglerod_izi_baholash": False,
    "uglerod_izi_tonna_yiliga": 0.0,

    # Qo'shimcha
    "daraxt_ekilgan_yiliga": 0,
    "ekologik_byudjet": 0,
    "chiqindi_litsenziyali_tashuvchi": False,
}


# =============================================================================
# 26. RAQOBATCHILAR - Raqobatchilar tahlili (ro'yxat)
# =============================================================================

def _raqobatchi_shablon():
    """Har bir raqobatchi uchun default shablon"""
    return {
        "nomi": "",
        "turi": "",  # respublika / viloyat / tuman / xususiy
        "manzili": "",
        "shahar": "",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",  # past / o'rta / yuqori
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    }


RAQOBATCHILAR = [
    # 1. Toshkent Respublika ixtisoslashtirilgan kardiologiya markazi
    {
        "nomi": "Toshkent Respublika ixtisoslashtirilgan kardiologiya markazi",
        "turi": "respublika",
        "manzili": "",
        "shahar": "Toshkent",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
    # 2. Toshkent Respublika ko'p tarmoqli tibbiy markazi
    {
        "nomi": "Toshkent Respublika ko'p tarmoqli tibbiy markazi",
        "turi": "respublika",
        "manzili": "",
        "shahar": "Toshkent",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
    # 3. Samarqand viloyat ko'p tarmoqli tibbiy markazi
    {
        "nomi": "Samarqand viloyat ko'p tarmoqli tibbiy markazi",
        "turi": "viloyat",
        "manzili": "",
        "shahar": "Samarqand",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
    # 4. SofiMed klinikasi (Buxoro xususiy)
    {
        "nomi": "SofiMed klinikasi",
        "turi": "xususiy",
        "manzili": "",
        "shahar": "Buxoro",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
    # 5. Buxoro bolalar ko'p tarmoqli tibbiy markazi
    {
        "nomi": "Buxoro bolalar ko'p tarmoqli tibbiy markazi",
        "turi": "viloyat",
        "manzili": "",
        "shahar": "Buxoro",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
    # 6. Buxoro tuman tibbiy birlashmalari (DTB)
    {
        "nomi": "Buxoro tuman tibbiy birlashmalari",
        "turi": "tuman",
        "manzili": "",
        "shahar": "Buxoro viloyati",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
    # 7. Buxoro shahar xususiy klinikalari (boshqalar)
    {
        "nomi": "Buxoro shahar xususiy klinikalari (boshqalar)",
        "turi": "xususiy",
        "manzili": "",
        "shahar": "Buxoro",
        "karavotlar_soni": 0,
        "shifokorlar_soni": 0,
        "mutaxassisliklar_soni": 0,
        "mutaxassisliklar_royxati": [],
        "kt_mavjud": False,
        "mrt_mavjud": False,
        "laparoskopiya": False,
        "endoskopiya": False,
        "dializ": False,
        "narxlar_darajasi": "",
        "reyting": 0.0,
        "sharh_soni": 0,
        "bemor_oqimi_bvktm_dan": 0,
        "afzalliklari": [],
        "kamchiliklari": [],
        "bozor_ulushi_taxmin_foiz": 0.0,
        "yillik_bemorlar": 0,
        "yillik_operatsiyalar": 0,
        "pullik_xizmatlar": False,
        "sugurta_bilan_ishlaydi": False,
        "veb_sayt": "",
        "telefon": "",
        "mashhur_shifokorlar": [],
        "yuqori_texnologik_jihozlar": [],
        "jarrohlik_turlari": [],
        "tez_yordam_xizmati": False,
        "24_soat_xizmat": False,
        "tibbiy_turizm": False,
        "qurulish_yangilanish": "",
        "xalqaro_hamkorlik": False,
        "ilmiy_faoliyat": False,
        "ta_lim_baza": False,
        "kuchli_bolimlar": [],
        "zaif_bolimlar": [],
        "strategik_rejalar": "",
        "asosiy_xavf": "",
        "asosiy_imkoniyat": "",
        "bemor_segmenti": "",
        "masofa_bvktm_dan_km": 0.0,
        "oxirgi_yangilanish_yili": 0,
    },
]


# =============================================================================
# 27. HUDUDIY_SALOMATLIK - Hududiy salomatlik ko'rsatkichlari (55 parametr)
# =============================================================================

HUDUDIY_SALOMATLIK = {
    # Aholi
    "buxoro_viloyat_aholisi": 0,
    "buxoro_shahar_aholisi": 0,
    "g_ijduvon_tumani": 0,
    "kogon_shahar": 0,
    "olot_tumani": 0,
    "peshku_tumani": 0,
    "romitan_tumani": 0,
    "shofirkon_tumani": 0,
    "vobkent_tumani": 0,
    "jondor_tumani": 0,
    "qorako_l_tumani": 0,
    "qorovulbozor_tumani": 0,

    # Yosh tarkibi
    "yosh_0_14_foiz": 0.0,
    "yosh_15_24_foiz": 0.0,
    "yosh_25_44_foiz": 0.0,
    "yosh_45_64_foiz": 0.0,
    "yosh_65_plus_foiz": 0.0,

    # Demografiya
    "tugulish_koeffitsienti": 0.0,
    "olim_koeffitsienti": 0.0,
    "umr_kutish_davri": 0.0,
    "umr_kutish_erkak": 0.0,
    "umr_kutish_ayol": 0.0,

    # O'lim sabablari - Top 10
    "olim_sabab_1_yurak_qon_tomir": 0.0,
    "olim_sabab_2_onkologiya": 0.0,
    "olim_sabab_3_nafas_kasalliklari": 0.0,
    "olim_sabab_4_jarohalar": 0.0,
    "olim_sabab_5_oshqozon_ichak": 0.0,
    "olim_sabab_6_infeksion": 0.0,
    "olim_sabab_7_endokrin": 0.0,
    "olim_sabab_8_siydik_buyrak": 0.0,
    "olim_sabab_9_asab_tizimi": 0.0,
    "olim_sabab_10_boshqalar": 0.0,

    # Nogironlik sabablari - Top 10
    "nogironlik_sabab_1": "",
    "nogironlik_sabab_2": "",
    "nogironlik_sabab_3": "",
    "nogironlik_sabab_4": "",
    "nogironlik_sabab_5": "",

    # Surunkali kasalliklar tarqalishi
    "diabet_tarqalish_foiz": 0.0,
    "gipertoniya_tarqalish_foiz": 0.0,
    "saraton_tarqalish_10000": 0.0,
    "tuberkuloz_tarqalish_100000": 0.0,
    "oiv_tarqalish_100000": 0.0,
    "bronxial_astma_tarqalish_foiz": 0.0,
    "surunkali_buyrak_kasalligi_foiz": 0.0,

    # Ona va bola
    "ona_olimi_100000": 0.0,
    "chaqaloq_olimi_1000": 0.0,
    "5_yosh_gacha_olim_1000": 0.0,

    # Emlash
    "emlash_qamrov_foiz": 0.0,

    # Resurslar
    "10000_aholiga_karavot": 0.0,
    "10000_aholiga_shifokor": 0.0,
    "10000_aholiga_hamshira": 0.0,

    # Moliya
    "jon_boshiga_sogliq_xarajati": 0,
    "sugurta_qamrov_foiz": 0.0,

    # Geografik qulaylik
    "eng_yaqin_kasalxona_masofa_max_km": 0.0,
    "eng_yaqin_kasalxona_masofa_ortacha_km": 0.0,
}


# =============================================================================
# 28. DAVLAT_DASTURLARI - Davlat dasturlari (35 parametr)
# =============================================================================

DAVLAT_DASTURLARI = {
    # DSTI
    "dsti_ishtirok": False,
    "dsti_yillik_tolovlar": 0,
    "dsti_shartnoma_raqami": "",
    "dsti_xizmatlar_royxati": [],

    # Bepul yordam
    "bepul_yordam_kvotasi": 0,
    "bepul_yordam_haqiqiy": 0,
    "bepul_operatsiyalar_kvota": 0,
    "bepul_diagnostika_kvota": 0,

    # Pullik xizmatlar
    "pullik_xizmatlar_litsenziya": False,
    "pullik_xizmatlar_narxnoma": False,

    # Davlat dasturlari
    "modernizatsiya_dasturi": False,
    "modernizatsiya_tafsilotlari": "",
    "ppp_loyihalari": [],
    "ppp_loyihalar_soni": 0,

    # Prezident qarorlari
    "prezident_qarori_muvofiqlik": False,
    "2027_kpi_tizimi_tayorlik": False,
    "2027_kpi_hozirgi_ball": 0.0,

    # Skrining dasturlari
    "skrining_dasturlari_ishtirok": [],
    "saraton_skrining": False,
    "diabet_skrining": False,
    "yurak_skrining": False,

    # Milliy dasturlar
    "milliy_emlash_dasturi": False,
    "tuberkuloz_dots_dasturi": False,
    "oiv_oits_dasturi": False,
    "ona_bola_salomatligi_dasturi": False,
    "yuqumli_bo_lmagan_kasalliklar_dasturi": False,
    "shoshilinch_tibbiy_yordam_dasturi": False,

    # Boshqalar
    "elektron_sogliq_dasturi": False,
    "telemedicina_davlat_dasturi": False,
    "tibbiy_kadrlar_dasturi": False,
    "dori_ta_minot_dasturi": False,
    "tibbiy_jihozlar_yangilash_dasturi": False,
    "raqamli_transformatsiya_dasturi": False,

    # Qo'shimcha
    "inspeksiya_natijalari": "",
    "davlat_buyurtmalari_hajmi": 0,
}


# =============================================================================
# 29. TELEMEDICINA - Telemedicina xizmatlari (25 parametr)
# =============================================================================

TELEMEDICINA = {
    # Umumiy
    "telemedicina_xizmati_mavjud": False,
    "platforma_turi": "",
    "platforma_nomi": "",
    "boshlangan_yil": 0,

    # Konsultatsiyalar
    "konsultatsiyalar_oyiga": 0,
    "konsultatsiyalar_yiliga": 0,
    "mutaxassisliklar_mavjud": [],
    "eng_ko_p_so_ralgan_mutaxassislik": "",

    # Qamrov
    "qishloq_hududlar_qamrovi": False,
    "qamrov_tumanlar_soni": 0,
    "masofaviy_monitoring": False,

    # Jihozlar
    "kameralar_soni": 0,
    "ekranlar_soni": 0,
    "diagnostik_qurilmalar": [],
    "mobil_telemedicina_punkti": 0,

    # Integratsiya
    "his_bilan_integratsiya": False,
    "elektron_retsept": False,

    # Qoniqish
    "bemor_qoniqish_ball": 0.0,
    "shifokor_qoniqish_ball": 0.0,

    # Moliya
    "xarajat_tejash_taxmin": 0,
    "telemedicina_byudjeti": 0,

    # Regulyativ
    "regulyativ_muvofiqlik": False,
    "ma_lumot_xavfsizligi": False,

    # Xodimlar
    "talim_olgan_xodimlar_soni": 0,
    "internet_talabi_mbps": 0,

    # Xalqaro
    "xalqaro_telekonsultatsiya": False,
    "xalqaro_konsultatsiya_soni": 0,

    # Ikkinchi fikr
    "ikkinchi_fikr_xizmati": False,
}


# =============================================================================
# 30. KELAJAK_REJALARI - Kelajak rejalari (30 parametr)
# =============================================================================

KELAJAK_REJALARI = {
    # Qisqa muddatli (1 yil)
    "qisqa_muddat_rejalar": [],
    "qisqa_muddat_byudjet": 0,
    "qisqa_muddat_ustuvorliklar": [],

    # O'rta muddatli (3 yil)
    "orta_muddat_rejalar": [],
    "orta_muddat_byudjet": 0,
    "orta_muddat_ustuvorliklar": [],

    # Uzoq muddatli (5-10 yil)
    "uzoq_muddat_rejalar": [],
    "uzoq_muddat_byudjet": 0,
    "uzoq_muddat_vizyon": "",

    # Yangi bo'limlar
    "yangi_bolimlar_rejasi": [],
    "yangi_bolimlar_byudjet": 0,

    # Yangi jihozlar
    "yangi_jihozlar_rejasi": [],
    "yangi_jihozlar_byudjet": 0,

    # Qurilish
    "qurilish_remont_rejasi": [],
    "qurilish_byudjet": 0,
    "yangi_bino_rejasi": False,

    # Xodimlar
    "xodimlar_kengaytirish": [],
    "yangi_mutaxassisliklar": [],

    # Yangi xizmatlar
    "yangi_xizmatlar_texnologiyalar": [],
    "robot_jarrohlik_rejasi": False,
    "transplantatsiya_rejasi": False,

    # Raqamlashtirish
    "raqamli_transformatsiya_xarita": "",
    "ai_joriy_etish_rejasi": [],

    # Sifat
    "sifat_yaxshilash_maqsadlar": [],
    "maqsad_kpi_2027": {},

    # Moliya
    "moliyaviy_maqsadlar": [],
    "daromad_oshirish_strategiyasi": "",

    # Xalqaro
    "xalqaro_akkreditatsiya_rejasi": False,
    "xalqaro_hamkorlik_rejasi": [],

    # Ilmiy
    "ilmiy_rivojlanish_rejasi": [],
    "scopus_maqola_maqsad": 0,

    # Jamiyat
    "jamoatchilik_dasturlari": [],
    "profilaktika_dasturlari": [],

    # Barqarorlik
    "barqarorlik_rejasi": "",
    "yashil_kasalxona_maqsad": False,
}


# =============================================================================
# 31. QONUNCHILIK - Qonunchilik va regulyativ (25 parametr)
# =============================================================================

QONUNCHILIK = {
    # Litsenziya
    "litsenziya_amal_qiladi": False,
    "litsenziya_muddati": "",
    "litsenziya_raqami": "",

    # Akkreditatsiya
    "akkreditatsiya_holati": "",
    "akkreditatsiya_muddati": "",
    "akkreditatsiya_darajasi": "",

    # Maxsus litsenziyalar
    "narkotik_dorilar_litsenziya": False,
    "radiatsiya_xavfsizlik_litsenziya": False,
    "tibbiy_faoliyat_litsenziya": False,

    # Ruxsatnomalar
    "qurilish_ruxsatnomalar": False,
    "ekologik_muvofiqlik": False,
    "yong_in_xavfsizlik_sertifikat": False,
    "sanitariya_epidemiologik_xulosa": False,

    # Soliq
    "soliq_rejimi": "",
    "soliq_imtiyozlari": False,

    # Audit
    "oxirgi_audit_sanasi": "",
    "audit_natijalari": "",
    "tekshiruvlar_yiliga": 0,

    # Jazolar
    "jarimalar_tarixi": [],
    "jarima_summasi_yiliga": 0,

    # Tibbiy xato
    "tibbiy_xato_davolari_soni": 0,
    "kompensatsiya_tolangan": 0,

    # Ma'lumotlar himoyasi
    "bemor_malumot_himoyasi": False,
    "malumot_himoya_siyosati": False,
    "gdpr_muvofiqlik": False,

    # Protokollar
    "klinik_protokol_muvofiqlik_foiz": 0.0,
    "milliy_standart_muvofiqlik": False,
}


# =============================================================================
# 32. SIMULYATSIYA_MAQSADLARI - Simulyatsiya maqsadlari (35 parametr)
# =============================================================================

SIMULYATSIYA_MAQSADLARI = {
    # Optimallashtirish maqsadlari (og'irliklar bilan)
    "maqsad_bemor_qoniqish_vazn": 0.0,
    "maqsad_olim_kamaytirish_vazn": 0.0,
    "maqsad_kutish_vaqti_vazn": 0.0,
    "maqsad_karavot_bandlik_vazn": 0.0,
    "maqsad_moliyaviy_samaradorlik_vazn": 0.0,
    "maqsad_xodim_qoniqish_vazn": 0.0,
    "maqsad_infeksiya_kamaytirish_vazn": 0.0,
    "maqsad_sifat_oshirish_vazn": 0.0,

    # Cheklovlar
    "cheklov_byudjet_max": 0,
    "cheklov_karavot_max": 0,
    "cheklov_xodim_max": 0,
    "cheklov_maydon_max_m2": 0.0,
    "cheklov_regulyativ": [],
    "cheklov_jihozlar_byudjet": 0,
    "cheklov_maosh_fondi_max": 0,

    # Stsenariylar
    "stsenariy_optimistik": {
        "byudjet_oshish_foiz": 0.0,
        "bemor_oshish_foiz": 0.0,
        "xodim_oshish_foiz": 0.0,
        "yangi_jihozlar": [],
        "yangi_bolimlar": [],
    },
    "stsenariy_pessimistik": {
        "byudjet_qisqarish_foiz": 0.0,
        "bemor_kamayish_foiz": 0.0,
        "xodim_kamayish_foiz": 0.0,
        "jihozlar_eskirish": [],
        "xavflar": [],
    },
    "stsenariy_bazaviy": {
        "byudjet_o_zgarish_foiz": 0.0,
        "bemor_o_zgarish_foiz": 0.0,
        "xodim_o_zgarish_foiz": 0.0,
        "joriy_tendensiyalar": [],
    },

    # 2027 maqsadli KPI'lar
    "kpi_2027_olim_foiz": 0.0,
    "kpi_2027_infeksiya_foiz": 0.0,
    "kpi_2027_bemor_qoniqish": 0.0,
    "kpi_2027_karavot_bandlik": 0.0,
    "kpi_2027_ortacha_yotish_kun": 0.0,
    "kpi_2027_kutish_vaqti_daqiqa": 0,
    "kpi_2027_jarrohlik_soni": 0,
    "kpi_2027_ambulator_tashriflar": 0,
    "kpi_2027_daromad": 0,
    "kpi_2027_xodimlar_soni": 0,
    "kpi_2027_scopus_maqolalar": 0,
    "kpi_2027_xalqaro_akkreditatsiya": False,
    "kpi_2027_raqamlashtirish_foiz": 0.0,
    "kpi_2027_telemedicina_konsultatsiya": 0,
    "kpi_2027_energiya_tejash_foiz": 0.0,
}


# =============================================================================
# BARCHA_BOLIMLAR - Barcha bo'limlarni birlashtiruvchi lug'at
# =============================================================================

BARCHA_BOLIMLAR = {
    "markaz_profili": MARKAZ_PROFILI,
    "bolimlar": BOLIMLAR,
    "kadrlar": KADRLAR,
    "tibbiy_jihozlar": TIBBIY_JIHOZLAR,
    "toshak_fondi": TOSHAK_FONDI,
    "poliklinika": POLIKLINIKA,
    "jarrohlik": JARROHLIK,
    "diagnostika": DIAGNOSTIKA,
    "dori_darmon": DORI_DARMON,
    "moliya": MOLIYA,
    "bemorlar_statistikasi": BEMORLAR_STATISTIKASI,
    "sifat_korsatkichlari": SIFAT_KORSATKICHLARI,
    "shoshilinch_yordam": SHOSHILINCH_YORDAM,
    "infratuzilma": INFRATUZILMA,
    "it_raqamlashtirish": IT_RAQAMLASHTIRISH,
    "xalqaro_hamkorlik": XALQARO_HAMKORLIK,
    "talim_ilmfan": TALIM_ILMFAN,
    "bemor_qoniqishi": BEMOR_QONIQISHI,
    "infeksiya_nazorati": INFEKSIYA_NAZORATI,
    "qon_banki": QON_BANKI,
    "reanimatsiya_intensiv": REANIMATSIYA_INTENSIV,
    "reabilitatsiya": REABILITATSIYA,
    "inson_resurslari": INSON_RESURSLARI,
    "xavfsizlik": XAVFSIZLIK,
    "ekologiya": EKOLOGIYA,
    "raqobatchilar": RAQOBATCHILAR,
    "hududiy_salomatlik": HUDUDIY_SALOMATLIK,
    "davlat_dasturlari": DAVLAT_DASTURLARI,
    "telemedicina": TELEMEDICINA,
    "kelajak_rejalari": KELAJAK_REJALARI,
    "qonunchilik": QONUNCHILIK,
    "simulyatsiya_maqsadlari": SIMULYATSIYA_MAQSADLARI,
}


# =============================================================================
# Yordamchi funksiyalar
# =============================================================================

def parametrlar_sonini_hisoblash():
    """Barcha parametrlarni rekursiv hisoblash"""
    count = 0

    def _count_dict(d):
        nonlocal count
        for k, v in d.items():
            if isinstance(v, dict):
                _count_dict(v)
            elif isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                for item in v:
                    _count_dict(item)
            else:
                count += 1

    for section_name, section_data in BARCHA_BOLIMLAR.items():
        if isinstance(section_data, dict):
            _count_dict(section_data)
        elif isinstance(section_data, list):
            for item in section_data:
                if isinstance(item, dict):
                    _count_dict(item)

    return count


def bolim_nomlari():
    """Barcha bo'lim nomlarini qaytaradi"""
    return list(BARCHA_BOLIMLAR.keys())


def bolim_olish(nom):
    """Berilgan nom bo'yicha bo'limni qaytaradi"""
    return BARCHA_BOLIMLAR.get(nom, None)


if __name__ == "__main__":
    print(f"BVKTM Data Schema")
    print(f"Bo'limlar soni: {len(BARCHA_BOLIMLAR)}")
    print(f"Jami parametrlar: {parametrlar_sonini_hisoblash()}")
    print(f"\nBo'limlar:")
    for i, nom in enumerate(bolim_nomlari(), 1):
        data = BARCHA_BOLIMLAR[nom]
        if isinstance(data, dict):
            print(f"  {i}. {nom}: {len(data)} parametr")
        elif isinstance(data, list):
            print(f"  {i}. {nom}: {len(data)} element")
