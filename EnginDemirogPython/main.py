# sayi1=20
# sayi2=10
# if sayi1>sayi2:
#     print("Sayi 1 büyüktür sayı 2 den")

#f string
# vade=int(input("Vade sayısını giriniz:"))
# vade=vade+12
# print(f"Seçtiğiniz vade sonucu ortaya çıkan vade:{vade}")

# isim="Emir"
# metin="Merhaba"

# metin=f"Hoşgeldin {isim}"
# print(metin)

#listeler
krediler=["İhtiyac kredisi","Taşıt Kredisi","Konut kredisi"]
print(type(krediler))
print(krediler[0])
print(len(krediler))

dizi=["Kredi",10,4.4,True]
print(dizi)

#fonksiyonlar

#eleman ekleme append methodu ile içerisine aldığı değeri listenin son elemanına ekler
krediler.append("Özel Kredi")
print(krediler)
krediler.append("X Kredisi")
print(krediler)

#pop methodu ile defalut olarak listedeki son indexi siler. Silinecek index belirtilebilir.
krediler.pop(0)
print(krediler)

#remove methodu ile belirtilen değeri siler

krediler.remove("Taşıt Kredisi")
print(krediler)

#extend methodu ile birden fazla değeri tek satırda eklenebilir.
krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

#döngüler
#for
#range
for i in range(10):#range methodu default olarak içine yazılan değere kadar 1 er 1 er artar  
    print("aaa")
    print(i)
print("*****************************")
for i in range(5,10):#5 ile 10 arasında 
    print(i)

print("**********************")#ilk sayı kaçtan başlayacağı. 2. sayı kaça kadar saydıracağı. 3.sayı kaçar kaçar artacağını belirler
for i in range(0,51,10):
    print(i)
print("**********************")

krediler=["İhtiyac kredisi","Taşıt Kredisi","Konut kredisi"]
for kredi in krediler:
    print(kredi)
print("**********************")

for i in range(len(krediler)):
    print(krediler[i])
print("**********************")
#while
i=0
while i<10:
    print("x")
    i+=1
print("y")

print("**********************")

#break

while True:
    print("x")
    break

i=0
while i < len(krediler):
    if krediler[i]=="Konut kredisi":
        break
    print(krediler[i])
    i+=1
print("**********************")
#fonksiyonlar
#def definition define tanımlama
    
def calculate():
    print(200-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(100,56)
sayHello("Emir")
sayHello("Ahmet")
sayHello("İlknur")

#return eğer tekrar çağırıp bir işlem yapmak istiyorsak return kullanmalıyız
def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat=calculateAndReturn(200,50)
print(yeniFiyat+10)

print("**********************")

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return(price-discount)
print("**********************")
fonk1=calculatePrice(100,50)
fonk2=calculatePriceAndReturn(300,100)

print(f"126.Satır:{fonk1}")
print(f"127.Satır:{fonk2+200}")
print("**********************")
    

#sınıflar classlar
#modules
#paket yönetimi
#self> this ilgili fonksiyonun tanımlandığı nesnenin kendisini ifade ediyor her fonk için ilk parametre self parametresi ile rezerve edilmiştir.Bir parametrenin verilmesi zorunlu.

#sınıflar classlar
from human import Human
# instance =örnek  
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2= Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Emir").talk("Merhaba")

#modules

