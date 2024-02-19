print("merhaba tobeto test ekibi")

#değişkenler

text="merhaba"
kullaniciAdi="emir"
print(text+kullaniciAdi)

studentCount="45" #string
studentCount1= 5 #int tam sayı

print(studentCount+"5")#455
print(studentCount1+5)#10

avaragePoint=25.5#double float decimal ondalıklı sayılar
print(avaragePoint+5)

isVerified= True #boolean
print(isVerified)

#Değişken isimleri öğrenme
print(type(text))
print(type(studentCount))
print(type(avaragePoint))
print(type(isVerified))

#matematiksel - mantıksal 

number =10
print(10+10)
print(number+number)

print(number-5)

print(number/2)

print(number*3)

print(number%3) #mod:sol taraftaki değerin sağ taraftaki değere bölümünden kalanı verir

#mantıksal öperatörler

print(number == 10) #true
print(number == 11) #false

print(number != 10) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

#string interpolation metin dönüştürme

text="merhaba"
kullaniciAdi="emir"
totalText=text+" "+kullaniciAdi
print(totalText)

totalText = " {message} Sayın {name} " . format ( message = "Hello" , name = kullaniciAdi )
print(totalText)

#f-string
totalText=f"Hoşgeldiniz {kullaniciAdi}"
print(totalText)