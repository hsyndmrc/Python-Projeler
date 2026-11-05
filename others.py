# Identity Operatör: is

x = y = [1,2,3,4]
z = [1,2,3,4]

print(x == y)
print(x == z)

# Özdeşlik anlamında sorgu yaptık bu yüzden false oldu. 
print(x is z)
print( x is y)


# Membership Operator: in

a = ["python","javascript"]

# Türkçe meal: değişken değeri in(içinde mi?) değişkenin. Yani Bir değer var. Bu amk değeri bu değişkenin içinde var mı yok mu onu true false bize döndürüyor.
print("python" in a)
print("python2" in a)

email = "deneme@gmail.com"
print("@" in email) # True