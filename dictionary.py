# 34 => İstanbul
# 35 => İzmir

# sehirler = ["İstanbul","İzmir"]
# plakalar = [34,35]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index("İstanbul")])
# print(plakalar[sehirler.index("İzmir")])

# key - value dictionary kullanımı.
# plakalar = {"İzmir": 35, "İstanbul": 34}
# print(plakalar["İzmir"])
# print(plakalar["İstanbul"])

# # Sözlüğün içerisine eleman ekleme !!!!!!!!!!
# plakalar["Eskişehir"] = 26
# plakalar["Bursa"] = 16

# print(plakalar)

# urunler = {
#     100: {
#         "ÜrünAdi:" : "Monitör",
#         "ÜrünAçiklamasi:" : "16 Inch",
#         "GarantiSüresi:" : 3,
#         "Fiyat: " : [800, 944],
#     },

#     101: {
#         "UrunAdi: " : "SSD",
#         "UrunAciklamasi: " : "256 GB",
#         "GarantiSuresi: " : 2,
#         "Fiyati: " : [1500,1770],
#     }
# }

# sonuc = urunler[100]["Fiyat: "]

# tutar = urunler[100]["Fiyat: "][1] + urunler[101]["Fiyati: "][1]
# print(tutar)


# print(sonuc)


# print(type(urunler))


# print(type(plakalar))


# ================================================ DICTIONARY UYGULAMA ================================================ 

urunler = {
    100:{
        "Ad" : "Modem",
        "Stok" : 12,
        "Fiyat" : 1500
    },
    101: {
        "Ad" : "ONT",
        "Stok" : 8,
        "Fiyat" : 2200
    },
    102: {
        "Ad" : "RJ45",
        "Stok" : 50,
        "Fiyat" : 25
    }
}


# BÖLÜM - 1 => 

# # Ürün Kodu 100 olan ürünün yalnızca adını ekrana yazdır.
print(f"ürünün adi: {urunler[100]["Ad"]} ") 

# Ürün Kodu 101 olan ürünün stok miktarını yazdır.
print(f"Ürün Stok miktari: {urunler[101]["Stok"]}")

# Ürün Kodu 102 olan ürünün fiyatını yazdır.
print(f"Ürün Fiyatı: {urunler[102]["Fiyat"]}")

# BÖLÜM - 1 SONU => 

# Bölüm - 2 => 

# Modem ürününün fiyatını 1750 olarak güncelle

urunler[100]["Fiyat"] = 1750
print(f"Modem Yeni Fiyat: {urunler[100]["Fiyat"]}")

# ONT ürününün stok miktarını 15 olarak değiştir.
urunler[101]["Stok"] = 15
print(f"Ont Stok Sayısı: {urunler[100]["Stok"]}")

# Ürün kodu 103 olan yeni bir ürün ekle: adı: "Splitter", stok 20, fiyat 150
urunler["Ad"] = "Splitter"
urunler["Stok"] = 20
urunler["Fiyat"] = 150
print(urunler)

# Bölüm - 2  SONU=> 
