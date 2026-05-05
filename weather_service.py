import requests
import datetime

# ─────────────────────────────────────────
# HAVA DURUMU
# ─────────────────────────────────────────
def hava_durumu_kontrol(sehir="Elazig"):
    """OpenWeatherMap'ten anlık hava durumu çeker.
    Döndürür: {sicaklik, durum, yagmur_var_mi} veya None"""
    api_key = "aabb64130ab58972ffe077601044d0a8"  # openweathermap.org'dan ücretsiz al
    url     = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=tr"

    try:
        response = requests.get(url, timeout=5)
        data     = response.json()

        if data.get("cod") != 200:
            raise ValueError(f"API hatası: {data.get('message', 'Bilinmeyen hata')}")

        durum    = data['weather'][0]['main']
        sicaklik = data['main']['temp']
        nem      = data['main']['humidity']
        uv_index = data.get('uvi', None)  # UV bazı planlarda gelir

        yagmur_var_mi = durum in ["Rain", "Drizzle", "Thunderstorm"]

        return {
            "sicaklik":      sicaklik,
            "durum":         durum,
            "nem":           nem,
            "uv_index":      uv_index,
            "yagmur_var_mi": yagmur_var_mi
        }
    except Exception as e:
        print(f"Hava durumu çekilemedi: {e}")
        # API çalışmıyorsa makul bir mock döndür
        return {
            "sicaklik":      22.0,
            "durum":         "Clouds",
            "nem":           55,
            "uv_index":      None,
            "yagmur_var_mi": False,
            "_mock":         True   # UI'da uyarı göstermek için
        }

# ─────────────────────────────────────────
# SULAMA TAVSİYESİ
# ─────────────────────────────────────────
def sulama_tavsiyesi(hava_data, bitki):
    """Hava durumuna ve bitkiye göre sulama tavsiyesi üretir.
    Döndürür: {sulama_yap: bool, mesaj: str}"""

    if hava_data is None:
        return {"sulama_yap": True, "mesaj": "Hava durumu alınamadı, normal sulama programını uygula."}

    dis_mekan     = bitki.get("konum") in ["Balkon", "Bahçe"]
    yagmur_var_mi = hava_data.get("yagmur_var_mi", False)
    sicaklik      = hava_data.get("sicaklik", 20)
    nem           = hava_data.get("nem", 50)

    # Dış mekân + yağmur → sulama yapma
    if dis_mekan and yagmur_var_mi:
        return {
            "sulama_yap": False,
            "mesaj":      f"🌧️ {bitki['ad']} dış mekânda, bugün yağmur var — sulama atlandı."
        }

    # Çok sıcak → daha fazla sulama gerekebilir
    if sicaklik > 30 and nem < 40:
        return {
            "sulama_yap": True,
            "mesaj":      f"🌡️ Hava çok sıcak ve kuru ({sicaklik}°C). {bitki['ad']} için ek sulama önerilir."
        }

    # Normal
    return {
        "sulama_yap": True,
        "mesaj":      f"✅ {bitki['ad']} için sulama zamanı. Hava: {sicaklik}°C, Nem: %{nem}."
    }

# ─────────────────────────────────────────
# GÖREV OLUŞTUR
# ─────────────────────────────────────────
def gorev_olustur(bitkiler, hava_data=None):
    """Tüm bitkiler için bakım görevleri listesi üretir.
    Hava durumuna göre dış mekân sulamalarını otomatik atlar.
    Döndürür: [{"bitki", "tur", "tarih", "not"}, ...]"""

    gorevler  = []
    bugun     = datetime.date.today()
    yagmur    = hava_data.get("yagmur_var_mi", False) if hava_data else False

    IKONLAR = {"Sulama": "💧", "Gübre": "🌱", "Kontrol": "🔍", "Temizlik": "🍃"}

    for p in bitkiler:
        dis_mekan = p.get("konum") in ["Balkon", "Bahçe"]

        # Sulama görevi — yağmurluysa dış bitkiyi atla
        if p.get("sulama_periyodu", 7) <= 3:
            if not (yagmur and dis_mekan):
                gorevler.append({
                    "bitki": p["ad"],
                    "tur":   "Sulama",
                    "tarih": bugun,
                    "not":   sulama_tavsiyesi(hava_data, p)["mesaj"]
                })

        # Sabit periyotlu görevler
        gorevler.append({"bitki": p["ad"], "tur": "Temizlik", "tarih": bugun + datetime.timedelta(days=1),  "not": "Yaprak temizliği yapılacak"})
        gorevler.append({"bitki": p["ad"], "tur": "Gübre",    "tarih": bugun + datetime.timedelta(days=3),  "not": "Gübre zamanı geldi"})
        gorevler.append({"bitki": p["ad"], "tur": "Kontrol",  "tarih": bugun + datetime.timedelta(days=7),  "not": "Genel sağlık kontrolü"})

    return gorevler
