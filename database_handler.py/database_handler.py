import pyodbc
from perenual_service import bitki_bilgisi_getir

def baglan():
    try:
        # SQL Server bağlantı cümlesi
        server = 'SERVER_ADIN\\SQLEXPRESS' # Kendi Server adınla değiştir!
        database = 'AkilliBahceDB'
        
        conn = pyodbc.connect(
            f'Driver={{SQL Server}};'
            f'Server={server};'
            f'Database={database};'
            f'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print(f"Veritabanı bağlantı hatası: {e}")
        return None

def akilli_bitki_ekle(ad, tur, ekim_tarihi, konum):
    
    api_bilgileri = bitki_bilgisi_getir(tur)
    
    
    hesaplanan_periyot = 7 
    
    if api_bilgileri:
        hesaplanan_periyot = api_bilgileri["periyot_gun"]
        print(f"[{tur}] için API bilgileri alındı! Işık: {api_bilgileri['isik']}, Sulama Periyodu: {hesaplanan_periyot} gün.")
    
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        sorgu = "INSERT INTO Bitkiler (Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sorgu, (ad, tur, ekim_tarihi, hesaplanan_periyot, konum))
        conn.commit() 
        conn.close()
        print(f"{ad} başarıyla veritabanına eklendi.")

def tum_bitkileri_getir():
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bitkiler")
        veriler = cursor.fetchall()
        conn.close()
        return veriler