class Student:
    def __init__(self,name,studentNumber) -> None:
        self.name=name
        self.studentNumber=studentNumber
        
    def doHomework(self):
        print(f"{self.name} is doing homework")
        
    
    def notStudy(self):
        print(f"{self.name} is not homework")

student1=Student("emir yılmaz",1020)
student1.name="ahmet"
student1.studentNumber=2020
student2=Student("İlknur",2024)
student1.doHomework()
student2.notStudy()