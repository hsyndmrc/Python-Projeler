# print(type(25 + 8)) # 25 ve 8 sayılarını int tipinde topladık ve sonuç int tipinde oldu. Ekrana <class 'int'> yazdırılır.
# print(type(25 - 8)) # 25 ve 8 sayılarını int tipinde çıkardık ve sonuç int tipinde oldu. Ekrana <class 'int'> yazdırılır.
# print(type(25 * 8)) # 25 ve 8 sayılarını int tipinde çarptık ve sonuç int tipinde oldu. Ekrana <class 'int'> yazdırılır.
# print(type(25 / 8)) # 25 ve 8 sayılarını int tipinde böldük ve sonuç float tipinde oldu. Ekrana <class 'float'> yazdırılır.
# print(25 + 8) # 25 ve 8 sayılarını int tipinde topladık ve sonuç int tipinde oldu. Ekrana 33 yazdırılır.
# print(25 - 8) # 25 ve 8 sayılarının int tipinde çıkardık ve sonuç int tipinde oldu. Ekrana 17 yazdırılır.
# print(25 * 8) # 25 ve 8 sayılarını int tipinde çarptık ve sonuç int tipinde oldu. Ekrana 200 yazdırılır.
# print(25 / 8) # 25 ve 8 sayılrını int tipinde böldük ve sonuç float tipinde oldu. Ekrana 3.125 yazdırılır. 



# print(type(47 / 6)) # / operatörü ile float tipinde bölme işlemi yaptık ve sonuç float tipinde oldu. ekrana <class 'float'> yazdırılır.
# print(type(47 // 6)) # // operatörü ile int tipinde bölme işlemi yaptık ve sonuç int tipinde oldu. Ekrana <class 'int'> yazdırılır.
# print(type(47 % 6)) # % operatörü ile int tipinde mod alma işlemi yaptık ve sonuç int tipinde oldu. Ekrana <class 'int'> yazdırılır.
# print(47 / 6) # / operatörü ile float tipinde bölme işlemi yaptık ve sonuç float tipinde oldu. ekrana 7.833333333333333 yazdırılır.
# print(47 // 6) # // operatörü ile int tipinde bölme işlemi yaptık ve sonuç int tipinde oldu. Ekrana 7 yazdırılır.
# print(47 % 6) # % operatörü ile int tipinde mod alma işlemi yaptık ve sonuç int tipinde oldu. Ekrana 5 yazdırılır.



# print((12 + 8) * 5 / 4) # Parantez içindeki işlemler önce yapılır. 12 + 8 = 20, 20 * 5 = 100, 100 / 4 = 25.0. Ekrana 25.0 yazdırılır.
# print(type((12 + 8) * 5 / 4)) # Parantez içindeki işlemler önce yapılır. 12 + 8 = 20, 20 * 5 = 100, 100 / 4 = 25.0. Ekrana <class 'float'> yazdırılır.

# print(7**2) # ** operatörü ile üs alma işlemi yaptık. yani karenin alanını bulduk.
# print(type( 7**2 )) # ** operatörü ile üs alma işlemi yaptık. Yani karenin alanını bulduk ve sonuç int tipinde oldu. Ekrana <class 'int'> yazdırılır.

# print(125 ** (1 / 3)) # ** operatörü ile üs alma işlemi yaptık. Bu şekilde yapmamızın nedeni 125 sayısının küp kökünü bulmak istememizdir.
# print(type(125 ** 1 / 3)) # ** operatörü ile üs alma işlemi yaptık. Bu şekilde yapmamızın nedeni 125 sayısının küp kökünü bulmak istememizdir ve sonuç float tipinde oldu. Ekrana <class 'float'> yazdırılır.   


# # indirimli fiyat hesaplama
# print((850 / 100) * 20) # Bu işlemde önce 850 sayısını 100'e böldük ve sonuç 8.5 oldu. Sonra bu sonucu 20 ile çarptık ve sonuç 170.0 oldu. Son olarak bu sonucu 0.1 ile çarptık ve sonuç 17.0 oldu. Ekrana 17.0 yazdırılır.
# print(type(850 / 100 * 20)) # Bu işlemde önce 850 sayısını 100'e böldük ve sonuç 8.5 oldu. Sonra bu sonucu 20 ile çarptık ve sonuç 170.0 oldu. Son olarak bu sonucu 0.1 ile çarptık ve sonuç 17.0 oldu. Ekrana <class 'float'> yazdırılır.

# # %10 vergili fiyat hesaplama
# print((850 / 100 * 20) * 10) # Bu işlemde önce 850 sayısını 100'e böldük ve sonuç 8.5 oldu. Sonra bu sonucu 10 ile çarptık ve sonuç 85.0 oldu. Ekrana 85.0 yazdırılır.
# print(type((850 / 100 * 20) * 10)) # Bu işlemde önce 850 sayısını 100'e böldük ve sonuç 8.5 oldu. Sonra bu sonucu 10 ile çarptık ve sonuç 85.0 oldu. Ekrana <class 'float'> yazdırılır.



# # Kişi Tanımlama
# name = "Sude"
# age = 23
# height = 1.60
# job = "Engineer"

# print(name, age, height, job) # Ekrana Sude 23 1.6 Engineer yazdırılır.
# print(type(name), type(age), type(height), type(job)) # Ekrana <class 'str'> <class 'int'> <class 'float'> <class 'str'> yazdırılır.

# urun = 75
# buyCount = 4
# result = urun * buyCount
# print(result) # Ekrana 300 yazdırılır.
# # kirwem bu veri tipinin olmasının amacı çünkü sayılas işlemler yapıyoruz. BU NASIL SORU AMK :D :D :D


# x = "120"
# y = "35"
# result = x + y
# print(result) # Ekrana 12035 yazdırılır. Çünkü x ve y değişkenleri str tipindedir ve + operatörü ile birleştirme işlemi yapılır.

# result2 = int(x) + int(y)
# print(result2) # Ekrana 155 yazdırılır. Çünkü x ve y değişkenleri int tipine dönüştürülmüştür ve + operatörü ile toplama işlemi yapılır.
# # Kirwem burada sonuçların farklı olmasının sebebi veri tipleridir. Biz ilk başta verimizi string olarak belirledik o yüzden çıktı olarak 12035 yazdı.
# # Fakat ikinci işlemde ise vermizi int tipine dönüştürdük ve normal toplama işlemi yaptık sonuç 155 oldu. Bu yüzden veri tipleri çok önemlidir.


# urun = 850
# indirim_orani = 0.20 # 20% indirim
# indirim = urun * indirim_orani # 20% indirim 
# vergi = 0.10 # 10% vergi
# indirimli_fiyat = urun - indirim
# indirimli_fiyat = indirimli_fiyat + (indirimli_fiyat * vergi) # 10% vergi

# result = indirimli_fiyat
# print(result) # Ekrana 748.0 yazdırılır. Çünkü 850 sayısının %20'si 170.0 ve 850 - 170 = 680.0 ve 680.0 + (680.0 * 0.10) = 748.0


# #Çalışan Tanımlama
# aylik_maas = 30000
# ek_kazanc = 4500
# aylik_gider = 12500

# toplam_kazanc = aylik_maas + ek_kazanc
# print("Toplam Kazanç:" , toplam_kazanc) # Ekrana Toplam Kazanç: 34500 yazdırılır.

# kalan_para = toplam_kazanc - aylik_gider
# print("Kalan Para:" , kalan_para) # Ekrana Kalan Para: 22000 yazdırılır.










# sayi1 = 25 # sayi1 adında değişken tanımladık ve bu değişkene 25 sayısını atadık.
# sayi2 = 10 # sayi2 adında bir değişken tanımladık ve bu değişkene 10 sayısını atadık.
# toplam_result = sayi1 + sayi2 # sayi1 ve sayi2 değişkenlerini topladık ve çıkan sonucu toplam_result değişkenine atadık.
# carpim_result = sayi1 * sayi2 # sayi1 ve sayi2 değişkenlerini çarptık ve çıkan sonucu carpim_result değişkenine atadık.
# print("Toplam Sonuç:" , toplam_result , "Çarpim Sonuç:" , carpim_result) # Ekrana Toplam Sonuç: 35 Çarpım Sonuç: 250 yazdırılır.

# urun = 10000
# indirim_orani = 0.25

# indirimli_fiyat = urun * indirim_orani
# print("Urunun indirimli fiyati: ", indirimli_fiyat) 

# name = "Sude"
# age = 23
# height = 1.60
# isStudent = True

# result = int(isStudent)
# result2 = float(age)
# result3 = int(height)
# # result4 = int(name)  Hata alırız. string integer'a dönüşmez
# print(result , result2, result3,)




# ------------------------------------------------------------- STRING METOTLARI ÖRNEK -------------------------------------------------------------

# Görev 1 — Ürün kodu çözümleme
# Kolay
# Bir teknoloji mağazasında ürünlerin kodları şu şekilde tutuluyor:
# urun_kodu = "TEL-2026-SAMSUNG"

# Python kullanarak aşağıdaki bilgileri elde et:
# 1. İlk üç karakteri alarak ürün kategorisini yazdır: TEL
# 2. Yıl bilgisini dilimleyerek yazdır: 2026
# 3. Son yedi karakteri alarak marka bilgisini yazdır: SAMSUNG
# 4. Ürün kodunu tamamen ters çevirerek ekrana yazdır.
# 5. Her işlemin neden o sonucu verdiğini yorum satırlarında açıkla.


# urun_kodu = "TEL-2026-SAMSUNG"

# # Burada 0 başlangıç indextir. Yani başlangıçtan itibaren al. Ama 3. index'i dahil etme dedik.
# print(urun_kodu[0:3])

# # değişkendeki 2026 sayısını yazdırma, değişkendeki 2026 yazısını diziye atma, ve type'ını gördük
# print(urun_kodu[4:8].split())
# print(urun_kodu[4:8])
# print(type(urun_kodu[4:8]))

# # SAMSUNG çıktısını verir. -7 ile tersten başlayarak -7. index'i bulur ve son değer vermediğimiz için sona kadar gider.
# print(urun_kodu[-7:])

# # başlangıç ve bitiş indexleri verilmedi. -1 ile artık değerini verdik. Ve bize yazıyı ters bastı.
# print(urun_kodu[::-1])





# Teknoloji mağazası — Ürün bilgi kartı
# Bir teknoloji mağazasında çalıştığını düşün. Elinde şu bilgiler var:
# Değişken	Değer
# urun_adi	"Samsung Galaxy S25"
# kategori	"Telefon"
# fiyat	42500
# stok	12
# indirim	0.15

# Senden istediklerim:
# 1. Bu beş değişkeni tanımla.
# 2. %15 indirim uygulayarak yeni fiyatı hesapla ve ayrı bir değişkende sakla.
# 3. .format() kullanarak ürün adını, kategorisini ve stok miktarını tek bir cümlede yazdır.
# 4. f-string kullanarak ürün adını, eski fiyatını ve indirimli fiyatını tek bir cümlede yazdır.
# 5. İndirimli fiyatı ekrana iki ondalık basamakla yazdır. Örneğin 36125.00 TL şeklinde.
# 6. Yaptığın işlemleri yorum satırlarında açıkla.


# urun_adi = "Samsung Galaxy S25"
# kategori = "Telefon"

# fiyat = 42500
# stok = 12
# indirim = 0.15

# # İndirim miktarı hesaplandı.
# indirim_miktari = fiyat * indirim

# # Ürünün tam indirimli hali hesaplandı.
# indirimli_fiyat = fiyat - indirim_miktari
# # print(indirimli_fiyat)



# # İlk kullanım bu şekilde String Formating
# print("Urun adi: {} Kategori: {} Urun Fiyati: {} Urun stok durumu: {}".format(urun_adi,kategori,fiyat,stok))
# # String Formating farklı kullanım
# print("Urun adi: {0} Kategori: {1} Urun Fiyati: {2} Urun stok durumu: {3}".format(urun_adi,kategori,fiyat,stok))
# # String Formatlama farklı kullanım.
# print("Urun adi: {a} Kategori: {k} Urun Fiyati: {f} Urun stok durumu: {s}".format(a = urun_adi,f = fiyat, s = stok, k = kategori))


# # String Formating yeni şekilde yazıldı.
# print(f"Urun adi: {urun_adi} Kategori:{kategori} Urun fiyati: {fiyat} Urun indirimli fiyati: {indirimli_fiyat}")

# # indirimli fiyatı gösterme sadece 2 ondalık basamağı olacak şekilde.
# print(f"{indirimli_fiyat:.2f}")






# ------------------------ ORNEK 3 
# musteri_adi = "   ahmet yılmaz   "
# sehir = "gaziantep"
# telefon = "0555-123-45-67"
# ariza = "Modem arızası, internet kopması"

musteri_adi = "   ahmet yılmaz   "
sehir = "gaziantep"
telefon = "0555-123-45-67"
ariza = "Modem arızası, internet kopması"

# Tanımlı olan değişkende başındaki ve sonundaki tüm boşlukları aldı.
print(musteri_adi.strip())

# Müşterinin adını soy adının baş harflerini büyük yaptık ve değişkenin başındaki sonundakş boşlukları sildik.
print(musteri_adi.title().strip())

# Şehir değişkeninindeki Tüm harfleri büyük yazdık.
print(sehir.upper())

# Telefon numarasındaki - işaretlerini kaldırdık.
print(telefon.replace("-",""))

# virgülü esas alarak ona göre parçalama yapar. Yani iki parçaya böldü. Dizi haline getirdi.
print(ariza.split(","))

