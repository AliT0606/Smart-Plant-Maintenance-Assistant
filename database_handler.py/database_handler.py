import pyodbc

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

def bitki_ekle(ad, tur, ekim_tarihi, periyod, konum):
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        # SQL tablosuna veri ekleme sorgusu [cite: 12]
        sorgu = "INSERT INTO Bitkiler (Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sorgu, (ad, tur, ekim_tarihi, periyod, konum))
        conn.commit() # Değişiklikleri kaydet [cite: 13]
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