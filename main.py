def rle_encode(data):
    """
    Bu fonksiyon, ardışık tekrar eden karakterleri sayarak veriyi sıkıştırır (Encode).
    Örnek: 'AAAAA' -> '5A'
    """
    # Eğer veri boşsa boş bir string döndürerek hata oluşmasını engeller
    if not data:
        return ""
    
    encoding = "" # Sıkıştırılmış sonucun tutulacağı değişken
    i = 0 # Veri üzerinde gezinmek için kullanılan indeks (imleç)
    
    # Tüm veriyi karakter karakter tarayan ana döngü
    while i < len(data):
        count = 1 # Her yeni karakter için sayacı 1'den başlat
        
        # Mevcut karakter bir sonrakiyle aynı olduğu sürece sayacı artır
        # (Dizinin sonuna gelmediğimizden emin olur: i + 1 < len(data))
        while i + 1 < len(data) and data[i] == data[i+1]:
            count += 1
            i += 1
        
        # Karakterin sayısını ve kendisini (Örn: '5' + 'A') sonuca ekle
        encoding += str(count) + data[i]
        i += 1 # Bir sonraki farklı karaktere geç
        
    return encoding

def rle_decode(data):
    """
    Sıkıştırılmış formattaki veriyi orijinal haline döndürür (Decode).
    Örnek: '5A' -> 'AAAAA'
    """
    decode = "" # Geri açılan verinin tutulacağı değişken
    count_str = "" # Karşılaşılan sayıları (rakamları) biriktirmek için
    
    for char in data:
        # Karakter bir rakam ise (0-9 arası)
        if char.isdigit():
            # Sayıyı biriktir (Örn: '1' ve '0' gelirse '10' olur)
            count_str += char
        else:
            # Karakter harf ise, o ana kadar biriken sayıyı tamsayıya çevir
            count = int(count_str)
            # Harfi sayı kadar tekrar ederek sonuca ekle (Örn: 'A' * 5)
            decode += char * count
            count_str = "" # Yeni sayı grubu için sayacı sıfırla
            
    return decode

def calculate_compression_ratio(original, compressed):
    """
    Verinin ne kadar küçüldüğünü yüzde olarak hesaplar.
    """
    original_size = len(original) # Orijinal metnin karakter sayısı
    compressed_size = len(compressed) # Sıkıştırılmış metnin karakter sayısı
    
    # Formül: (Sıkıştırılmış Boyut / Orijinal Boyut) * 100
    ratio = (compressed_size / original_size) * 100
    return ratio

# --- UYGULAMA BÖLÜMÜ ---

# Ödev görselindeki örnek girdi
input_data = "AAAAABBBCCDAA"

# 1. Aşama: Veriyi sıkıştırıyoruz
compressed_data = rle_encode(input_data)

# 2. Aşama: Sıkıştırılmış veriyi geri açıyoruz
decompressed_data = rle_decode(compressed_data)

# 3. Aşama: Verimliliği ölçüyoruz
ratio = calculate_compression_ratio(input_data, compressed_data)

# Sonuçların ekrana basılması
print(f"Girdi: {input_data}")
print(f"Sıkıştırılmış: {compressed_data}")
print(f"Geri Açılmış: {decompressed_data}")
print(f"Sıkıştırma Oranı: %{ratio:.2f}") # Noktadan sonra 2 basamak gösterir