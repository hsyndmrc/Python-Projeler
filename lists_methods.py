
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

# isletme = "   ANADOLU TEKNİK SERVİS   "
# servis_sayisi = 8
# servis_birim_ucreti = 750
# malzeme_gideri = 1350
# ulasim_gider = 450
# vergi_orani = 0.10
# toplam_servis_geliri = servis_sayisi * servis_birim_ucreti
# malzeme_ulasim_gider = malzeme_gideri + ulasim_gider
# vergi_oncesi_kazanc = toplam_servis_geliri - malzeme_ulasim_gider
# net_kazanc = vergi_oncesi_kazanc - (vergi_oncesi_kazanc * vergi_orani)

# temiz_isim = isletme.strip()  # Başındaki ve sonundaki boşlukları kaldırır
# print(toplam_servis_geliri) # Toplam servis gelirini hesaplar
# print(malzeme_ulasim_gider) # Malzeme ve ulaşım giderlerini toplar
# print(vergi_oncesi_kazanc) # Vergi öncesi kazancı hesaplar
# print(net_kazanc) # Net kazancı hesaplar

# print(f""""
#     İşletme Adı:{temiz_isim}
#     Servis Sayısı: {servis_sayisi:.2f}
#     Servis Birim Ücreti: {servis_birim_ucreti:.2f}
#     Malzeme Gideri: {malzeme_gideri:.2f}
#     Ulaşım Gideri: {ulasim_gider:.2f}
#     vergi Oranı: {vergi_orani:.2f}
#     Toplam Servis Geliri: {toplam_servis_geliri:.2f}
#     Malzeme ve Ulaşım Gideri: {malzeme_ulasim_gider:.2f}
#     Vergi Öncesi Kazanç: {vergi_oncesi_kazanc:.2f}
#     Net Kazanç: {net_kazanc:.2f}
# """
# )

musteri = "   aHMET kAYA   "
telefon = "0532-456-78-90"
email = "AHMET.KAYA@GMAIL.COM"
ariza_kodu = "FBR-2026-0158"
adres = "gaziantep, şahinbey, karataş"
servis_ucreti = 1750
indirim_orani = 0.20
# Servis ücretine %20 indirim uygulandıktan sonra kalan ücreti hesaplar.
servis_ucret_indirimi = servis_ucreti - (servis_ucreti * indirim_orani)

# Müşteri adındaki gereksiz boşlukları kaldırır ve ad-soyad düzgün biçimlendir.
musteri_adi = musteri.strip().title()
# print(musteri_adi)

# Teelfon numarasındaki bütün - karakterlerini temizle
telefon_numarasi = telefon.replace("-","")
# print(telefon_numarasi)

# Email adresindeki boşlukları kadır ve tüm harfleri küçük yap.
email_adress = email.strip().lower()
# print(email_adress)

#Arıza kodundaki FBR, 2026, 0158 bilgilerini string dilimleme kullanarak ayrı değişkenlere ayır.
ariza_fbr = ariza_kodu[0:3]
ariza_yil = ariza_kodu[4:8]
ariza_no = ariza_kodu[9:13]

# print(f"Arıza Kodu: {ariza_fbr} Arıza Yılı: {ariza_yil} Ariza Numarası: {ariza_no}")

# Adres kelimelerini baş harflerini büyük olacak şekilde düzenle. Virgüller kalsın.
adres_duzeni = adres.title()
# print(adres_duzeni)

print(f"""  Müşteri Adı: {musteri_adi} 
            Telefon Numarasi: {telefon_numarasi}
            Email Adresi: {email_adress}
            Adres: {adres_duzeni}
            Arıza Kodu: {ariza_fbr}
            Arıza Yılı: {ariza_yil}
            Arıza Numarasi: {ariza_no}
            Servis Ucreti: {servis_ucreti:.2f}
            İndirim Orani: {indirim_orani:.2f}
            %10 İndirimli Ücret: {servis_ucret_indirimi:.2f}
""")
