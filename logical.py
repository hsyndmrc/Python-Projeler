
# # And Operatörü

# x = 19
# # sonuc = 10 < x < 20

# sonuc = (x > 10) and (x < 20)

# # True ve True => True
# # True ve False => False
# # False ve False => False

# karne_notu = 60
# devamsizlik = 6

# sonuc = (karne_notu >= 50) and (devamsizlik < 10)

# # OR operatörü
# sonuc = (x < 10) or (x % 3 == 0)

# # Not 
# sonuc = not (x > 0)

# print(sonuc)



# ============================================================ ÖRNEK ============================================================

personel = ("Ahmet", "Yilmaz", "Fiber")

arizalar = ["FBR", "DSL", "FBR", "ONT", "DSL"]

stok = {
    "Modem" : 8,
    "RJ45" : 25,
    "ONT" : 3,
    "Splitter" : 5
}

minimum_stok = 5

modem_online = True
fiber_sinyali = False
teknisyen_onayi = True

# PERSONEL BİLGİLERİ
# Tuple içinden personel adını, soyadını ve çalışma alanını ayrı değişkenlere al. Ekrana düzenli şekilde yazdır.
personel_ad = personel[0]
personel_soyad = personel[1]
personel_alan = personel[2]

print(f"""       PERSONEL BİLGİLERİ:
                Personel Adi: {personel_ad}
                Personel Soyadi: {personel_soyad}
                Personel Alani: {personel_alan}
""")

# ARIZA KAYITLARI
# arizalar listesini bir set yapısına dönüştür. kaç farklı arıza türü olduğunu bul ve FBR arızasıbı in operatörü ile kontrol et.
# Arizalari set ettik baba
arizalar_set = set(arizalar)

# set edilen arizaların uzunluğu baba
arizalar_set_len = len(arizalar_set)
print(f"Arizalarin Set hali: {arizalar_set}. Kaç farkli ariza türü var: {arizalar_set_len}")

# ARiza kodlarının içinde "FBR" var mı yok mu onu gösterdik.
print("FBR" in arizalar_set)

# DEPO STOK KONTROL
# Depodan 2 modem ve 1 ont kullanıldı.
# -= operatörünü kullanarak stok sözlüğünü doğrudan güncelle.
# Ardından modem ve ONT stoklarının minimum_stok değerinden küçük olup olmadığını karşılaştır. Sonuçlar True veya False olsun.
alinan_modem = 2
alinan_ont = 1

stok["Modem"] =- alinan_modem
stok["ONT"] -= alinan_ont

print(f"Modem Stoklarinin minimum Kontrolü: {stok['Modem'] < minimum_stok}. ")
print(f"ONT Stoklarinin minimum Kontrolü: {stok["ONT"] < minimum_stok}")

# MANTIKSAL OPERATORLER
# Aşağıdaki kontrolleri ayrı değişkenlerde sakla:
# - Modem çevrimiçi ve fiber sinyali varsa bağlantı hazır mı?
# - Modem çevrimiçi veya fiber sinyali varsa en az bir bağlantı kontrolü olumlu mu?
# - Teknisyen onayı yoksa onay bekleniyor mu?

baglanti_hazir = modem_online and (not fiber_sinyali)
olumlu_kontrol = modem_online or (not fiber_sinyali)
isteknisyen_onayi_ = not teknisyen_onayi
print(f"""      
                Baglanti Hazir: {baglanti_hazir}
                Olumlu Kontrol: {olumlu_kontrol}
                Teknisyen Onay: {teknisyen_onayi}
""")