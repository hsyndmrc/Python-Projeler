
# iller = ["İstanbul" , "Ankara", "İzmir" , "Bursa"]
# sonuc = iller

# sonuc = iller[2]

# # 0'ıncı index iler 2'nci index arasındaki illeri gösterebiliriz.
# sonuc = iller[0:2]

# # 2'nci indexten başlayıp sona kadar gider.
# sonuc = iller[2:]

# # Başlangıç indexinden başlayıp 3'üncü indexe kadar gider
# sonuc = iller[:3]

# # Sonuncu indexi bastırır.
# sonuc = iller[-1]
# sonuc = iller[-3:-1]

# # 0'ıncı index değerini Tekirdağ ile değiştirdi. Yani istanbul yerine tekirdağ oldu
# iller[0] = "Tekirdağ"

# # Son indexi değiştirdik
# iller[-1] = "Balıkesir"

# # Bir listenin uzunluğunu bize gösterir. Int değer olarak veri gönderir.
# sonuc = len(iller)

# # Listeye yeni eleman eklemek için kullanılır. Birden fazla değer verebiliriz.
# sonuc = iller + ["Adana","Antalya"]

# # Listeden eleman silmek için kullanılır. del iller[0:3] aralıkta belirtebiliriz.
# del iller[0] 

# print(iller)

# ================================= LİSTE ÖRNEK =================================

ekipmanlar = ["Modem", "Fiber Kablo", "ONT", "RJ45", "Splitter"]

# Listenin ilk elemanını ve son elemanını ayrı ayrı yazdır.
print(ekipmanlar[0]) # ilk eleman
print(ekipmanlar[-1]) # Son eleman

# Listenin ilk 3 elemanını dilimleme yöntemiyle al.
print(ekipmanlar[0:3])

# Listenin Sonun "Krone" ve "Fiber Patch Cord" ekleyerek yeni bir liste oluştur ve yeni_ekipmanlar değişkenine ata
yeni_ekipmanlar = ekipmanlar + ["Krone","Fiber Patch Cord"]

# yeni_ekipmanlar liste uzunluğu 
print(len(yeni_ekipmanlar))

del yeni_ekipmanlar[2]

print(yeni_ekipmanlar)
print(ekipmanlar)