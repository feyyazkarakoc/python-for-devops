
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



