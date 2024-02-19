""" for i in range(1,12):
    print(i)  """

#start: döngü kaç sayısından başlasın (default 0)
#stop: döngü kaç kere tekrar etsin 
#step: döngü kaç kaç arttırılsın (default 1)
    
#kullanıcının vereceği üst limit ile alt limitten bu üst
#limite kaadar olan tüm çift sayıları ekrana yazdıralım.

""" forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))

for i in range(forRangeMin,forRangeMax+1):
    if i % 2 ==0:
        print(i) """

#kullanıcının girdiği sayılar arasındaki en büyüğünü bulan program
""" biggestValue= 0
for i in range(5):
    sayi = int(input(f"{i+1}. sayiyi giriniz"))
    if sayi > biggestValue:
        biggestValue = sayi

print(f"Girdiğiniz sayilar arasinda en büyük olani: {biggestValue}") """


""" sayilar =[]
for i in range(5):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz")))

#sayilar.sort(reverse=True) #desc oldu
#print(sayilar[0])
print(min(sayilar))
print(max(sayilar)) """

students = ["Ahmet","Tuba","Abdullah","Onur","Dilara"]
#length = uzunluk
print(len(students))

#break : ilgili döngünün o anda kırılmasını sağlar
for i in range(len(students)):
    if i>2:
        break
    print(f"{i+1}. Öğrenci: {students[i]}")

#continue : iterasyondaki current değeri atla bir sonraki değer ile devam et
for i in students:
    if i =="Tuba":
        continue
    print(f"Öğrenci: {i}")


i=0
while i<10:
    print("Merhaba")
    i+=2 