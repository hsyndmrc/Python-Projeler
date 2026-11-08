
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


iller = {
    "01" : "Adana",
    "02" : "Adiyaman",
    "06" : "Ankara",
    "27" : "Gaziantep",
    "34" : "İstanbul",
    "35" : "İzmir",
    "42" : "Konya"
}

sayac = 0

# Şehirleri yazdırma
for key,value in iller.items():
    # print(key,value)
    if (key == "27"):
        print(f"27 Plakali Sehir: {value}")

    if("a" in value or "A" in value):
            print(f"İçerisinde 'a' veya 'A' olan Şehiler: {value}")
            sayac += 1

print(f"İçerisinde 'a' ya da 'A' Bulunan sehirlerin miktari {sayac}")