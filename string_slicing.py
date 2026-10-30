name = "Huseyin"
surname = "Ertuna"
age = "26"

print(name + surname)

text = "Benim adim " + name + " Soyadim: " + surname + "Yasim ise: "+ age + "."
print(text)

print(text[0]) # B
print(text[1]) # e
print(text[-1]) # .

# Sıfırıncı indexten başla ve 5. indexe kadar hepsini al demektir. !!! 5. index dahil değildir. !!!
print(text[0:5]) 

# 6'ıncı indexten başladı. 17'inci indexe kadar olan her veriyi aldı. Fakat 17. index dahil değil.!!1
print(text[6:17])

# Başlangıç indexi verilmedi. Verilmediği için 0'dan başlayarak 10. indexe kadar olanları aldı.
print(text[:10])

# Başlangıç indexi 10 olarak verdik. Burada ise başlangıç 10. idexten başlayaca ve sonuna kadar hepsini alacak
print(text[10:])

# Burada ise -20'nci indexten başladı ve -1'ince indexe kadar gitti. Negatif sayı ile ifade edilirse 0'ıncı index son karakterdir!!!!
print(text[-20:-1])

# Burada ise 0'ıncı indexten başladı ve 2'şer 2'şer atlayarak yazdırdı. 0 başlangıç indextir. 30 kaçıncı indexe kadar olacağını söyler. 2 ise artış miktarıdır.
print(text[0:30:2])

# Burada ise başlangıç ve bitiş indexleri belirtmedik. Bu demek oluyor ki başlangıçtan sonuca kadar 2'şer 2'şer atlayarak çıktı ver. 
print(text[::2])

# Burada ise veriyi bize tam tersten başalayarak çıktı verdi.
print(text[::-1]) # .62 :esi misaYanutrE :midayoS niyesuH mida mineB