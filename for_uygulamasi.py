
# malzemeler = [
#     {"urun" : "Fiber Kablo", "stok" : 15, "fiyat" : 250},
#     {"urun" : "Modem" , "stok" : 3, "fiyat" : 1200},
#     {"urun" : "ONT" , "stok" : 2, "fiyat" : 850},
#     {"urun" : "RJ45", "stok" : 40, "fiyat" :5},
#     {"urun" : "Splitter", "stok" : 4, "fiyat" :150}
# ]

# kritik_stok = 0

# # Butun malzemeler for ile dolaş
# for malzeme in malzemeler:
#     # Tüm malzemelere for ile baktık.
#     # print(malzeme)
#     if (malzeme["stok"] < 5):
#         # Stok miktarı 5'in altında olan malzeme listesi. 
#         print(f"""Stok miktari 5'in altinda olan malzemeler: {malzeme["urun"]}""")

#         print(f"Stok miktari kritik seviye olan malzemelerin degerleri: {malzeme['urun']},{malzeme['stok']}, {malzeme["fiyat"]}")
#         kritik_stok += 1

# print(f"Kritik seviyede olan malzeme miktari: {kritik_stok}")


# iller = {
#     "01" : "Adana",
#     "02" : "Adiyaman",
#     "06" : "Ankara",
#     "27" : "Gaziantep",
#     "34" : "İstanbul",
#     "35" : "İzmir",
#     "42" : "Konya"
# }

# sayac = 0

# # Şehirleri yazdırma
# for key,value in iller.items():
#     # print(key,value)
#     if (key == "27"):
#         print(f"27 Plakali Sehir: {value}")

#     if("a" in value or "A" in value):
#             print(f"İçerisinde 'a' veya 'A' olan Şehiler: {value}")
#             sayac += 1

# print(f"İçerisinde 'a' ya da 'A' Bulunan sehirlerin miktari {sayac}")






depo = {
    "Fiber Kablo": {"stok": 20, "fiyat": 150},
    "Modem": {"stok": 4, "fiyat": 1200},
    "ONT": {"stok": 8, "fiyat": 850},
    "Splitter": {"stok": 3, "fiyat": 200},
    "RJ45": {"stok": 50, "fiyat": 10}
}

depo_toplam_deger = 0
kritik_urun_sayisi = 0

for urun_adi, bilgiler in depo.items(): 
     # urunlerin içindeki stok ve fiyat çarpılarak her bir ürünün kaç olduğunun bulduk.
    urun_hesap = bilgiler["stok"] * bilgiler["fiyat"]
    depo_toplam_deger += urun_hesap

    print(f"""
                ============== DEPO RAPORU ==============
                Urun: {urun_adi}
                Stok: {bilgiler['stok']}
                Fiyat: {bilgiler['fiyat']}
                Urunun Toplam Degeri: {urun_hesap}
""")
    if (bilgiler["stok"] < 5):
        print("""
                Durum: KRİTİK STOK!!!        
""")


print(f"Deponun Toplam Degeri: {depo_toplam_deger}")


