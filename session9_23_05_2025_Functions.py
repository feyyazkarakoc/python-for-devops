
# Functions

# def fonksiyon_ismi(parametre) :
#    işlemler

"""
Temel Yapı:
def fonksiyon_adi(parametre1, parametre2, ...):
    # Fonksiyonun yaptığı işlemler üçlü çift tırnak (""" """ veya ''' ''') içinde, docstring formatında açıkça yazılır
    return değer  # opsiyonel
"""

"""
Docstring'in Faydaları:
help() komutuyla bu açıklamaya erişebilirsin.
IDE'ler (VS Code, PyCharm, vb.) imleci fonksiyon üstüne getirince docstring’i gösterir.
Daha okunabilir ve sürdürülebilir kod sağlar.
Otomatik dökümantasyon araçları (Sphinx, pdoc, vs.) docstring üzerinden çalışır.
Python'da fonksiyonların içine docstring yazmak çok yaygındır,
Profesyonel projelerde neredeyse her fonksiyon, sınıf, modül böyle belgelenir.
Özellikle açık kaynak projelerde bu bir zorunluluk gibi uygulanır.


"""


def kare_al(x) : # doc string şeklinde fonksiyonun tanımı yazılır
    '''
    Girilen sayının karesini alan fonksiyon 
    '''
    return x ** x


print(kare_al(2)) # 4

help(kare_al)
"""
Help on function kare_al in module __main__:

kare_al(x)
    girilen sayının karesini alan fonksiyon

"""

def kare_al2(x) :
    print(x ** 2) 
# Bu satır ekrana karesini yazdırır ama  bu fonksiyon return kullanmadığı için, otomatik olarak None döner.


print(kare_al2(9))
"""
81
None

Fonksiyonlarda print → ekrana yazar.
return → çağırana değer döner.
"""

# return yok, bu çıktıyı bir yerde kullanamam
x = 5 + kare_al2(2) # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType', print none döndürür
print(x)

x = 5 + kare_al(2)
print(x) # 9 

print(type(print())) # <class 'NoneType'> 
# Fonksiyonlarda çıktının kullanılabilir olması için print yerine return tercih edilir

def topla(a, b) :
    return a + b

print()

