
a = 10 
b = 20
c = 30

a, b, c = 10, 2, 30

# Değerlerin yeri değişti.
a, b = b, a 

# Pratik Yöntem
# a = a + 5
# a += 5  # a = a + 5
# a -= 5 # a = a - 5
# a *= 5 # a = a * 5
# a /= 5 # a = a / 5

# a %= 5 # a = a % 5
# a **= 5 # a = a ** 5 
# a //= 5 # a = a // 5


sayilar = (1,2,3,4,5,6)

# a değerini alıyor, b değerini alıyor. *c ise geriye kalan değerleri liste şeklinde alıyor.
# a,b, *c = sayilar # 1 2 [3, 4, 5, 6]

# a yine değerini alacak c değerini alacak. *b ise geriye kalan değerleri alacak
# a, *b, c = sayilar # 1 [2, 3, 4, 5] 6

*a, b, c = sayilar # [1, 2, 3, 4] 5 6


print(a, b, c)