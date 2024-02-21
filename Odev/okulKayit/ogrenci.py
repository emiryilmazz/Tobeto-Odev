# ---Bir okul kayıt sistemi kodlayalım---
# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. 
# Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek 
# bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. 
# Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

class Student:
    def __init__(self, isim, soyisim,vize,final):
        self.isim= isim
        self.soyisim= soyisim
        self.vize=vize
        self.final=final
    
    def bilgi(self):
        print(f"Öğrenci Adı: {self.isim}, Soyadı: {self.soyisim}")
    
    def ortalamaHesaplama(self):
        ortalama= (self.vize*0.4) + (self.final*0.6)
        return ortalama
    
