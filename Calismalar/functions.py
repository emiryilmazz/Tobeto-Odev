#defination tanımlama
def ortalamaHesaplama():
    final=100
    vize=85
    ortalama=(vize*0.4)+(final*0.6)
    print(ortalama)

def ortalamaHesaplama2():
    final=100
    vize=85
    ortalama=(vize*0.4)+(final*0.6)
    return(ortalama)
#return ifadesi fonksiyonun çağırıldığı yere değer götürür

ortalamaHesaplama()
print(ortalamaHesaplama2())

def ortalamaHesapla3(vize:float,final:float):
    return (vize*0.4)+(final*0.6)

print(ortalamaHesapla3(86,45))