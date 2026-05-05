# Yerel bitki kutuphanesi — API gerektirmez, 100+ bitki tanımlı
MOCK_BITKILER = {
    # ── İç Mekan Bitki Bakım Listesi ──
    "monstera deliciosa":       {"sulama": "Average",  "periyot": 7,  "isik": "Indirect sunlight"},   # Delik Yapraklı Monstera
    "spathiphyllum":            {"sulama": "Frequent", "periyot": 4,  "isik": "Part shade"},           # Barış Çiçeği
    "dracaena trifasciata":     {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun, Part shade"}, # Kayınvalide Dili (Snake Plant)
    "aloe vera":                {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Sarısabır / Aloe
    "epipremnum aureum":        {"sulama": "Average",  "periyot": 7,  "isik": "Part shade"},           # Pothos / Şeytan Sarmaşığı
    "chlorophytum comosum":     {"sulama": "Average",  "periyot": 7,  "isik": "Part shade"},           # Kurdele Çiçeği
    "echeveria":                {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Sukulent / Taş Gülü
    "phalaenopsis":             {"sulama": "Average",  "periyot": 7,  "isik": "Indirect sunlight"},   # Kelebek Orkide
    "pilea peperomioides":      {"sulama": "Average",  "periyot": 5,  "isik": "Bright indirect"},     # Para Çiçeği
    "ficus benjamina":          {"sulama": "Average",  "periyot": 7,  "isik": "Bright indirect"},     # Ağlayan İncir
    "ficus lyrata":             {"sulama": "Average",  "periyot": 7,  "isik": "Bright indirect"},     # Keman Yapraklı Fikus
    "calathea":                 {"sulama": "Frequent", "periyot": 4,  "isik": "Indirect sunlight"},   # Dua Çiçeği
    "dracaena marginata":       {"sulama": "Average",  "periyot": 10, "isik": "Indirect sunlight"},   # Kırmızı Kenarlı Drakena
    "zamioculcas zamiifolia":   {"sulama": "Minimum",  "periyot": 14, "isik": "Part shade"},           # ZZ Bitkisi
    "aglaonema":                {"sulama": "Average",  "periyot": 7,  "isik": "Indirect sunlight"},   # Aglaonema / Çin Herdem Yeşili
    "anthurium andraeanum":     {"sulama": "Average",  "periyot": 7,  "isik": "Indirect sunlight"},   # Flamingo Çiçeği
    "begonia rex":              {"sulama": "Average",  "periyot": 5,  "isik": "Part shade"},           # Kral Begonya
    "nephrolepis exaltata":     {"sulama": "Frequent", "periyot": 3,  "isik": "Part shade"},           # Boston Eğrelti Otu
    "peperomia obtusifolia":    {"sulama": "Minimum",  "periyot": 10, "isik": "Indirect sunlight"},   # Peperomia / Radyo Bitkisi
    "maranta leuconeura":       {"sulama": "Frequent", "periyot": 4,  "isik": "Indirect sunlight"},   # Dua Bitkisi
    "tradescantia zebrina":     {"sulama": "Average",  "periyot": 5,  "isik": "Bright indirect"},     # Tradeskantya / Gökkuşağı Bitkisi
    "scindapsus pictus":        {"sulama": "Average",  "periyot": 7,  "isik": "Part shade"},           # Gümüş Pothos
    "syngonium podophyllum":    {"sulama": "Average",  "periyot": 6,  "isik": "Indirect sunlight"},   # Ok Başı Bitkisi
    "dieffenbachia":            {"sulama": "Average",  "periyot": 7,  "isik": "Indirect sunlight"},   # Dilsiz Sopa / Deffenbahya
    "philodendron hederaceum":  {"sulama": "Average",  "periyot": 7,  "isik": "Indirect sunlight"},   # Kalp Yapraklı Filodendron
    "schefflera arboricola":    {"sulama": "Average",  "periyot": 7,  "isik": "Bright indirect"},     # Şemsiye Ağacı
    "yucca elephantipes":       {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Fil Ayağı Yukka
    "crassula ovata":           {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Jade Bitkisi / Para Ağacı
    "haworthiopsis fasciata":   {"sulama": "Minimum",  "periyot": 14, "isik": "Indirect sunlight"},   # Havorthia / Zebra Kaktüs
    "gasteria":                 {"sulama": "Minimum",  "periyot": 14, "isik": "Part shade"},           # Gasteria / Öküz Dili
    "aspidistra elatior":       {"sulama": "Minimum",  "periyot": 10, "isik": "Part shade"},           # Demir Bitkisi 
    "hoya carnosa":             {"sulama": "Average",  "periyot": 10, "isik": "Bright indirect"},     # Mum Çiçeği
    "alocasia amazonica":       {"sulama": "Frequent", "periyot": 4,  "isik": "Indirect sunlight"},   # Fil Kulağı / Afrika Maskesi
    "colocasia esculenta":      {"sulama": "Frequent", "periyot": 3,  "isik": "Part shade"},           # Gölevez / Taro
    "strelitzia reginae":       {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Cennet Kuşu Çiçeği
    "cycas revoluta":           {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Sagu Palmiyesi
    # ── Kaktüs & Sukulent ──
    "cactus":                 {"sulama": "Minimum",  "periyot": 21, "isik": "Full sun"},             # Kaktüs (genel)
    "opuntia":                {"sulama": "Minimum",  "periyot": 21, "isik": "Full sun"},             # Frenk İnciri Kaktüsü
    "cereus":                 {"sulama": "Minimum",  "periyot": 21, "isik": "Full sun"},             # Sütun Kaktüs
    "mammillaria":            {"sulama": "Minimum",  "periyot": 21, "isik": "Full sun"},             # Küre Kaktüs
    "sempervivum":            {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Taş Gülü / Tavuk ve Civciv
    "sedum":                  {"sulama": "Minimum",  "periyot": 14, "isik": "Full sun"},             # Sedum / Dondurmacı Çiçeği
    # ── Dış Mekan & Bahçe Çiçekleri ──
    "rose":                   {"sulama": "Average",  "periyot": 5,  "isik": "Full sun"},             # Gül
    "lavender":               {"sulama": "Minimum",  "periyot": 10, "isik": "Full sun"},             # Lavanta
    "hydrangea":              {"sulama": "Frequent", "periyot": 3,  "isik": "Part shade"},           # Ortanca
    "geranium":               {"sulama": "Average",  "periyot": 5,  "isik": "Full sun"},             # Sardunya
    "petunia":                {"sulama": "Frequent", "periyot": 3,  "isik": "Full sun"},             # Petunya
    "chrysanthemum":          {"sulama": "Average",  "periyot": 5,  "isik": "Full sun"},             # Kasımpatı
    "dahlia":                 {"sulama": "Average",  "periyot": 5,  "isik": "Full sun"},             # Yıldız Çiçeği / Dalya
    "tulipa":                 {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Lale
    "narcissus":              {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Nergis
    "iris":                   {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Süsen
    "bougainvillea":          {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Begonvil
    "jasmine":                {"sulama": "Average",  "periyot": 5,  "isik": "Full sun"},             # Yasemin
    "wisteria":               {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Mor Salkım
    "hibiscus":               {"sulama": "Frequent", "periyot": 3,  "isik": "Full sun"},             # Nar Çiçeği / Hibiskus
    "camelia":                {"sulama": "Average",  "periyot": 5,  "isik": "Part shade"},           # Kamelya
    "magnolia":               {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Manolya
    "forsythia":              {"sulama": "Average",  "periyot": 7,  "isik": "Full sun"},             # Altın Çan
    "rhododendron":           {"sulama": "Frequent", "periyot": 4,  "isik": "Part shade"},           # Orman Gülü
    "azalea":                 {"sulama": "Frequent", "periyot": 4,  "isik": "Part shade"},           # Açelya
    # ── Sebze & Ot ──
    "basil":                  {"sulama": "Frequent", "periyot": 3,  "isik": "Full sun"},             # Fesleğen
    "mint":                   {"sulama": "Frequent", "periyot": 3,  "isik": "Part shade"},           # Nane
    "rosemary":               {"sulama": "Minimum",  "periyot": 10, "isik": "Full sun"},             # Biberiye
    "thyme":                  {"sulama": "Minimum",  "periyot": 10, "isik": "Full sun"},             # Kekik
    "parsley":                {"sulama": "Average",  "periyot": 5,  "isik": "Full sun"},             # Maydanoz
    "tomato":                 {"sulama": "Frequent", "periyot": 2,  "isik": "Full sun"},             # Domates
    "pepper":                 {"sulama": "Frequent", "periyot": 3,  "isik": "Full sun"},             # Biber
    "strawberry":             {"sulama": "Frequent", "periyot": 3,  "isik": "Full sun"},             # Çilek
    "cucumber":               {"sulama": "Frequent", "periyot": 2,  "isik": "Full sun"},             # Salatalık
    "eggplant":               {"sulama": "Frequent", "periyot": 3,  "isik": "Full sun"},             # Patlıcan
    "sage":                   {"sulama": "Minimum",  "periyot": 10, "isik": "Full sun"},             # Adaçayı
}

def bitki_bilgisi_getir(bitki_turu):
    aranan = str(bitki_turu).lower().strip()
    for key, data in MOCK_BITKILER.items():
        if key in aranan or aranan in key:
            return {
                "orijinal_sulama": data["sulama"],
                "periyot_gun":     data["periyot"],
                "isik":            data["isik"]
            }
    # Bilinmeyen bitki için makul varsayılan
    return {
        "orijinal_sulama": "Average",
        "periyot_gun":     7,
        "isik":            "Indirect sunlight"
    }



def hastalik_tespit(yaprak_durumu, toprak_nemi):
    tehlike = "yok"
    teshis  = "Sağlıklı görünüyor."
    oneri   = "Mevcut bakım rutinine devam et."

    if toprak_nemi == "Islak" and yaprak_durumu == "Sararma":
        tehlike = "yuksek"
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
        tehlike = "yuksek"
        teshis  = "Böcek istilası"
        oneri   = "Yaprakların altını kontrol et, böcek ilacı kullan."
    elif yaprak_durumu == "Kahverengi Lekeler":
        tehlike = "orta"
        teshis  = "Yaprak yanığı veya mantar"
        oneri   = "Direkt güneşten koru, etkilenen yaprakları kes."
    elif yaprak_durumu == "Düşen Yapraklar":
        tehlike = "orta"
        teshis  = "Stres (ışık/su/sıcaklık değişimi)"
        oneri   = "Konumunu değiştirme, sulama düzenini kontrol et."
    elif yaprak_durumu == "Solma":
        tehlike = "orta"
        teshis  = "Su stresi veya kök sorunu"
        oneri   = "Önce toprak nemini kontrol et, sonra kökü incele."

    return {"tehlike_seviyesi": tehlike, "teshis": teshis, "oneri": oneri}

def bakim_takvimi_olustur(bitki_bilgisi):
    if not bitki_bilgisi:
        return {"sulama_gun": 7, "gubreleme_gun": 30, "budama_gun": 90}
    sulama_gun = bitki_bilgisi.get("periyot_gun", 7)
    return {"sulama_gun": sulama_gun, "gubreleme_gun": sulama_gun * 4, "budama_gun": sulama_gun * 12}