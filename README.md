# BLM101_25360859321_MeryemS-meyyeAysal
Öğrenci Bilgileri:Meryem Sümeyye Aysal 25360859321
Proje Konusu:Veri Depolama Ve Sıkıştırma Algoritmaları
Youtube Linki:
Proje Açıklaması:Kod Ne Yapıyor?
Bu program, bilgisayar bilimlerinde Kayıpsız Sıkıştırma (Lossless Compression) yöntemlerinden biri olan Run-Length Encoding (RLE) algoritmasını simüle eder.
Sıkıştırma (Encoding): Metin içerisindeki ardışık tekrar eden karakterleri tespit eder ve bunları tekrar_sayısı + karakter formatına dönüştürerek veri boyutunu küçültür.
Geri Açma (Decoding): Sıkıştırılmış veriyi okuyarak, hiçbir veri kaybı yaşanmadan orijinal metne geri döndürür.
Analiz: İşlem sonunda sıkıştırma oranını hesaplayarak algoritmanın verimliliğini gösterir.
A. Sıkıştırma (Encode) Mantığı
Tarama: Program, verilen metni soldan sağa doğru bir döngü ile tarar.
Karşılaştırma: Mevcut karakteri, bir sonraki karakter ile karşılaştırır.
Sayma: Eğer karakterler aynıysa bir sayaç (count) birer birer artırılır.
Yazma: Karakter değiştiğinde (veya metin bittiğinde), o ana kadar sayılan miktar ve karakter yan yana getirilerek (5A gibi) yeni bir diziye eklenir.
B. Geri Açma (Decode) Mantığı
Ayrıştırma: Sıkıştırılmış dizideki rakamlar ve harfler birbirinden ayrılır.
Genişletme: Okunan rakam kadar yanındaki harf ekrana basılır. Örneğin 3B görüldüğünde, belleğe BBB yazılır.
Bu kodun çalışması için herhangi bir harici kütüphane (library) veya paket kurulumuna gerek yoktur. Sadece bilgisayarınızda Python 3.x sürümünün yüklü olması yeterlidir.
