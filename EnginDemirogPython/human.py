class Human:
    #built-in #constructor #initialize
    def __init__(self,name):#yapıcı blok
        self.name=name
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"Str fonksiyonundan dönen değer: {self.name}"#str fonksiyon çağırmak için kullanılır
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")