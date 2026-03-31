import requests

def bitki_bilgisi_getir(bitki_turu):
    # Perenual API
    api_key = "sk-0zds69cc2f32ec01016010"
    # Tür ismine göre arama yapan endpoint
    url = f"https://perenual.com/api/species-list?key={api_key}&q={bitki_turu}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        
        if data.get('data') and len(data['data']) > 0:
            ilk_sonuc = data['data'][0]
            sulama = ilk_sonuc.get('watering', 'Average')
            isik = ilk_sonuc.get('sunlight', ['Bilinmiyor'])
            
            
            periyot_gun = 7 # Varsayılan (Average)
            if sulama == "Frequent":
                periyot_gun = 2 # Sık sulama
            elif sulama == "Minimum":
                periyot_gun = 14 # Az sulama
                
            return {
                "orijinal_sulama": sulama,
                "periyot_gun": periyot_gun,
                "isik": ", ".join(isik)
            }
        else:
            print("Bitki API'de bulunamadı.")
            return None
            
    except Exception as e:
        print(f"Perenual API bağlantı hatası: {e}")
        return None