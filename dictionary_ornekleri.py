

# urunler = {
#     100:{
#         "Ad" : "Modem",
#         "Stok" : 12,
#         "Fiyat" : 1750
#     },

#     101:{
#         "Ad" : "ONT",
#         "Stok" : 15,
#         "Fiyat" : 2200
#     },

#     102:{
#         "Ad" : "RJ45",
#         "Stok" : 50,
#         "Fiyat" : 25
#     },

#     103:{
#         "Ad" : "Splitter",
#         "Stok" : 20,
#         "Fiyat" : 150
#     }
# }

# indirim = 0.15
# # Müşteri 2 modem, 3 RJ45 ve 1 Splitter satın aldı.
# musteri_satin_alma = urunler[100]["Fiyat"] * 2 + urunler[102]["Fiyat"] * 3 + urunler[103]["Fiyat"]
# print(f"Müşterinin Ödeyeceği Tutar: {musteri_satin_alma}")

# stok_modem = urunler[100]["Stok"] - 2
# stok_rj45 = urunler[102]["Stok"] - 3
# stok_splitter = urunler[103]["Stok"] - 1

# genel_kalan_stoklar = [stok_modem,stok_rj45,stok_splitter]

# # Satılan ürünlerin stoklarını doğrudan urunler sözlüğünün içinde güncelle
# urunler[104] = {
#     "Modem" : urunler[100]["Stok"],
#     "RJ45" : urunler[102]["Stok"],
#     "Splitter" : urunler[103]["Stok"]
# }

# print(urunler)

# # Satılan Ürünlerin toplam tutarını hesapla
# musteri_satin_alma = urunler[100]["Fiyat"] * 2 + urunler[102]["Fiyat"] * 3 + urunler[103]["Fiyat"]
# indirim_miktari = musteri_satin_alma * 0.15
# indirimli_tutar = musteri_satin_alma - (musteri_satin_alma * indirim)
# print(f"Müşterinin indirimsiz Ödemesi gereken tutar: {musteri_satin_alma}. Müşteriye %10 indirim uygulandi. Ödenecek Tutar: {indirimli_tutar}")

# # Üç Tırnak f-string kullanarak satış raporu oluştur. Raporda satılan miktar, kalan stoklar, indirimsiz tutar, indirim miktarı ve ödenecek tutar bulunsun.

# print(f""" 
#         Müşteriye Satilan miktar: {stok_modem} / {stok_rj45} / {stok_splitter}
#         Kalan Stoklar: {genel_kalan_stoklar}
#         İndirimsiz Tutar: {musteri_satin_alma}
#         İndirim miktari: {indirim_miktari} 
#         Ödenecek Tutar: {indirimli_tutar}
# """)

# urunler[100]["Stok"] = urunler[100]["Stok"] - 1
# print(urunler[100]["Stok"])




malzemeler = ["Modem", "RJ45", "Splitter","Fiber Kablo","RJ45"]

personel = ("Ahmet", "Yilmaz", 2001, "Saha Ekibi")

stok = {
    "Modem" : 5,
    "RJ45" : 30,
    "Splitter" : 8
}



# Malzemeler listesindeki toplam eleman sayısını bul. Ardından listeye "ONT" ekle.

malzeme_toplam_eleman = len(malzemeler)
print(f"""Malzemeler Listesindeki Toplam Eleman Sayisi: {malzeme_toplam_eleman}""")

eklenecek_malzeme = "ONT"
malzemeler.append(eklenecek_malzeme)

# Güncellenen liste eleman sayısını tekrardan yazdırdık.
malzeme_toplam_eleman = len(malzemeler)
print(f"""       Malzeme listesine eklene Eşya: {eklenecek_malzeme}
                 Malzemeler Listesindeki Eleman Sayisi: {malzeme_toplam_eleman}""")



# Personel tuple'ından adı, soyadı ve ekibi ayrı ayrı ekrana yazdı.
personel_ad = personel[0]
personel_soyad = personel[1]
personel_ekip = personel[3]

print(f"""
        Personel Adi:{personel_ad}
        Personel Soyadi: {personel_soyad}
        Personale Ekibi: {personel_ekip}
""")

# Stok sözlüğündeki RJ45 miktarını 25 yap. Sonra update() kullanarak "ONT" : 4 bilgisi ekle

# RJ45 Yeni Stok durum güncellemesi. 
rj45_yeni_stok = 25
stok["RJ45"] = rj45_yeni_stok

# ONT bilgisi eklenmesi.
eklenen_cihaz = "ONT"
eklenen_cihaz_miktar = 45
stok.update({eklenen_cihaz : eklenen_cihaz_miktar})
print(f"""   RJ45 Stok bilgisi: {rj45_yeni_stok}
             Yeni Eklenen Cihaz: {eklenen_cihaz} 
             Yeni Eklenen Cihaz Miktar: {eklenen_cihaz_miktar}""")

# Stok Sözlüğünün yedeği alındı.
stok_copy = stok.copy()

# Silinecek Ürün Tanımlaması
silinecek_urun = "Splitter"
stok.pop(silinecek_urun)

print(f"""      Stok Sözlüğünden silinecek Ürün: {silinecek_urun}
                Stok Sözlüğünün Copy'si: {stok_copy}
                Stok Sözlüğünün Orijinal Hali: {stok}
""")

# Malzemeler listesini set'e dönüştürerek tekrar eden RJ45 değerini kaldır. Benzersiz malzeme sayısını bul.
# Set'e Dönüştürdük
malzeme_set = set(malzemeler)
malzeme_set_sayi = len(malzeme_set)
print(f"""
            Yeni malzeme Set Listesi: {malzeme_set} 
            Yeni Malzeme Set Listesi Uzunluğu: {malzeme_set_sayi}
""")


# GENEL BİLGİLER
print(f"""
                Personel Adi ve Ekibi: {personel_ad} {personel_soyad} {personel_ekip}
                Güncel Malzeme Listesi: {malzemeler}
                Güncel Malzeme SET Listesi: {malzeme_set}
                Güncel Stok Sözlüğü: {stok}
                Yedek Stok Sözlüğü: {stok_copy}
""")
