
personel = ("Ahmet", "Yilmaz", "Fiber")

malzemeler = ["Modem", "RJ45", "ONT", "Modem", "Splitter"]

stok = {
    "Modem" : 12,
    "RJ45" : 40,
    "ONT" : 8,
    "Splitter" : 5
}

kullanilan_modem, kullanilan_rj45, minimum_stok = 3, 7, 10

# PERSONEL BİLGİLERİ
# Tuple'dan personelin adını, soyadını ve çalıştığı alanı ayrı değişkenlere al.
personal_ad = personel[0]
personel_soyad = personel[1]
personel_alan = personel[2]

print(f"""
            Personelin Adi: {personal_ad}
            Personel Soyad: {personel_soyad}
            Personel Alan: {personel_alan}
""")


# DEPO STOK GÜNCELLEME
# Modem ve RJ45 stoklarından kullanılan miktarı -= opertörü ile düşür. Sonra güncel stokları yazdır.

stok["Modem"] -= kullanilan_modem
stok["RJ45"] -= kullanilan_rj45
print(f"""
            Guncel Stok: {stok}        
""")

# STOK KARŞILAŞTIRMASI
# Modem stokunun minimum_stok değerinden az olup olmadığını kontrol et. Aynı kontorlü RJ45 içinde yap. Sonuçları True False dönder
print(f"""
            STOK KONTROL:
            Modem Stok: {stok['Modem']}
            RJ45 Stok: {stok['RJ45']}
            
            MODEM STOK KONTROL:
            {stok['Modem'] < minimum_stok}

            RJ45 STOK KONTROL:
            {stok['RJ45'] < minimum_stok}
""")

# TEKRARLANAN MAZEMELERİ AYIKLA
# Malzemeler listesini SET'e dönüştür. Kaç benzersiz malzeme olduğunu bul.
malzemeler_set = set(malzemeler)
malzemeler_set_uzunluk = len(malzemeler_set)
print(f"""
            Malzemeler Listesinin Set edilmiş Hali: {malzemeler_set}
            Malzemeler listesinin Set Benzersiz Malzeme miktari: {malzemeler_set_uzunluk}
""")



print(f"""
               = PERSONEL BİLGİLERİ =
               {personal_ad}
               {personel_soyad}
               {personel_alan}

               = GÜNCEL STOK =
               Modem: {stok['Modem']}
               ONT: {stok['ONT']}
               RJ45: {stok['RJ45']}
               SPLITTER: {stok['Splitter']}

               = KARŞILAŞTIRMA SONUÇLARI =
               Modem Stok Kontrol:
               {stok['Modem'] < minimum_stok}

               RJ45 Stok Kontrol:
               {stok['RJ45']  < minimum_stok}
""")