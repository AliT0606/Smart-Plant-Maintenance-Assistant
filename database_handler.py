import pyodbc
import datetime
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
# SAĞLIK HESAPLAMA ALGORİTMASI
# ─────────────────────────────────────────
def saglik_hesapla(son_sulama, sulama_periyodu):
    """Son sulama tarihine göre sağlık puanı hesapla.
    
    - Sulama periyodundan 1-3 gün fazla: -5%
    - 4-7 gün fazla: -15%
    - 8+ gün fazla: -25%
    - Zamanında sulanmışsa: +5% (max 100%)
    """
    if not son_sulama:
        return 80  # Hiç sulanmamışsa varsayılan
    
    try:
        from datetime import date, datetime
        if isinstance(son_sulama, str):
            son = date.fromisoformat(son_sulama[:10])
        else:
            son = son_sulama
        
        bugun = date.today()
        gecikme = (bugun - son).days - sulama_periyodu
        
        if gecikme <= 0:
            return min(100, 85 + 5)  # Zamanında → 90%
        elif gecikme <= 3:
            return max(5, 85 - 5)   # 1-3 gün geç → 80%
        elif gecikme <= 7:
            return max(5, 85 - 15)  # 4-7 gün geç → 70%
        else:
            return max(5, 85 - 25)  # 8+ gün geç → 60%
    except Exception:
        return 80

# ─────────────────────────────────────────
# OKUMA
# ─────────────────────────────────────────
def tum_bitkileri_getir():
    """Tüm bitkileri DB'den çeker.
    Sütun sırası: Id, Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum, Saglik, SonSulama"""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Id, Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum, Saglik, SonSulama FROM Bitkiler")
        veriler = cursor.fetchall()
        conn.close()
        return veriler
    return []

def bitki_getir(bitki_id):
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Id, Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum, Saglik, SonSulama FROM Bitkiler WHERE Id = ?", (bitki_id,))
        veri = cursor.fetchone()
        conn.close()
        return veri
    return None

def sulama_gecmisi_getir(bitki_id):
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
def akilli_bitki_ekle(ad, tur, ekim_tarihi, konum, sulama_periyodu):
    """Bitkiyi veritabanına ekler."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Bitkiler (Ad, Tur, EkimTarihi, SulamaPeriyodu, Konum, Saglik, SonSulama) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (ad, tur, ekim_tarihi, sulama_periyodu, konum, 80, None)
        )
        conn.commit()
        conn.close()
        print(f"✅ {ad} veritabanına eklendi.")

def sulama_kaydet(bitki_id, tarih):
    """Sulamayı hem SulamaGecmisi'ne hem Bitkiler.SonSulama'ya kaydeder."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        tarih_str = str(tarih)
        cursor.execute(
            "INSERT INTO SulamaGecmisi (BitkiId, SulamaTarihi) VALUES (?, ?)",
            (bitki_id, tarih_str)
        )
        cursor.execute(
            "UPDATE Bitkiler SET SonSulama = ? WHERE Id = ?",
            (tarih_str, bitki_id)
        )
        conn.commit()
        conn.close()
        print(f"Bitki {bitki_id} sulandı: {tarih_str}")

# ─────────────────────────────────────────
# GÜNCELLEME
# ─────────────────────────────────────────
def bitki_guncelle(bitki_id, yeni_ad=None, yeni_konum=None, yeni_periyot=None, yeni_saglik=None, yeni_son_sulama=None):
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        if yeni_ad:
            cursor.execute("UPDATE Bitkiler SET Ad = ? WHERE Id = ?",             (yeni_ad,         bitki_id))
        if yeni_konum:
            cursor.execute("UPDATE Bitkiler SET Konum = ? WHERE Id = ?",          (yeni_konum,      bitki_id))
        if yeni_periyot:
            cursor.execute("UPDATE Bitkiler SET SulamaPeriyodu = ? WHERE Id = ?", (yeni_periyot,    bitki_id))
        if yeni_saglik is not None:
            cursor.execute("UPDATE Bitkiler SET Saglik = ? WHERE Id = ?",         (yeni_saglik,     bitki_id))
        if yeni_son_sulama is not None:
            cursor.execute("UPDATE Bitkiler SET SonSulama = ? WHERE Id = ?",      (yeni_son_sulama, bitki_id))
        conn.commit()
        conn.close()

# ─────────────────────────────────────────
# SİLME
# ─────────────────────────────────────────
def bitki_sil(bitki_id):
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM SulamaGecmisi WHERE BitkiId = ?",  (bitki_id,))
        cursor.execute("DELETE FROM Bitkiler WHERE Id = ?",             (bitki_id,))
        conn.commit()
        conn.close()
        print(f"Bitki {bitki_id} silindi.")

# ─────────────────────────────────────────
# TAMAMLANAN GÖREVLER
# ─────────────────────────────────────────
def gorev_tamamla(gorev_id):
    """Görevi DB'ye tamamlandı olarak işaretle."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO TamamlananGorevler (GorevId, Tarih) VALUES (?, ?)",
                (gorev_id, str(datetime.date.today()))
            )
            conn.commit()
        except Exception:
            pass  # Zaten eklenmiş olabilir (UNIQUE constraint)
        conn.close()

def gorev_tamamlanmadi(gorev_id):
    """Görevin tamamlanma işaretini kaldır."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TamamlananGorevler WHERE GorevId = ?", (gorev_id,))
        conn.commit()
        conn.close()

def tamamlanan_gorevleri_getir():
    """DB'deki tüm tamamlanan görev ID'lerini set olarak döndür."""
    conn = baglan()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT GorevId FROM TamamlananGorevler")
        rows = cursor.fetchall()
        conn.close()
        return set(row[0] for row in rows)
    return set()
