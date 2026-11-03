
# # list 
# # tuple 
# # Dictionary 

# # sets indexleme yapılamıyor, sıralanamaz. Değerler Değişmiyor. sıralama indexleme yapılmıyor. performans bakımından avantajlı. 


# markalar = {"Audi","Mercedes","BMW","Honda"}
# markalar2 = {"Renault","Toyota","Mazda"}

# # sonuc = markalar[0]
# # 'set' object is not subscriptable

# # Sorgulama
# # TRUE
# sonuc = "BMW" in markalar

# # Değer değişmez.

# # Yeni Eleman ekleme Sıralama olmadığı için random yere atar. Çünkü indexleme yapmaz bu liste türü
# markalar.add("Opel")

# # Birden fazla değer Eklenebilir.
# markalar.update(["Toyota", "Skoda"])


# # sonuc = len(markalar)

# # Değer Silme. Silmek istediğimiz değeri vermemiz gerekiyor.
# # markalar.remove("Opel")

# # Rastgele silme yapar.
# # sonuc = markalar.pop()

# # Liste içindeki tüm değerleri siler.
# # sonuc = markalar.clear()


# # 2 Tane set listesi olduğunda bunları birleştirebiliriz.
# sonuc = markalar.union(markalar2)

# print(sonuc) # {'Renault', 'Toyota', 'Opel', 'Mazda', 'BMW', 'Audi', 'Honda', 'Mercedes', 'Skoda'}

arizalar = ["FBR","DSL","ONT","FBR","MODEM","DSL","RJ45","ONT"]

# Listedeki tekrarlarını kaldırarak benzersiz arıza kodlarından bir set oluştur.

arizalar_set = {"FBR","DSL","ONT","MODEM","RJ45"}

# Kac farklı ariza türü olduğunu bul. 
ariza_tur_sayisi = len(arizalar_set)
print(f"{ariza_tur_sayisi} Adet Farkli Ariza Turu mevcut")

# FBR arizası var mı kontol et
fbr_varMi = "FBR" in arizalar_set
print(f"{fbr_varMi}")

# Yeni "SPLITTER" arızasını ekle
eklenen_ariza = "SPLITTER"
arizalar_set.add(eklenen_ariza)
print(f"Eklenen ariza: {eklenen_ariza}. Mevcut SET Listesi: {arizalar_set}")

# "RJ45" arizasini sil.
silinen_ariza = "RJ45"
arizalar_set.remove(silinen_ariza)
print(f"Silinen Ariza: {silinen_ariza}. Mevcut SET Listesi: {arizalar_set}")

print(f"""
            Ariza Listesi: {arizalar}
            Toplam Ariza Sayisi: {ariza_tur_sayisi}
            SET'lenmiş Ariza Listesi: {arizalar_set}
            FBR Kontrol: {fbr_varMi}
            Eklenen Ariza: {eklenen_ariza}
            Silinen Ariza: {silinen_ariza}

            Güncellenmiş SET Listesi: {arizalar_set}
""")