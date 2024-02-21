#import mat as m >>> tüm modülleri kullanmak için hepsini import eder
from mat import topla as toplamaIslemi #sadece istediğimiz modülünü import etmek istersek
from human import Human as insan

#as > takma ad kullanmak için "alias"

#built in modules
import random
from selenium import webdriver
#package

#print(m.topla(10,30))
print(toplamaIslemi(10,30))

print(random.randint(0,100))#rastgele 0 ile 100 arasında sayı üretir
insan1=insan("Emir")
insan1.talk("Merhaba")

#packages

chromeDriver = webdriver.Chrome()