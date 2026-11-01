
# sayilar = [1,3,9,14,28,36,3]

# harfler = ["a","b","f","k","s","v","s"]

# # min ve max. int değer ise en küçük ve en büyük. harf ise min değer alfabetik sırada ilk gelendir. Max değer ise alfabetik olarak sırada en son gelendir.
# sonuc = min(sayilar)
# print(sonuc) 

# # sayılar listesinde max değeri verir.
# sonuc = max(sayilar)
# print(sonuc)

# # harfler dizisinde min değeri verir yani a çıktısı gelir
# sonuc = min(harfler)
# print(sonuc)

# sonuc = max(harfler)
# print(sonuc)


# # ekleme. Listenin sonuna ekler
# sayilar.append(20)
# print(sayilar)

# harfler.append("l")
# print(harfler)

# # Listede istediğimiz yere istediğimiz veriyi ekler. ilk yazılan index numarasıdır. Virgülden sonra yazılan ise değerdir.
# sayilar.insert(3,12)
# print(sayilar)
# harfler.insert(5,"e")
# print(harfler)

# # SİLME 
# # Listenin sonundaki elemanı siler
# sayilar.pop()
# print(sayilar)
# harfler.pop()
# print(harfler)

# # İstediğimiz bir veriyi silmemize yarar
# sayilar.remove(14)
# print(sayilar)

# harfler.remove("f")
# print(harfler)

# # Listelerde Sıralama işlemi

# # Sayılar dizisinin içindeki verileri küçükten büyüğe doğru sıralayacak
# sayilar.sort()

# # Harflerde ise alfabetik olarak yapar
# harfler.sort()

# print(sayilar)
# print(harfler)


# # Listeyi ters çevirmek için
# sayilar.reverse()
# print(sayilar)
# harfler.reverse()
# print(harfler)

# # Liste içerisinde bir elemandan kaç tane geçtiğini görmek istediğimizde 
# print(sayilar.count(3))
# print(harfler.count("s"))

# # Liste içerisinde arama yapmak ve kaçıncı indexte olduğunu bulmak
# print(sayilar.index(1))

# # Listeyi boşaltmak için
# print(sayilar.clear())


# # ======================================= LİST METHOT UYGULAMA =======================================
# malzemeler = ["Modem", "ONT", "Splitter", "Modem", "RJ45"]
# fiyatlar = [850, 1200, 75, 850, 30]

# # Malzemeler listesinde kaç tane "Modem" olduğunu bul.
# print(malzemeler.count("Modem"))


# # RJ45 malzemesinin indeksini bul
# print(malzemeler.index("RJ45"))

# # Listenin sonuna "Fiber Kablo" ekle
# sonuc = malzemeler.append("Fiber Kablo")
# print(malzemeler)

# # "ONT" ile "Splitter" arasına "CAT6" ekle
# malzemeler.insert(2,"CAT6")
# print(malzemeler)

# # Listedeki "RJ45" elemanını sil
# malzemeler.remove("RJ45")
# print(malzemeler)

# # Listenin son elemanını .pop() ile çıkar ve çıkarılan elemanı ayrı bir değişkende sakla
# cikarilan_eleman = malzemeler.pop()
# print(cikarilan_eleman)

# # Malzemeleri alfabetik sırala ardından ters çevir.
# malzemeler.sort()
# # Alfabetik sıralandı
# print(malzemeler)

# # Malzemeler ters çevrildi.
# malzemeler.reverse()
# print(malzemeler)

# print(min(fiyatlar))
# print(max(fiyatlar))

# malzemeler.sort()
# print(malzemeler)


# =========================================== LİSTE METOT UYGULAMA 3 ===========================================