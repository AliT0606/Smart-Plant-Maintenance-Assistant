import random

# Kendi yerel bitki kütüphanemiz (İnternet bağlantısı veya API Key gerektirmez):
MOCK_BITKILER = {
    "monstera": {"sulama": "Average", "periyot": 7, "isik": "Part shade, Indirect sunlight"},
    "spathiphyllum": {"sulama": "Frequent", "periyot": 4, "isik": "Part shade"},
    "sansevieria": {"sulama": "Minimum", "periyot": 14, "isik": "Full sun, Part shade"},
    "aloe vera": {"sulama": "Minimum", "periyot": 14, "isik": "Full sun"},
    "pothos": {"sulama": "Average", "periyot": 7, "isik": "Part shade"},
    "chlorophytum": {"sulama": "Average", "periyot": 7, "isik": "Part shade"},
    "rose": {"sulama": "Average", "periyot": 5, "isik": "Full sun"}
}

def bitki_bilgisi_getir(bitki_turu):
    aranan = str(bitki_turu).lower().strip()
    print(f"🌿 [MOCK API] Veri aranıyor: {aranan}")

    for key, data in MOCK_BITKILER.items():
        if key in aranan:
            sonuc = {
                "orijinal_sulama": data["sulama"],
                "periyot_gun":     data["periyot"],
                "isik":            data["isik"]
            }
            print(f"✅ Sabit Veri Bulundu: {sonuc}")
            return sonuc

    uretilen_sonuc = {
        "orijinal_sulama": "Average",
        "periyot_gun":     random.choice([3, 5, 7, 10, 14]),
        "isik":            random.choice(["Full sun", "Part shade", "Indirect sunlight", "Full shade"])
    }
    print(f"✅ Rastgele Veri Üretildi: {uretilen_sonuc}")
    return uretilen_sonuc

def hastalik_tespit(yaprak_durumu, toprak_nemi):
    return {"tehlike_seviyesi": "yok", "teshis": "Sağlıklı", "oneri": "Bakıma devam."}

def bakim_takvimi_olustur(bitki_bilgisi):
    if not bitki_bilgisi:
        return {"sulama_gun": 7, "gubreleme_gun": 30, "budama_gun": 90}
    sulama_gun = bitki_bilgisi.get("periyot_gun", 7)
    return {"sulama_gun": sulama_gun, "gubreleme_gun": sulama_gun * 4, "budama_gun": sulama_gun * 12}