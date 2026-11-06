# Uygulama 1
# Kullanıcıdan veri alıyoruz. String olarak aldığımız için int() içine yazıp integer değerine çeviriyoruz. 
# sayi = int(input("Sayi giriniz: "))

# if (sayi > 0):
#     if(sayi % 2 == 1):
#         print("Girilen Sayi pozitif tek sayidir.")
#     else:
#         print("Girilen sayi pozitif fakat tek degil")
# else:
#     print("Girilen Sayi negatiftir.")


# Uygulama 2

# x = int(input("x sayisini giriniz:"))
# y = int(input("y sayisini giriniz:"))
# z = int(input("z sayisini giriniz:"))

# if (x > y) and (x > z):
#     print("X en Büyük sayidir.")
# elif(y > x) and (y > z):
#     print("Y En büyük sayi")
# elif (z > x ) and (z > y):
#     print("Z en büyük sayi")

# Uygulama 3

# isim = input("İsim: ")
# yas = int(input("Yas: "))
# egitim = input("Egitim: ")

# if (yas >= 18):
#     if (egitim == "lise" or egitim == "üniversite"):
#         print("Ehliyet alabilirsiniz")
#     else:
#         print(f"{isim} ehliyet alamazsiniz. Cünkü Egitim durumu yetersiz.")
# else:
#     print(f"{isim} ehliyet alamazsiniz. Cunku yasiniz tutmuyor")


# ariza_turu = input("Ariza türü Giriniz: ")
# internet_var = bool(int(input("İnternet Var ise 1, Yok ise 0'a basiniz: ")))
# musteri_tipi = input("Kurumsal mi Normal Musteri mi Yaziniz: ")

# if (ariza_turu == "Fiber" and internet_var):
#     print("Acil Fiber Arizasi!!!")
# elif(musteri_tipi == "Kurumsal"):
#     print("Kurumsal Müşteri Önceliği")
# else:
#     print("Normal Ariza kaydi")


# print(internet_var)



# =========================================== PYTHON GÖREV - 1 ---- SAHA ARİZA ONCELİK SİSTEMİ ===========================================
# Senaryo: Türktelekom saha ekibindesin. Yeni bir ariza kaydi geliyor. Programın arızanın durumuna göre hangi işlemi yapacağını belirleyecek. 

# 1. Kullanıcıdan üç bilgi al
# - ariza_turu → Fiber, DSL veya Modem
# - internet_var → 1 ise internet var, 0 ise yok
# - musteri_tipi → Bireysel veya Kurumsal

ariza_türü = input("Ariza turunuzu giriniz: ")
internet_var = int(input("İnternetiniz var ise 1'e, Yoksa ise 0'a basiniz: "))
musteri_tipi = input("Musteri tipinizi yaziniz: ")
teknisyen_ismi = input("Müdahele edecek Teknisyen: ")
musaitlik_durumu = int(input("Teknisyen Musait mi? 1 / 0"))


if (musteri_tipi == "Kurumsal" and internet_var == 0 and ariza_türü == "Fiber" and musaitlik_durumu == 1):
    print(f"Acil - Kurumsal ariza!!! Teknisyen Yonlendiriliyor: {teknisyen_ismi}: ")
elif (musteri_tipi == "Kurumsal" and internet_var == 0 and ariza_türü == "Fiber" and musaitlik_durumu == 0):
    print("Acil - Kurumsal ariza!!! Teknisyen Bekleniyor...")
elif (ariza_türü == "Fiber" and internet_var == 0 and musteri_tipi == "Bireysel"):
    print("Yüksel - Fiber baglanti arizasi")
elif (ariza_türü == "Modem" and internet_var == 1 and musteri_tipi == "Bireysel"):
    print("Düsük - Modem Kontrolü")
else:
    print("Normal - Standart ariza kaydi")