

# malzemeler = ["Modem","ONT","RJ45","Splitter","Modem"]
# fiyatlar = [850,1200,30,75,850]

# personeller = [
#             ["Ahmet", "Fiber", 25],
#             ["Mehmet", "Bakır", 30],
#             ["Ayşe", "Arıza Takip", 27]
# ]

# # ======================================================================== BOLUM 1 DEPO İŞLEMLERİ ========================================================================

# # Depoda Kaç adet "Modem" olduğunu hesapla
# modem_count = malzemeler.count("Modem")
# print(f"Depoda {modem_count} adet Modem bulunmaktadır.")

# # "RJ45" Malzemesinin kaçıncı indexte olduğunu bul.
# rj45_index = malzemeler.index("RJ45")
# print(f"RJ45 malzemesinin indexi: {rj45_index}")

# # Depoya "Fiber Patch Cord" Ekle
# depo_eklenen_malzeme = "fiber Patch Cord"
# malzemeler.append(depo_eklenen_malzeme)
# print(f"Depoya Eklenen Ürün: {depo_eklenen_malzeme}. Güncel Depo Listesi: {malzemeler}")

# # "Ont" ile "RJ45" arasına "CAT6 Kablo" ekle
# cat6 = "CAT6 Kablo"
# ont_index = malzemeler.index("ONT")
# print(f"ONT malzemesinin İndexi: {ont_index}")
# print(f"RJ45 malzemesinin İndexi: {rj45_index}")
# malzemeler.insert(ont_index + 1, cat6)
# print(f"Depoya Eklenen Ürün: {cat6}. Güncel Depo Listesi: {malzemeler}")

# # Splitter malzemesini depodan çıkar
# splitter_index = malzemeler.index("Splitter")
# splitter_index = malzemeler.pop(splitter_index)
# print(f"Depodan Çıkarılan Ürün: {splitter_index}. Güncel Depo Listesi: {malzemeler}")

# # Listenin sonundaki malzemeyi çıkar ve cikarlin_malzeme adlı değişkende sakla
# cikarilan_malzeme = malzemeler.pop()
# print(f"Depodan Çıkarılan Ürün: {cikarilan_malzeme}. Güncel Depo Listesi: {malzemeler}")

# # Güncel Malzemeleri Alfabetik sıraya diz ve kaç eleman kaldığını yazdır
# guncel_malzemeler = sorted(malzemeler)  
# print(f"Güncel Malzemeler Alfabetik Sırada: {guncel_malzemeler}. Depoda Kalan Malzeme Sayısı: {len(guncel_malzemeler)}")

# # ======================================================================== BOLUM 1 DEPO İŞLEMLERİ BİTİŞ ========================================================================



# # ======================================================================== BOLUM 2 PERSONEL İŞLEMLERİ ========================================================================

# # Mehmet'in yalnızca çalıştığı alanı ekrana Yazdır
# mehmet_alan = personeller[1][1]
# print(f"Mehmet'in Çalıştığı Alan: {mehmet_alan}")

# # Ayşe'nin sadece Yaşnı ekrana Yazdır.
# ayse_yas = personeller[2][2]
# print(f"Ayşe'nin Yaşı: {ayse_yas}")

# # Ahmet'in Yaşını 26 olarak Güncelle
# ahmet_guncel_yas = 26
# personeller[0][2] = ahmet_guncel_yas
# print(f"Ahmet'in Güncel Yaşı: {personeller[0][2]}")

# # Personeller Listesinin Tamamını ekrana yazdır. 
# print(f"Personellerin Listeri: {personeller}")

# # ======================================================================== BOLUM 2 PERSONEL İŞLEMLERİ BİTİŞ ========================================================================


# # ======================================================================== BOLUM 3 FİYAT ANALİZ İŞLEMLERİ ========================================================================

# # Fiyatlar listesindeki en düşük ve en yüksek fiyatı bul.
# en_dusuk_fiyat = min(fiyatlar)
# en_yuksek_fiyat = max(fiyatlar)
# print(f"Fiyatlar listesindeki en düşük fiyat: {en_dusuk_fiyat}, En yüksek fiyat: {en_yuksek_fiyat}")

# # Fiyatları Küçükten Büyüğe sırala
# sirali_fiyatlar = sorted(fiyatlar)
# print(f"Fiyatların Küçükten Büyüğe Sıralanmıi Hali: {sirali_fiyatlar}")

# # Fiyat Listesinin Eleman sayısını göster
# fiyat_sayisi = len(fiyatlar)
# print(f"Fiyatlar Listesinin Eleman Sayısı: {fiyat_sayisi}")

# # ======================================================================== BOLUM 3 FİYAT ANALİZ İŞLEMLERİ BİTİŞ ========================================================================

# # ======================================================================== BOLUM 3 FİNAL RAPORU ========================================================================
# print(f"""
#                     =========== FİNAL RAPOR ===========           
#                     Malzeme Listesi: {malzemeler}
#                     Fiyat Listesi: {fiyatlar}            
#                     Personel Listesi: {personeller}
#                     Depodan Çıkarılan Malzeme: {cikarilan_malzeme}
#                     Guncel Malzemele Listesi: {guncel_malzemeler}
#                     Fiyat Listesi: {sirali_fiyatlar}
#                     En Düşük Fiyat: {en_dusuk_fiyat}
#                     En Yüksek Fiyat: {en_yuksek_fiyat}
# """ )
