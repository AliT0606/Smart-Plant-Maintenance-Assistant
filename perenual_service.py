import requests

API_KEY = "Ssk-0zds69cc2f32ec01016010"  # perenual.com'dan alınan key
BASE    = "https://perenual.com/api"

# ─────────────────────────────────────────
# BİTKİ BİLGİSİ
# ─────────────────────────────────────────
def bitki_bilgisi_getir(bitki_turu):
    """Tür ismine göre Perenual API'den sulama ve ışık bilgisi çeker.
    Döndürür: {orijinal_sulama, periyot_gun, isik} veya None"""
    url = f"{BASE}/species-list?key={API_KEY}&q={bitki_turu}"

    try:
        response = requests.get(url, timeout=5)
        data     = response.json()

        if data.get('data') and len(data['data']) > 0:
            ilk       = data['data'][0]
            sulama    = ilk.get('watering', 'Average')
            isik_list = ilk.get('sunlight', ['Bilinmiyor'])

            # İngilizce → gün sayısına çevir
            periyot_gun = 7
            if sulama == "Frequent":
                periyot_gun = 2
            elif sulama == "Minimum":
                periyot_gun = 14

            return {
                "orijinal_sulama": sulama,
                "periyot_gun":     periyot_gun,
                "isik":            ", ".join(isik_list)
            }
        else:
            print(f"'{bitki_turu}' API'de bulunamadı.")
            return None

    except Exception as e:
        print(f"Perenual API bağlantı hatası: {e}")
        return None

# ─────────────────────────────────────────
# BİTKİ FOTOĞRAFI
# ─────────────────────────────────────────
def bitki_fotograf_getir(bitki_turu):
    """Perenual API'den bitkinin fotoğraf URL'ini çeker.
    Döndürür: url (str) veya None"""
    url = f"{BASE}/species-list?key={API_KEY}&q={bitki_turu}"

    try:
        response = requests.get(url, timeout=5)
        data     = response.json()

        if data.get('data') and len(data['data']) > 0:
            ilk         = data['data'][0]
            default_img = ilk.get('default_image', {})
            foto_url    = default_img.get('medium_url') or default_img.get('original_url')
            return foto_url
        return None

    except Exception as e:
        print(f"Fotoğraf çekilemedi: {e}")
        return None

# ─────────────────────────────────────────
# HASTALIK TESPİT
# ─────────────────────────────────────────
def hastalik_tespit(yaprak_durumu, toprak_nemi):
    """Yaprak durumu ve toprak nemine göre teşhis üretir.
    Döndürür: {tehlike_seviyesi, teshis, oneri}"""

    tehlike = "yok"
    teshis  = "Sağlıklı görünüyor."
    oneri   = "Mevcut bakım rutinine devam et."

    if toprak_nemi == "Islak" and yaprak_durumu == "Sararma":
        tehlike = "yüksek"
        teshis  = "Kök çürümesi (aşırı sulama)"
        oneri   = "Sulamayı hemen durdur, toprağın kurumasını bekle."

    elif toprak_nemi == "Kuru" and yaprak_durumu == "Kahverengi Uçlar":
        tehlike = "orta"
        teshis  = "Aşırı susuzluk"
        oneri   = "Derin sulama yap, saksı drenajını kontrol et."

    elif yaprak_durumu == "Beyaz Lekeler":
        tehlike = "orta"
        teshis  = "Külleme (mantar hastalığı)"
        oneri   = "Hava sirkülasyonunu artır, mantar ilacı uygula."

    elif yaprak_durumu == "Delikler":
        tehlike = "yüksek"
        teshis  = "Böcek istilası"
        oneri   = "Yaprakların altını kontrol et, böcek ilacı kullan."

    elif toprak_nemi == "Nemli" and yaprak_durumu == "Sağlıklı Yeşil":
        tehlike = "yok"
        teshis  = "Optimal sağlık"
        oneri   = "Hiçbir işlem gerekmiyor."

    return {
        "tehlike_seviyesi": tehlike,
        "teshis":           teshis,
        "oneri":            oneri
    }

# ─────────────────────────────────────────
# BAKIM TAKVİMİ OLUŞTUR
# ─────────────────────────────────────────
def bakim_takvimi_olustur(bitki_bilgisi):
    """API'den gelen bilgiyle bakım periyotlarını hesaplar.
    Döndürür: {sulama_gun, gubreleme_gun, budama_gun}"""

    if not bitki_bilgisi:
        return {"sulama_gun": 7, "gubreleme_gun": 30, "budama_gun": 90}

    sulama_gun = bitki_bilgisi.get("periyot_gun", 7)

    # Sulama periyoduna göre diğer periyotları orantılı hesapla
    gubreleme_gun = sulama_gun * 4   # 4 sulamada bir gübre
    budama_gun    = sulama_gun * 12  # 12 sulamada bir budama

    return {
        "sulama_gun":    sulama_gun,
        "gubreleme_gun": gubreleme_gun,
        "budama_gun":    budama_gun
    }
