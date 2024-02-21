from ogrenci import Student
from ogretmen import Teacher

ogrenciListesi=[]
ogretmenListesi=[]

def addStudent(isim,soyisim,vize,final):
    
    newStudent=Student(isim,soyisim,vize,final)
    ogrenciListesi.append(newStudent)
    
    
def printStudent():
    for student in ogrenciListesi:
        student.bilgi()
        print(student.ortalamaHesaplama())

def addTeacher(isim,soyisim,bolum,maas,zamOrani):
    newTeacher=Teacher(isim,soyisim,bolum,maas,zamOrani)
    ogretmenListesi.append(newTeacher)

def printTeacher():
    for teacher in ogretmenListesi:
        teacher.bilgi()
        print(f"Zamli Maaş=", teacher.zamliMaas())



addStudent("Emir","Yılmaz",90,80)
addStudent("Kevser","Yılmaz",100,80)
addStudent("Ahmet","Suat",80,90)
addTeacher("Ozlem","Akman","Matematik",14000,30)
addTeacher("Nesibe","Kaya","Fizik",16000,20)


printStudent()
printTeacher()