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


ariza_turu = input("Ariza türü Giriniz: ")
internet_var = bool(int(input("İnternet Var ise 1, Yok ise 0'a basiniz: ")))
musteri_tipi = input("Kurumsal mi Normal Musteri mi Yaziniz: ")

if (ariza_turu == "Fiber" and internet_var):
    print("Acil Fiber Arizasi!!!")
elif(musteri_tipi == "Kurumsal"):
    print("Kurumsal Müşteri Önceliği")
else:
    print("Normal Ariza kaydi")


print(internet_var)