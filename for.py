
# sayilar = [1,3,6,8,12,16,25]

# # print(sayilar[0])
# # print(sayilar[1])
# # print(sayilar[2])
# # print(sayilar[3])
# # print(sayilar[4])
# # print(sayilar[5])

# # for i in sayilar:
# #     print(i)

# # for i in sayilar:
# #     print("Merhaba")

# # isimler = ["sinem","baris","mert","deniz"]

# # for isim in isimler:
# #     print(isim)


# # isim = "Huseyin"

# # for i in isim:
# #     print(i)

# _tuple = [(1,2),(3,4),(6,9)]

# for a,b in _tuple:
#     print(a,b)

# iller = {"01":"Ankara", "02":"Adiyaman", "03" : "Afyon"}

# # for x in iller:
# #     print(x)

# # for x in iller:
# #     print(iller[x])

# # Değerleri görürüz.
# # for x in iller.values():
# #     print(x)

#  # Key ve value olarak aldığımız için. En iyi kullanım anlaşılır olan bu.""
# for key,value in iller.items():
#     print(key,value)


# FOR DÖNGÜSÜ UYGULAMA 

arizalar = [{
    "musteri": "Ahmet",
    "tur" : "Fiber",
    "internet" : 0,},

    {   
    "musteri" : "Mehmet",
    "tur" : "DSL",
    "internet" : 1,
    },

    {
    "musteri" : "Ayse",
    "tur" : "Fiber",
    "internet" : 0 ,

    },
    {
    "musteri" : "Fatma",
    "tur" : "Modem",
    "internet" : 1,
    },
    

    {
    "musteri" : "Ali",
    "tur" : "DSL",
    "internet" : 0,
    }]

internet_olmayan_musteri_sayisi = 0

for ariza in arizalar:
    # print(ariza["musteri"])
    if ariza["internet"] == 0:
        print(ariza["musteri"],ariza["tur"])
        internet_olmayan_musteri_sayisi = internet_olmayan_musteri_sayisi + 1



print(f"İnterneti olmayan toplam musteri sayisi: {internet_olmayan_musteri_sayisi}")