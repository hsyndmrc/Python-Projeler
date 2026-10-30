
name = "Levent"
surname = "Ertuna"
age = 36

# {} simgesi koyarak .format yazıp argüman olarak yukarıda tanımlanmış değişkenleri verebiliyoruz.
print("My name is: {} {}".format(name,surname)) #My name is: Levent Ertuna


# Burada ise yapılan süslü parantez içerisine index vererek yer değiştirmesi yapabiliyoruz.
print("My name is: {1} {0}".format(name,surname)) # My name is: Ertuna Levent

#Burada ise takma ad kullanılarak süslü parantez içerisine n ve s değişkenlerinden birini atarsak hangisi ilk sıraya atandıysa o ilk olarak yazılır.
print("My name is: {n} {s}".format(n = name, s= surname))

# çoklu index exleme 
print("My name is: {} {}. I'm {} years old.".format(name,surname,age))

# Bir değişken birden fazla kez kullanılacaksa index numaraları ile yapılabilir.
print("My name is: {0} {1}. I'm {2} years old. {2}".format(name,surname,age))


number = 5 / 3

# Ondalıklı kısmı sadece 3 hane olarak göster (n:1.3)
print("the resutl is {n:1.3}".format(n = number))

# Python'a yeni gelen bir özellik. yukarıdaki formatlama olayının kısaltılmış ve kolay hali.
print(f"My name is {name} {surname} and I'm {age} years old.")