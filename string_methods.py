
yazi = "Benim adım Hüseyin Demirci. İstanbul'da yaşıyorum"

# Bütün harfleri büyük yapan bir methot
# sonuc = yazi.upper()

# Bütün harfleri küçük yapar
# sonuc = yazi.lower()

# Her kelimenin baş harfini büyük yapar.
# sonuc = yazi.title()

# Sadece içeriğin baş harfini büyük yapar.
# sonuc = yazi.capitalize()

# isLower() değişkenin içinde hepsi küçük harf mi diye bakıyor. True ya da False değer döndürür.
# sonuc = yazi.islower()

# Tüm karakterler büyük mü diye kontrol ediyor.
# sonuc = yazi.isupper()

# Başında ve sonunda olan space (boşlukları siler)
# sonuc = yazi.strip()

# cümleyi boşlukları baz alarak bir dizi haline getirdi.
# sonuc = yazi.split()

# cümleyi noktaları baz alarak ayırdı.
# sonuc = yazi.split(".") # ['Benim adım Hüseyin Demirci', " İstanbul'da yaşıyorum"]

# her bir harfin arasına tire (-) işareti koyarak bize çıktı verdi
# sonuc = "-".join(yazi)

# Metnin içinde parantez içinde yazdığımız içerik var mı yok mu onu kontrol eder. Yoksa hata mesajı gönderir. Varsa kaçıncı indexte olduğunu bize söyler
# sonuc = yazi.index("Hüseyin")

# başlangıcında bu harf ya da bu kelime var mı diye kontrol eder.
# sonuc = yazi.startswith("B") # true false değer döndürür.

# sonunda bu harf var mı yok mu diye kontrol eder.
# sonuc = yazi.endswith("a") # True False değer döndürür.

# İlk yazılan ifadeyi ikinci yazılan parametre ile değiştirir.
# sonuc = yazi.replace("İstanbul","bursa")

# Türkçe karakterleri ingilizce karakterler ile değiştirir. Çoklu kullanım bu şekildedir.
sonuc = yazi.replace("ı","i").replace("ş","s").replace("ü","u")



print(sonuc)