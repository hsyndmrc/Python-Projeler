
# arabaAudi = {
#     "Marka" : "Audi",
#     "Model" : "A5",
#     "Yil" : 2019,
# }

# # Değerlere Erişme
# # sonuc = arabaAudi["Marka"]
# # sonuc = arabaAudi.get("Marka")


# # Sorgulama İşlemleri
# # Bu objenin içerisinde "Marka" var mı diye sorar. Boolean türünde cevap döndürür.
# # sonuc = "Marka" in arabaAudi

# # Bir objenin içerisinde kaç tane değer var
# # sonuc = len(arabaAudi)

# # Objeye Değer Ekleme
# arabaAudi["Renk"] = "Siyah"

# # Silme İşlemleri
# # arabaAudi.pop("Yil")

# # Objenin Son değerini siler 3.7'den önce herhangi bir elemanı siliyordu. Fakat python 3.7'den sonra son değeri siliyor!!!!!!!
# # arabaAudi.popitem()

# # del arabaAudi["Marka"]

# # Araba Audiyi siler Objeyi siler direkt
# # del arabaAudi

# # Obje silinmez içindeki değerler silinir. Del ile karıştırma
# # arabaAudi.clear()

# # Objeyi Kopyalama
# # araba = arabaAudi.copy()

# # araba["Marka"] = "Mercedes"

# # Değer Güncelleme
# arabaAudi.update({
#     "Marka" : "BMW",
#     "Renk" : "Beyaz"
# })
# print(arabaAudi)



arac = {
    "Marka" : "Ford",
    "Model" : "Courier",
    "Yil" : 2015,
    "Kilometre" : 177000
}

# get() Kullanarak aracın modelini yazdır.
araba_marka = arac.get("Model")
print(f"Aracin Modeli: {araba_marka}")

# "Renk" anahtarı var mı in ile kontrol et
araba_renk = "Renk" in arac
print(f"Sorguladiğiniz Renk Araçta {araba_renk}")

# "Renk" : "Beyaz" bilgisini ekle
arac_renk = arac.update({
    "Renk" : "Beyaz"
})
print(f"{arac.get("Marka")} {arac.get("Model")} Araç Bilgisi Güncellendi. Eklenen Yeni Bilgi: {arac.get("Renk")}. Güncellenen arac Bilgisi: {arac}")

# copy() kullanarak arac_yedek oluştur.
arac_yedek = arac.copy()


#update() ile orijinal aracın kilometresini 180000, Rengini siyah yap.
arac.update({
    "Kilometre" : 180000,
    "Renk" : "Siyah" 
})

print(f"""
            Orijinal arac bilgisi: {arac}
            Yedeklenmiş Arac Bilgisi: {arac_yedek}
""")