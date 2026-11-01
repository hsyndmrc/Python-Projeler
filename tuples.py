
# list1 = [1,3,5,13,3]

# thistuple = (1,2,"altı",False,2)
# thistuple2 = (1,4,"beş",True,2)

# print(type(list1))
# print(type(thistuple))


# print(list1[0])
# print(thistuple[0])
# print(thistuple[2])

# print(len(list1))
# print(len(thistuple))


# list1[0] = 6
# print(list1)

# list1.append(45)
# print(list1)

# print(list1.count(3))
# print(thistuple.count(2))

# print(thistuple + thistuple2)

# # listeyi tuple'a döüştürmek
# list2 = tuple([6,8,3,12])
# print(type(list2))
# print(list2)



# thistuple.append(45)
# print(thistuple)

# thistuple[0] = 7
# print(thistuple)
# thistuple[0] = 6
# print(thistuple)



# ======================================================== TUPLE ÖRNEK ========================================================


personel = ("Ahmet", "Yılmaz", 2001, "Fiber", "Gaziantep")

# Personelin adını ve soyadını ayrı ayrı yazdır.
# Personelin Doğum yılı
personel_ad = personel[0]
personel_soyad = personel[1]
personel_dogumY = personel[2]
print(f"Personelin Adı: {personel_ad} Personelin Soyadı: {personel_soyad}. Personel Doğum Yılı: {personel_dogumY}")

# Fiber bilgisinin kaçıncı indexte olduğunu bul.
fiber_index = personel.index("Fiber")
print(f"Fiber İndex Numarası: {fiber_index}")

# Gaziantep bilgisinin tuple içerisinde kaç kez geçtiğini bul
gaziantep_count = personel.count("Gaziantep")
print(f"Gaziantep Kelimesi {gaziantep_count} defa geçmektedir.")

# "Aktif", "Saha Ekibi" adında ikinci bir tuple oluştur ve personel ile birleştirerek yeni bir tuple elde et 
# Yeni Tuple'ı ve orijinal personel tuple'ını ayrı ayrı yazdır. Aralarındaki farkı gözlemle.
personel2 = tuple(["Aktif", "Saha Ekibi"])

# yeni_tuple = (personel, personel2)
yeni_tuple = personel + personel2
yeni_tuple_len = len(yeni_tuple)
print(f"Yeni Tuple:  {yeni_tuple} ve Uzunluğu: {yeni_tuple_len}")
print(f"""
                Personel1 Tuple'ı: {personel}        
                Personel2 Tuple'ı: {personel2}
                Yeni Oluşturulan Tuple: {yeni_tuple}
""")

