import pyodbc
from perenual_service import bitki_bilgisi_getir

# ─────────────────────────────────────────
# BAĞLANTI
# ─────────────────────────────────────────
def baglan():
    try:
        server   = 'SWIPES-MONSTER\\SQLEXPRESS'
        database = 'AkilliBahceDB'
        conn = pyodbc.connect(
            f'Driver={{SQL Server}};'
            f'Server={server};'
            f'Database={database};'
            f'Trusted_Connection=yes;'
            f'TrustServerCertificate=yes;'
        )
        return conn
    except Exception as e:
        print(f"Veritabanı bağlantı hatası: {e}")
        return None

# ─────────────────────────────────────────
# OKUMA
# ─────────────────────────────────────────
def tum_bitkileri_getir():
    """Tüm bitkileri DB'den çeker.
    Döndürdüğü sütun sırası: Id, Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum"""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bitkiler")
        veriler = cursor.fetchall()
        conn.close()
        return veriler
    return []

def bitki_getir(bitki_id):
    """Tek bir bitkiyi ID'ye göre getirir."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bitkiler WHERE Id = ?", (bitki_id,))
        veri = cursor.fetchone()
        conn.close()
        return veri
    return None

def sulama_gecmisi_getir(bitki_id):
    """Belirli bir bitkinin tüm sulama geçmişini getirir."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM SulamaGecmisi WHERE BitkiId = ? ORDER BY SulamaTarihi DESC",
            (bitki_id,)
        )
        veriler = cursor.fetchall()
        conn.close()
        return veriler
    return []

# ─────────────────────────────────────────
# EKLEME
# ─────────────────────────────────────────
# ─────────────────────────────────────────
# EKLEME
# ─────────────────────────────────────────
def akilli_bitki_ekle(ad, tur, ekim_tarihi, konum, sulama_periyodu):
    """Arayüzden (API'den) gelen hazır periyodu doğrudan veritabanına ekler."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Bitkiler (Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum) VALUES (?, ?, ?, ?, ?)",
            (ad, tur, ekim_tarihi, sulama_periyodu, konum)
        )
        conn.commit()
        conn.close()
        print(f"✅ {ad} başarıyla veritabanına eklendi (Periyot: {sulama_periyodu} gün).")

def sulama_kaydet(bitki_id, tarih):
    """Bir bitkinin sulandığını SulamaGecmisi tablosuna kaydeder."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO SulamaGecmisi (BitkiId, SulamaTarihi) VALUES (?, ?)",
            (bitki_id, tarih)
        )
        conn.commit()
        conn.close()
        print(f"Bitki {bitki_id} için sulama {tarih} tarihinde kaydedildi.")

# ─────────────────────────────────────────
# GÜNCELLEME
# ─────────────────────────────────────────
def bitki_guncelle(bitki_id, yeni_ad=None, yeni_konum=None, yeni_periyot=None):
    """Bitkinin istenen alanlarını günceller."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        if yeni_ad:
            cursor.execute("UPDATE Bitkiler SET Ad = ? WHERE Id = ?",           (yeni_ad,     bitki_id))
        if yeni_konum:
            cursor.execute("UPDATE Bitkiler SET Konum = ? WHERE Id = ?",        (yeni_konum,  bitki_id))
        if yeni_periyot:
            cursor.execute("UPDATE Bitkiler SET SulamaPeriyodu = ? WHERE Id = ?",(yeni_periyot,bitki_id))
        conn.commit()
        conn.close()
        print(f"Bitki {bitki_id} güncellendi.")

# ─────────────────────────────────────────
# SİLME
# ─────────────────────────────────────────
def bitki_sil(bitki_id):
    """Bitkiyi ve ona ait sulama geçmişini DB'den siler."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        # Önce sulama geçmişini sil (foreign key varsa)
        cursor.execute("DELETE FROM SulamaGecmisi WHERE BitkiId = ?", (bitki_id,))
        cursor.execute("DELETE FROM Bitkiler WHERE Id = ?",            (bitki_id,))
        conn.commit()
        conn.close()
        print(f"Bitki {bitki_id} silindi.")