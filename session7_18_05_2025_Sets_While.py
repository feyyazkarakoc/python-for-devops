
# Sets
# Türkçesi kümeler
# Unique değerler içeren (tekrarlı elemanlar kabul etmez) (unique), sıralaması olmayan (unordered), indexlenmeyen (indeksle erişilemez), mutable bir veri yapısıdır
# {} ve  set() metodu ile oluşturulur
# set() Fonksiyonu Python’daki yerleşik (built-in) bir fonksiyondur. Herhangi bir iterable'ı (liste, string, tuple vs.) alır ve bir kümeye (set) çevirir.

print(set("hello")) # {'e', 'o', 'l', 'h'} # tekrar eden l'yi almadı, sıralama yok

"""
Set içinde sadece hashlenebilir (değiştirilemez) türler olabilir.”
Bu, bir set'in içindeki elemanların sabit (değiştirilemez) olması gerektiği anlamına gelir.
Python’da set, elemanlarını benzersizliğe göre saklar. Bunu yaparken elemanların hash() değerini kullanır.
hash() fonksiyonu değişmeyen (immutable) türlerde çalışır.
 Set içine konabilecek türler:
int, float, str, bool, tuple (içinde değiştirilebilir bir şey yoksa)
Set içine konamayacak türler:
list, dict, set → çünkü bunlar değiştirilebilir (mutable) ve hashlenemez.
Örnek:
s = set()
s.add(10)       # int eklenebilir
s.add("abc")    # str eklenebilir
s.add((1, 2))   # tuple eklenebilir
s.add([1, 2])   # TypeError: unhashable type: 'list'

set yapısının kendisi değiştirilebilir (eleman eklenebilir, silinebilir),
ama içine konulan tek tek elemanlar değiştirilemez (sabit olmalı).
Yani:
set → değiştirilebilir (mutable)
içindeki elemanlar → değiştirilemez (immutable ve hashlenebilir)

Örnek:
s = set()
s.add("elma")    # ekledik
s.remove("elma") # çıkardık
# Ama içeriye liste koyamazsın çünkü list değişebilir:
s.add([1, 2])    # hata verir: çünkü list mutable

Kısaca Özet:
set yapısı	Değiştirilebilir (add, remove vs.)
Set’in içindeki elemanlar	Değiştirilemez ve hashlenebilir olmalı
Neden böyle?	Python set, elemanları hızlı karşılaştırmak için hash() kullanır
"""


"""
Python'da veri türleri, değiştirilebilir (mutable) ve değiştirilemez (immutable) olmak üzere iki gruba ayrılır. 
Bu ayrım, bir değişkenin bellekteki içeriğinin değiştirilip değiştirilemeyeceğini belirler.

Immutable (Değiştirilemez) Türler
Bu türlerde bir değer atandıktan sonra, içeriği değiştirilemez. Yeni bir değer vermek, aslında yeni bir nesne oluşturur.
Örnek immutable türler:
int (tam sayılar)
float (ondalıklı sayılar)
bool (True, False)
str (metinler)
tuple (demetler) – ama içindeki öğeler de immutable olmalı
frozenset (donmuş set)
bytes (byte dizisi)

Örnek:
x = 5
print(id(x))  # x'in bellekteki adresi
x = x + 1     # Yeni bir değer atandı
print(id(x))  # Farklı bir adres —> çünkü int immutable

Mutable (Değiştirilebilir) Türler
Bu türlerde, bir değişkene atanan veri yerinde (in-place) değiştirilebilir. Yeni nesne oluşturulmaz, aynı bellek adresinde değişiklik yapılır.
Örnek mutable türler:
list (liste)
dict (sözlük)
set (küme)
bytearray

Örnek:
my_list = [1, 2, 3]
print(id(my_list))  # Bellek adresi
my_list.append(4)
print(my_list)      # [1, 2, 3, 4]
print(id(my_list))  # Aynı adres —> çünkü liste mutable
"""

x = set()
print(x)
print(type(x)) # <class 'set'> # sadece set() ile boş bir set oluşturulur

y = {}
print(y)
print(type(y)) # <class 'dict'> # {} ile boş bir set oluşturulamaz, bu bir dict oluşturur

z = {1}
print(z)
print(type(z)) # <class 'set'> # 

print(set("techpro education")) # {'d', 'o', ' ', 'i', 'a', 'p', 'r', 'u', 'h', 't', 'n', 'c', 'e'} # tekrar eden harfleri almadı, boşluk karakterini de aldı, unordered sıraladı

set1 = {"blue", "green", "white", "magenta", "blue", "blue"} # dictioary'de de {} kullanıyorduk, python bu farkı anahtar : değer ile anlıyor
print(set1) # {'green', 'white', 'blue', 'magenta'} # tekrar eden elemanları almadı, unordered sıraladı
print(len(set1)) # 4 # tekrar eden elemanları almadı, sadece bir tane blue aldı, unique olmalı

set2 = {[1,2,3,5,4,2,3,4,7,9,8,6]} # TypeError: unhashable type: 'list' # list mutable olduğu için hata verir
set2 = set([1,2,3,5,4,2,3,4,7,9]) # set() ile listeyi set'e çeviriyoruz
print(set2) # {1, 2, 3, 4, 5, 7, 9} 
print(len(set2)) # 7

alfabe = "a b c d e f g".split() # defaultu boşluktu, boşluk karakterine göre ayırdık
print(alfabe) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # liste oluşturduk
set3 = set(alfabe) # set'e çeviriyoruz
print(set3) # {'e', 'b', 'f', 'g', 'd', 'a', 'c'}

print(set([1, True, False, 0, 1.0 , 0.0])) # {False, 1}  # True ve 1 aynı şey, False ve 0 aynı şey, 1.0 ve 1 aynı şey

# union(), intersection(), difference()

a = set("malatya")
b = set("kayısı")
print(a, b, sep = "\n")
# {'y', 'l', 't', 'm', 'a'}
# {'ı', 'y', 'k', 's', 'a'}

print(a - b) # a'nın b'den farklı olan elemanlarını getirir # {'m', 'l', 't'}
print(a.difference(b)) # a'nın b'den farklı olan elemanlarını getirir # {'m', 'l', 't'}

print(b - a) # b'nin a'dan farklı olan elemanlarını getirir # {'k', 's', 'ı'}
print(b.difference(a)) # b'nin a'dan farklı olan elemanlarını getirir # {'k', 's', 'ı'}

print(a.intersection(b)) # a ve b'de ortak elemanları getirir # {'y', 'a'}
print(b.intersection(a)) # a ve b'nin kesişim kümesini getirir # {'y', 'a'}
print(a & b) # a ve b'de ortak elemanları getirir # {'y', 'a'}

print(a.union(b)) # a ve b'nin tüm elemanlarını getirir # {'ı', 'y', 'l', 'k', 't', 'm', 's', 'a'}
print(b.union(a)) # a ve b'nin tüm elemanlarını getirir # {'ı', 'y', 'l', 'k', 't', 'm', 's', 'a'}
print(a | b) # a ve b'nin tüm elemanlarını getirir # {'ı', 'y', 'l', 'k', 't', 'm', 's', 'a'}

c = set("fındık")
d = set("fıstık")
print(c, d, sep = "\n")
# {'ı', 'f', 'k', 'n', 'd'}
# {'ı', 'f', 'k', 't', 's'}
print(c - d) # {'d', 'n'}
print(d - c) # {'s', 't'}
print(c - d | d - c) # {'d', 's', 't', 'n'}
print((c | d) - (c & d)) # {'d', 's', 't', 'n'}

print(a, b, c, d, sep = "\n")
"""
{'y', 'l', 't', 'm', 'a'}
{'ı', 'y', 'k', 's', 'a'}
{'ı', 'f', 'k', 'n', 'd'}
{'ı', 'f', 'k', 't', 's'}
"""

print(c.intersection(d) - d.union(c)) # set()
# boş kümeyi göstermek için set() yazılır, {} değil. {} boş bir sözlük (dictionary) anlamına gelir.
print(d.union(c) - (c.intersection(d))) # {'d', 's', 't', 'n'}

print(a.difference(b).difference(c)) # {'m', 'l', 't'}
print(a.difference(b).difference(d)) # {'m', 'l'}

# clear()

a.clear()
print(a) # set()

# remove()

print(b) # {'ı', 'y', 'k', 's', 'a'}
b.remove("a")
print(b) # {'ı', 'y', 'k', 's'}

b.remove("i") # KeyError: 'i' # remove() verilen eleman yoksa hata verir
# bu hatayı almamak için discard() kullanabiliriz
b.discard("i") # verilen eleman yoksa hata vermez
print(b) # {'ı', 'y', 's'} 

# pop()

set1 = set("selam")
print(set1) {'e', 'l', 'm', 's', 'a'}
