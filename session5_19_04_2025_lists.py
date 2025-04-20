
# Tekrar

# Kullanıcıdan bir sayı alınız.
# Sayının pozitif, negatif veya sıfır olup olmadığını ekrana yazdırınız.

sayi = int(input("Bir sayı giriniz:"))
if sayi > 0:
    print(f"Girdiğiniz sayi ({sayi}) pozitiftir.")
elif sayi < 0:
    print(f"Girdiğiniz sayı ({sayi}) negatiftir.")
else:
    print("Girdiğiniz sayı 0'dır.")

# Kullanıcıdan bir sayı alınız.
# Sayının tek veya çift olup olmadığını ekrana yazdırınız.

sayi = int(input("Bir sayı giriniz:"))

if sayi % 2 == 0:
    print(f"Girdiğiniz sayı ({sayi}) çifttir.")
else:
    print("Girdiğiniz sayı ({sayi}) tektir.")


# Kullanıcıdan bir karakter alınız.
# Karakterin büyük harf, küçük harf veya rakam olup olmadığını kontrol ediniz.

karakter = input("Lütfen bir karakter giriniz:")
if karakter.islower():
    print(f"Girdiğiniz karakter ({karakter}) küçük bir harftir. ")
elif karakter.isupper():
    print(f"Girdiğiniz karakter ({karakter}) büyük bir harftir.")
elif karakter.isnumeric():
    print(f"Girdiğiniz karakter ({karakter})  bir rakamdır.")
else:
    print(f"Girdiğiniz karakter ({karakter}) rakam ya da harf değil.")

# List Methods

# string veriler iterable ve immutable
# liste tipi veriler iterable ve mutable
# iterable:  index ile elemanlarına ulaşabiliyoruz

""" Python listelerinin özellikleri:

Sıralıdır – Elemanlar eklenme sırasını korur.

Değiştirilebilirdir – Liste içeriği sonradan değiştirilebilir.

Farklı veri tipleri içerebilir – Aynı listede sayılar, string’ler ve başka listeler olabilir.

Tekrar eden elemanlara izin verir – Aynı değer birden fazla kez bulunabilir.

İndekslenebilir – Her elemana sıfırdan başlayan indekslerle ulaşılabilir.

Dilimlenebilir – Belirli aralıktaki elemanlar seçilebilir (liste[1:3]).

Negatif indeksleri destekler – Sondan başlayarak erişim mümkündür (liste[-1]).

Dinamik boyutludur – Listeye eleman eklenebilir veya çıkarılabilir.

Birçok yerleşik metodu vardır – append(), remove(), pop() gibi metotlar listelerle çalışmayı kolaylaştırır.

Kapsayıcı (container) bir veri tipidir – Diğer veri yapıları (tuple, list, dict) içerebilir."""

 
liste = [1, 3, True, [1, 2, 3], "1.5", "max"]

print(liste[0]) # 1

print(liste[-1]) # max

print(liste[3]) # [1, 2, 3]

print(liste[3][2]) # 3

liste[1] = 5 # listeler mutable
print(liste) # [1, 5, True, [1, 2, 3], '1.5', 'max']

print(type(liste)) # <class 'list'>


# list()
a = list() # listeyi list() metodo ile de tanımlayabiliriz.
print(a) # []

liste_1 = list("techpro") # str'yi listeye çevirdi
print(liste_1) # ['t', 'e', 'c', 'h', 'p', 'r', 'o']

b = "Hello"
print(list(b)) # ['H', 'e', 'l', 'l', 'o']

# print(list(256)) # HATA TypeError: 'int' object is not iterable, list() metodu içine iterable veri verilmeli, string ya da liste gibi 
# print(list("Hello","word")) # HATA TypeError: list expected at most 1 argument, got 2, list() metoduna 1 parametre verilmeli

# len()
print(len(liste)) # 6 liste içindeki listeyi tek bir elemean olarak sayıyor

print(liste_1) # ['t', 'e', 'c', 'h', 'p', 'r', 'o']
print(len(liste_1)) # 7

print(len("techpro")) # 7

# noktaya ulaşmak istiyoruz
print(liste[4][1]) # '1.5' tırnak içinde yazılmıi demek ki türü string. O halde index kullanabiliriz.
print(list(liste[4])[1]) # ikinci yol

# 4. elemanı floata dönnüştürelim
x = float(liste[4])
print(type(x)) # <class 'float'>

liste_2 = [1, 2, 1, 4, 3, 3, 5, 12, 35, 2, 7, 61]
print(liste_2[2:11:3]) # [1, 3, 35] start:stop:step start dahil, stop dahil değil

print(liste_2[::5]) # [1, 3, 7]

print(liste_2[5:8]) # [3, 5, 12]

a = [1, 3, 5]
b = [2, 4, 6]
print(a + b) # [1, 3, 5, 2, 4, 6]

# append()

