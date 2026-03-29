import requests

def hava_durumu_kontrol(sehir="Istanbul"):
    # Buradaki API KEY'i OpenWeatherMap'ten ücretsiz almalısın [cite: 10]
    api_key = "SENIN_API_KEYIN_BURAYA" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=tr"
    
    try:
        response = requests.get(url) [cite: 21]
        data = response.json()
        
        # Hava durumu açıklamasını ve yağmur kontrolünü al 
        durum = data['weather'][0]['main'] # 'Rain', 'Clear' vb.
        sicaklik = data['main']['temp']
        
        yagmur_var_mi = False
        if durum == "Rain" or durum == "Drizzle":
            yagmur_var_mi = True
            
        return {
            "sicaklik": sicaklik,
            "durum": durum,
            "yagmur_var_mi": yagmur_var_mi
        }
    except Exception as e:
        print(f"Hava durumu çekilemedi: {e}")
        return None

# Test için:
# print(hava_durumu_kontrol("Istanbul"))