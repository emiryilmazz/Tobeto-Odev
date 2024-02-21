#nesne, obje, sınıf
class Human:
    #property,attribute=özellik nitelik
    # name="emir"
    # age=25

    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        print("yapıcı blok çalıştı")
    #davranışlar,method
    def age(self,age):
        return age
    
    def talk(self,message):
        print(message)

    def walk(self):
        print(f"{self.name} walking...")

human1=Human("emir",23) #instance ürettik
human1.talk("merhaba")
human1.walk()

#classların içerisinde bir fonksiyon tanımlıyorsak fonksiyonların ilk parametresi rezervedir=self
