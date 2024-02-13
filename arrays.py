#diziler
sayilar = [100,200,300,"merhaba",True,15.5]
#programcılar saymaya 0 dan başlar
print(sayilar[0]) 
print(sayilar)

sayilar.append(400)
print(sayilar)

sayilar.remove("merhaba") #değere göre siler
print(sayilar)

sayilar.pop(2) #indexe göre siler (default son index)
print(sayilar)

add=[700,800,900]
sayilar.extend(add)
print(sayilar)

sayilar.clear() #listenin içini temizler
print(sayilar)