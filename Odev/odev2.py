# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

# eleman1=1
# eleman2=1
# toplam=0 
# print(eleman1)

# for i in range(1,20):
  
#      print(eleman2) 

#      toplam=eleman1+eleman2 
#      eleman1=eleman2  
#      eleman2=toplam

# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

# sayi = int(input("Bir sayı girin: "))

# toplam = 0
# for i in range(1, sayi):
#     if sayi % i == 0:
#         toplam += i

# if toplam == sayi:
#     print(f"{sayi} Sayısı mükemmel sayıdır.")
# else:
#     print(f"{sayi} Sayısı mükemmel sayı değildir.")



# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

 
# sayiBir= int( input("Birinci sayıyı giriniz: "))
# sayiİki= int( input("İkinci sayıyı giriniz: "))  

# if ( sayiBir> sayiİki):
#      kucukSayi=sayiİki
# else:
#      kucukSayi=sayiBir

# for i in range(1,kucukSayi+1):
#      if( sayiBir % i ==0)  and (sayiİki % i==0):
#          ebob=i
#          ekok= (sayiBir*sayiİki)//ebob  

# print('ebob', ebob)
# print('ekok',ekok)


# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

# sayi = int(input("Bir sayı girin: "))

# if sayi > 1:
#     for i in range(2, sayi):
#         if (sayi % i) == 0:
#             print(sayi, "Asal Sayı Değildir.")
#             break
#     else:
#         print(sayi, "Asal Sayıdır.")
# else:
#      print(sayi, "Asal Sayı Değildir.")


# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

sayi = int(input("Bir sayı girin: "))

i = 2
print(sayi, "Sayısının asal çarpanları:")
while i <= sayi:
    if sayi % i == 0:
        print(i)
        sayi //= i
    else:
        i += 1
