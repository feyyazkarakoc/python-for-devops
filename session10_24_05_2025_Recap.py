
# 1 - Kullanıcıdan input ile iki veri alın. Alınan değerler aynı uzunlukta ise True döndüren algoritmayı yazınız.

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
sonuc = len(veri1) == len(veri2)
print(sonuc)

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
print(len(veri1) == len(veri2))

print(len(input("Birinci veriyi giriniz: ")) == len(input("İkinci veriyi giriniz: ")))

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
sonuc = True if len(veri1) == len(veri2) else False
print(sonuc)

veri1 = input("Birinci veriyi giriniz: ")
veri2 = input("İkinci veriyi giriniz: ")
if len(veri1) == len(veri2) :
    print(True)
else :
    print(False)

# 2 - Kullanıcıdan bir sayı isteyin. Sayı tek ise iki katını çift ise karesini yazdırın.
sayi = int(input("Bir sayı giriniz: "))
if sayi % 2 == 0 :
    print(f"Girdiğiniz sayı : {sayi}, Sonuç : {sayi ** 2}")
else :
    print(f"Girdiğiniz sayı : {sayi}, Sonuç : {sayi * 2}")

# 3 - Kullanıcıdan iki tam sayı isteyin. Sayılar eşitse veya sayıların farkı 5'in katı ise True döndüren algoritmayı yazınız.
sayi1 = int(input("Birinci tam sayıyı giriniz: "))
sayi2 = int(input("İkinci tam sayıyı giriniz: "))

if sayi1 == sayi2 or (sayi1 - sayi2) % 5 == 0 :
    print(f"Girdiğiniz sayılar : {sayi1, sayi2} Sonuç : ", True)
else :
    print(f"Girdiğiniz sayılar : {sayi1, sayi2} sonuç : ", False)


print(True if (sayi1 == sayi2) or ((sayi1 - sayi2) % 5 == 0) else False)

# abs() içine verilen ifadenin mutlak değerini döndürür

print(True if sayi1 == sayi2 or abs(sayi1 - sayi2) % 5 == 0 else False)


""" 4 - Vücut kitle indexini hesaplayan fonksiyonu yazınız. Hesapladığınız değerin hangi kategoride olduğunu belirtiniz. 
(vki = kilo / (boy ** 2))
VKI Aralıkları:
18.5'in altı: Zayıf
- 18.5 24.9: Normal kilolu
- 25 - 29.9: Fazla kilolu
- 30 - 39.9: Obez
- 40 ve üzeri: Aşırı obez """

def vki_hesapla(kilo, boy) :
    vki = kilo / (boy ** 2)
    if vki < 18.5 :
        aralik =  "Zayıf"
    elif 18.5 <= vki <= 24.9 :
        aralik = "Normal kilolu"
    elif 25 <= vki <= 29.9 :
        aralik =  "Fazla kilolu"
    elif 30 <= vki <= 39.9 :
        aralik =  "Obez"
    elif vki >= 40 :
        aralik =  "Aşırı obez"
    
    return vki, aralik
    
kilo = float(input("Kilonuzu giriniz (kg): "))
boy =  float(input("Boyunuzu giriniz (m): "))

vki, aralık = vki_hesapla(kilo, boy)
print(f"Vücut kitle indeksiniz: {vki: .2f} - Kategori : {aralık}")

# 5 - Kullanıcıdan bir cümle isteyin. Cümledeki büyük harf ve küçük harf sayısını hesaplayan bir program yazın.

def buyuk_kucuk_harf_say(cumle) :
    buyuk_harf, kucuk_harf = 0, 0
    for  harf in cumle :
        if harf.isupper() :
            buyuk_harf += 1
        elif harf.islower() :
            kucuk_harf += 1
    return buyuk_harf, kucuk_harf

cumle = input("Bir cümle giriniz: ")
print(buyuk_kucuk_harf_say(cumle))

cumle = input("Bir cümle giriniz: ")
kucuk_harf, buyuk_harf = 0, 0
for i in cumle :
    kucuk_harf += i.islower()
    buyuk_harf += i.isupper()
print(cumle)
print(f"Küçük har sayısı : {kucuk_harf}\nbüyük harf sayısı : {buyuk_harf}")
# f stringten önce format kullanılıyordu, şu an yaygın değil
print("Küçük harf sayısı : {0}\nBüyük harf sayısı : {1}".format(kucuk_harf, buyuk_harf))

# 5 - Kullanıcının girdiği kelimeyi tersten yazdıran bir fonksiyon yazınız

kelime = input("Bir kelime giriniz: ")
def my_reverse (kelime) :
    """Kullanıcının girdiği kelimeyi tersten yazdıran fonksiyon."""
    return kelime[::-1]

print(f"Girdiğiniz \"{kelime}\" kelimesinin tersi : {my_reverse(kelime)}")

# veya
kelime = input("Bir kelime giriniz: ")
print(f"Girdiğiniz \"{kelime}\" kelimesinin tersi : {''.join(reversed(kelime))}") # reversed() fonksiyonu, iterable döndürür bu yüzden join ile birleştirdik.
# join önünde "" kullanabiliriz, burada kullandığımızda pythonun kafası karışıyor, tek tırnak kullandık


# 5 - Girilen sayının faktöriyelini döndüren bir fonksiyon yazınız

def faktoriyel(sayi) :
    carpim = 1
    for i in range(1, sayi + 1) :
        carpim *= i
    return carpim

sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktoriyel(sayi)}")

def faktöriyel(sayi) :
    carpim = 1
    while sayi > 1:
        carpim *= sayi
        sayi -= 1
    return carpim

sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktöriyel(sayi)}")


def faktoriyel(n) :
    if n == 0 or n==1 :
        return 1
    elif n < 0 :
        return "Tanımsız"
    else :
        carpim = 1
        for i in range(1, n + 1) :
            carpim *= i
        return carpim
    
sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktoriyel(sayi)}")


def faktoriyel_recursive(sayi) :
    if sayi < 0 :
        return "Tanımsız"
    elif sayi == 0 or sayi == 1 :
        return  1
    return sayi * faktoriyel_recursive(sayi - 1)

sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} sayısının faktöriyeli : {faktoriyel_recursive(sayi)}")

# 5 - Palindrome bulalım
def palindrome(ifade) :
    return ifade == ifade[::-1]

print(palindrome("ey edip adanada pide ye"))

def palindrome(ifade) :
    return ifade == "".join(reversed(ifade))

print(palindrome("ey edip adanada pide ye"))

# 8 - Virgülle ayrılmış sayılardan oluşan bir string dizesi giriniz. Bu dizedeki tek sayıların karesini virgülle ayırarak yazdırınız.