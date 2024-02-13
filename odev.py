#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
#github'a ekleme yapalım, linkleri paylaşalım lütfen 🙂


#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

print("Vücut kitle indeksi")
boy = float(input("Boy:"))
kilo = int(input("Kilo:"))
endeks = kilo /(boy*boy)
print("Vücut kitle endeksi",endeks)

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

print("Zamlı Maaş Hesaplama")
maas = float(input("Maaşı Giriniz (TL): "))
zam_orani = float(input("Zam Oranını Giriniz (%): "))
zamli_maas = maas + (maas * zam_orani / 100)
print("Zamlı Maaş:", zamli_maas, "TL")

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.


print("Üç adet tam sayı giriniz")
birinciSayi=int(input("birinci sayi: "))
ikinciSayi=int(input("ikinci sayi: "))
ucuncuSayi=int(input("üçüncü sayi: "))
enbuyukSayi=max(birinciSayi,ikinciSayi,ucuncuSayi)
print("En Büyük Sayı: ",enbuyukSayi)


#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

print("Dairenin yarı çapını giriniz ")
yariCap=float(input("Yarı çap değeri giriniz: "))
pi=3.14
daireAlani=pi*yariCap*yariCap
daireCevre= 2*pi*yariCap
print("Dairenin alanı: ",daireAlani)
print("Dairenin yarıçapı: ",daireCevre)

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
#github'a ekleme yapalım, linkleri paylaşalım lütfen 

sayi=(input("sayı giriniz:"))
tersten = ""
for rakam in sayi:
    tersten = rakam + tersten

print(tersten)

if tersten==sayi:
    print(sayi,"Sayısı Palindromdur")
else:
    print(sayi,"Sayısı Palindrom değildir")
  

