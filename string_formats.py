
name = "Levent"
surname = "Ertuna"
age = 36

# {} simgesi koyarak .format yazıp argüman olarak yukarıda tanımlanmış değişkenleri verebiliyoruz.
print("My name is: {} {}".format(name,surname)) #My name is: Levent Ertuna


# Burada ise yapılan süslü parantez içerisine index vererek yer değiştirmesi yapabiliyoruz.
print("My name is: {1} {0}".format(name,surname)) # My name is: Ertuna Levent

#Burada ise takma ad kullanılarak süslü parantez içerisine n ve s değişkenlerinden birini atarsak hangisi ilk sıraya atandıysa o ilk olarak yazılır.
print("My name is: {n} {s}".format(n = name, s= surname))
print("My name is: {} {}. I'm {} years old.".format(name,surname,age))