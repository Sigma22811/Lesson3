print ("Lesson3")

class Student: 2 usage
    def __init__(self,Name,Surname,Age):
        self.Name=Name
        self.Surname=Surname
        self.Age=Age
        print("create Sucsessfull")

    def print_student(self):
        print("Surname:",self.Surname,"\tName",self.Name, "\tAge:",self.Age)

Student1 = Student("Vitalik","Oxygen",42)

Student2 = Student( "Ramzes","Strela",25)

student1.print_student()

student2.print_student()