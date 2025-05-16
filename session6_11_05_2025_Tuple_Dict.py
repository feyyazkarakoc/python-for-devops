"""
Python'da bir nesne for döngüsüyle dolaşılabiliyorsa, ona iterable denir.
Örnek iterable'lar:
list, tuple, set, dict, str
range(10)
file nesneleri
Teknik olarak:
Bir nesne __iter__() metoduna sahipse (veya __getitem__()), Python onu iterable olarak kabul eder.

Java'da Iterable ne demek?
Tanım:
Java'da Iterable bir arayüzdür (interface) ve foreach döngüsünde kullanılabilen nesneleri tanımlar.
List sınıfı Iterable arayüzünü uygular. Bu yüzden for-each döngüsüyle gezilebilir.
Java’da iterable olan şeyler:
List, Set, Queue, Map.keySet()

Kendi sınıfını da implements Iterable diyerek iterable yapabilirsin.
public class MyIterable implements Iterable<String> {
    @Override
    public Iterator<String> iterator() {
        return List.of("x", "y", "z").iterator();
    }
}

Java’da Bir Sınıfın Iterable Olması İçin Ne Gerekir?
Bir sınıfın for-each döngüsünde kullanılabilmesi (yani iterable olması) için:
Iterable<T> arayüzünü implements etmelisin 
iterator() metodunu override etmelisin
"""







# Tuples: Türkçe demet
# () ile kullanılır
# tuple() metodu da var
# Değiştirilemez (immutable) veri yapısıdır.
# iterable'dır. Yani elemanlarına for döngüsü ile tek tek ulaşılabilir.

my_tuple = (1, 2, "3", "Hello", True)
print(my_tuple) # (1, 2, '3', 'Hello', True)
print(type(my_tuple)) # <class 'tuple'>

print(tuple("techpro education")) # ('t', 'e', 'c', 'h', 'p', 'r', 'o', ' ', 'e', 'd', 'u', 'c', 'a', 't', 'i', 'o', 'n')

name = "İbrahim"
print(tuple(name)) # ('İ', 'b', 'r', 'a', 'h', 'i', 'm')

print(tuple(1453)) # TypeError: 'int' object is not iterable önemli
# tuple() metodu iterable argüman alır (örneğin string, list, tuple, set, dict gibi)

print(tuple([1, 2, 3, 4])) # (1, 2, 3, 4) içine liste aldı tuple'a dönüştürdü

a = [1, 2, 3, 4]

b = tuple(a)

print(b) # (1, 2, 3, 4) listeyi tuple'a dönüştürdü

print(a[0]) # 1 list indexlenebilir
print(b[0]) # 1 tuple indexlenebilir
a[0] = 5
print(a) # [5, 2, 3, 4] list mutable

b[0] = 5 # tuple immutable # TypeError: 'tuple' object does not support item assignment

print(tuple(range(1, 20, 5))) # (1, 6, 11, 16) range() fonksiyonu ile tuple oluşturma

x = (1)
print(type(x)) # <class 'int'>

x = (1,)
print(type(x)) # <class 'tuple'>

print(tuple("techpro")) # ('t', 'e', 'c', 'h', 'p', 'r', 'o')

tuple_1 = "x", "y", 3, 1.5
print(tuple_1) # ('x', 'y', 3, 1.5) parantez kullanılmadığında da python tuple olareak olarak algılar
print(type(tuple_1)) # <class 'tuple'>

print(type(("hello",))) # <class 'tuple'>
print(type(("hello"))) # <class 'str'>

print(("Ayşe", "Uluğbek", "Mukaddes") + ("Ali",)) # ('Ayşe', 'Uluğbek', 'Mukaddes', 'Ali')
# Listelerde olduğu gibi toplama operatörü tuple'da da concat işlemi yayor.

print(("Ayşe", "Uluğbek", "Mukaddes") * 2) # ('Ayşe', 'Uluğbek', 'Mukaddes', 'Ayşe', 'Uluğbek', 'Mukaddes')


# Indexing

tuple_2 = (7, 8, "max", False, 234, [1 ,2 ,3], [5, 6, 7])

print(tuple_2[2]) # max
print(tuple_2[2][1]) # a

print(tuple_2[-1][2]) # 7

print("ali", "mehmet" + "ali") # ali mehmetali
print(type("ali", "mehmet" + "ali")) # TypeError: type() takes 1 or 3 arguments


print(("ali", "mehmet" + "ali")) # ('ali', 'mehmetali')
print(type(("ali", "mehmet" + "ali"))) # <class 'tuple'>

print(tuple_2) # (7, 8, 'max', False, 234, [1, 2, 3], [5, 6, 7])

# list mutable, tuple immutable. tuple içerisindeki listeye eleman ekleyebilir miyiz?
tuple_2[5].append(4)
print(tuple_2) # (7, 8, 'max', False, 234, [1, 2, 3, 4], [5, 6, 7])
print(type(tuple_2[5])) # <class 'list'> 5. eleman liste, listenin özelliklerini taşır

del tuple_2[3] # TypeError: 'tuple' object doesn't support item deletion # tuple immutable'dır.

del tuple_2[5][0]
print(tuple_2) # (7, 8, 'max', False, 234, [2, 3, 4], [5, 6, 7]) # 1 silindi, liste mutable

# Ama tuple'ı tamamen silebiliriz
del tuple_2
print(tuple_2) # NameError: name 'tuple_2' is not defined # tuple_2 silindi


# len

tuple_3 = (2, 4, [1, 2, 3], "Ayşe", "Fatma")
print(len(tuple_3)) # 5

print(len(tuple_3[2])) # 3

# index()

tuple_3.index("Ayşe") # 3

print((1, 2, 2, 3, 3, 3, 1, 3, 2, 1, 5, 6).index(1)) # 0  # verilen elemanın ilk gördüğü yerdeki indexini verir

# count()
print((1, 2, 2, 3, 3, 3, 1, 3, 2, 1, 5, 6).count(3)) # 4 # verilen elemanın kaç tane olduğunu verir

# Kullanıcıdan 2 tane nesne isteyin, girilen nesneler int ise bunların toplamını veren programı yazın.


# isnumeric() ile, en kapsamlısı isnumeric()
input_1 = input("Birinci nesneyi giriniz: ")

input_2 = input("İkinci nesneyi giriniz: ")

if input_1.isnumeric() and input_2.isnumeric():
        print(int(input_1) + int(input_2))
else:
        print("Lütfen sayısal bir değer giriniz.")

# isdigit() ile
input_1 = input("Birinci nesneyi giriniz: ")

input_2 = input("İkinci nesneyi giriniz: ")

if input_1.isdigit() and input_2.isdigit():
        print(int(input_1) + int(input_2))
else:
        print("Lütfen sayısal bir değer giriniz.")

# isdecimal() ile
input_1 = input("Birinci nesneyi giriniz: ")

input_2 = input("İkinci nesneyi giriniz: ")

if input_1.isdecimal() and input_2.isdecimal():
        print(int(input_1) + int(input_2))
else:
        print("Lütfen sayısal bir değer giriniz.")


# ord()  sayısal (ordinal) karşılığı verir.

print(ord("a")) # 97


# chr() ASCII'deki sayısal karşılığı verir.

print(chr(98)) # b


# Dictionaries 
# sözlük veya mapping ile karşımıza çıkıyor. {} ile kullanılır
# dict() metodu da var

"""
items() metodu, sözlükteki her bir key-value çiftini içeren tuple’lardan oluşan ve liste gibi görünen bir view object döndürür.
Bu nesne:
dict_items tipindedir.
İçerdiği her öğe: (key, value) şeklinde bir tuple’dır.
Görünüşte liste gibi davranır ama gerçek bir liste değildir (yani .append() gibi liste metodları yoktur).

view object Nedir?
Python'da sözlük metotları olan .items(), .keys() ve .values() birer view object döndürür.
View object, sözlüğün canlı (dynamic) bir görünümünü temsil eder.
Yani sözlük değiştiğinde view object de otomatik olarak değişir.
Örnek:
dict_1 = {"key1" : "value1", "key2": "value2"}
view = dict_1.items()
print(view)  # dict_items([('key1', 'value1'), ('key2', 'value2')])
dict_1["key3"] = "value3"
print(view)  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
Görüldüğü gibi dict_1 değişince view de değişti.
Bu canlı yapıya view object denir.
Bu çıktıda:
dict_items(...) → view object
İçindeki her ('key', 'value') → tuple

dict_items(...)
Bu, view object’in türünü belirtir.
dict_1.items() ifadesi çalıştırıldığında dönen özel tiptir: dict_items

[...] → Köşeli parantez
İçeride bir liste (Python'da list) var.
Yani bu dict_items nesnesi, görünüşte bir liste gibi davranıyor.

'key1', 'value1') → Normal parantezler
Bu bir tuple’dır.
"""

dict_1 = {"key1" : "value1", "key2": "value2", "key3": "value3"}
print(dict_1) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# dictionary'nin her bir öğesine item denir.
# items() metodu sözlükteki her bir öğeyi (key, value) şeklinde tuple olarak verir ve bu tuple'ları içeren bir view object döner.
# .items() çıktısı, doğrudan list() veya tuple() içine alınabilir.

print(dict_1.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])


"""
set-like object "Küme-benzeri nesne" demek. Yani bu nesne tıpkı bir set (küme) gibi davranır:
Tekrar eden elemanlar yok
Elemanlar sırasızdır
in operatörüyle sorgulama yapılabilir

providing a view on D's keys: "Sözlük D’nin anahtarlarına bir görünüm sağlar."
Bu, anahtarları kopyalamadan gösterdiğini anlatır. Yani bellek tasarrufu sağlar ve orijinal sözlük değişirse bu görünüm de güncellenir.      

dict.keys() ne döner?
dict_keys adlı özel bir nesne döner. Bu nesne:
set gibi davranır
iterable’dır (üzerinde döngü yapılabilir)
indexlenemez (örneğin d.keys()[0] yazılamaz, ama list(d.keys())[0] olur)
otomatik güncellenir (sözlük değişince bu görünüm de değişir)         

tam olarak bir set dönmez.
Ama set gibi davranan özel bir dict_keys nesnesi döner.
İstersen bunu sete dönüştürebilirsin:
set_of_keys = set(d.keys())  # artık gerçek bir set


dict.keys() ne döner?	dict_keys adında set-benzeri bir görünüm döner
Gerçek bir set mi?	Hayır, ama set(d.keys()) ile dönüştürülebilir
"""


print(dict_1.keys()) # dict_keys(['key1', 'key2', 'key3']) # sadece key'leri verir



