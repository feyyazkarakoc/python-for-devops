
# Comparison Operators
# Karşılaştırma opratörleri boolean döndürür.

print(5 == 5)

print(9 == 2)

print(1 != 8)

print(2 != 2)

print(2 > 3)

print(2 < 5)

print(3 >= 2)

print(4 <= 3)

# Logical Operators
# Mantıksal operatörler boolean döndürür.
# and, or, not
# işlem önceliği: not > and > or

print(1 is not False) # True 
print(1 is True) # False # is operatörü nesne kimliğini (yani bellekteki yerini) karşılaştırır. 1 ve True eşit değerde olabilir ama aynı nesne değildirler.

print(1 == True) # True # == operatörü değerleri karşılaştırır. 1 ve True (1) değer olarak eşittirler.
print(1 != False) # True # != operatörü değerleri karşılaştırır. 1 ve False (0) eşit değerde değildirler.

print(0 is not False) # True

print(2 and 3 ) # 3 # Hepsi True olduğunda en sonuncuyu döndürür.
print(0 and 1000) # 0 # Gördüğü ilk False değeri yazdırır.
"""and ifadesi, bool sonucu döndürmek zorunda değildir. x and y ifadesi:
Eğer x False ise, sonucu x olur.
Eğer x True ise, sonucu y olur."""

print(1 and False and 0 and 5) # False

print(0 or 1) # İlk gördüğü True değeri döndürür. # 1
print(None or 5 or 0) # 5 # None False olarak döner
print(0 or False or None) # None # Hepsi False ise sonuncuyu döndürür.
print(None or 0) # 0 Önemli

print(2 or 0 or 9) # 2 # İlk gördüğü True ifadedeyi döndürür.

print("Bilsen" or [] and 0) # Bilsen # işlem önceliği: and > or

print(False or 9 and not 0) # True # işlem önceliği: not > and > or önemli

print([] or not 1 and 0) # False # işlem önceliği: not > and > or önemli

print(True or False and not 0 and 8 or False) # True # işlem önceliği: not > and > or 

print(not 0) # True # not önüne geldiği ifadenin tersini döndürür. 
print(not 1) # False # not operatörü, True ve False değerlerini tersine çevirir.

print('Mukaddes' or [])

print('To be' or not 'To be') # To be # not 'To be' ifadesi False döner. False or 'To be' ifadesi 'To be' döner.

print(0 != 0) # False # != operatörü değerleri karşılaştırır. 0 ve 0 eşit değerdedirler.

print(0 is not False) # True # is not operatörü nesne kimliğini (yani bellekteki yerini) karşılaştırır. 0 ve False eşit değerde olabilir ama aynı nesne değildirler.




# String methods


# input() # input() fonksiyonu, kullanıcıdan bir girdi alır ve çıktısı str olur.

input("Adınızı giriniz :")

isim = input("Adınızı yazınız : ")
print(isim)

yas = input("Yaşınızı yazınız : ")
print(type(yas)) # str döner.
print(yas) # str döner.

#10 yıl sonra kaç yaşında olacaksınız?
yas_10 = int(yas) + 10
print(f"Bugünkü yaşınız {yas}, 10 yıl sonra {yas_10} yaşında olacaksınız.") # int() fonksiyonu, str'i int'e çevirir. 
# f string metodu ile değişkenleri string içerisinde kullanabiliyoruz.

# Girilen sayının karesini hesaplayın
sayi = input("Bir sayı giriniz : ")
sayi = int(sayi)
karesi = sayi ** 2 
print(f"Girdiğiniz sayı {sayi}, bu sayının karesi {karesi}")

sayi_1 = float(input("Numara giriniz : "))
print(type(sayi_1)) # float döner.
print(sayi_1)

yas_1 = int(input("Yaşınızı giriniz : "))
print(f"Yaşınız {yas_1}, 10 yıl sonra {yas_1 + 10} yaşında olacaksınız.")


# lower()  metodu, stringi küçük harfe çevirir.

print("FEYYAZ".lower())

isim = "Miyase"
print(isim)
print(isim.lower())

x = "TECHPRO Education"
print(x.lower())
print(x)

"""String immutable olması şöyle düşünebilirsin:
Bir kağıda HELLO yazdın, ama o kağıda bir daha yazı yazamazsın.
Yeni bir kağıda hello yazarsın, sonra elindekini değiştirirsin."""

sehir = input("Yaşadığınız şehir : ")
print(sehir)

sehir_1 = input("Yaşadığınız şehir : ").lower() # String ifadeleri küçük harfe dönüştürür.
print(sehir_1)


# upper() String ifadeleri büyük harfe çevirir.

sehir_2 = input("Bir şehir giriniz : ")
print(sehir_2)
print(sehir_2.upper()) # String ifadeleri büyük harfe dönüştürür.
print(sehir_2.lower())

print("İZMİR".lower())

print("izmir".upper()) # IZMIR   python büyüttüğü zaman İngilizce karaktere göre büyütür.


# title() metodu, her bir sözcüğün ilk harfini büyük yapar.

print("birazdan mola vereceğiz.".title()) # Birazdan Mola Vereceğiz.

# capitalize() metodu, cümlenin ilk harfini büyük harf yapar.

print("python öğrenmek çok eğlenceli".capitalize()) # Python öğrenmek çok eğlenceli 
print("python öğrenmek çok eğlenceli".title()) # Python Öğrenmek Çok Eğlenceli

# swapcase() metodu, büyük harfleri küçük, küçük harfleri büyük yapar.

print("pytHON".swapcase()) # PYThon

