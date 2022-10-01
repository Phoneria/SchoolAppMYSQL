import mysql.connector
from datetime import date




mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "01.Ahmet",
    database= "schoolapp"

)

mycursor=mydb.cursor()

mycursor = mydb.cursor()

class Student:

    def __init__(self,Name,Surname,Birthdate,Gender,ClassID):
        mycursor.execute("SELECT MAX(ID) FROM student ")
        id = mycursor.fetchone()[0]+1

        mycursor.execute("SELECT MAX(StudentNumber) FROM student ")
        StudentNumber = mycursor.fetchone()[0]+10

        self.id = id
        self.StudentNumber = StudentNumber
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender

        mycursor.execute("Select ID from class ")
        all_classes = []
        for i in mycursor.fetchall():
            all_classes.append(i[0])

        if not ClassID in all_classes:
            self.ClassID = 1
            print("Student Added To First Class automatically.Because There Is No Class Like That")
        else:
            self.ClassID = ClassID

    def add_student(self):
        sql = "INSERT INTO student(ID,StudentNumber,Name,Surname,BirthDate,Gender,ClassID) VALUES (%s,%s,%s,%s,%s,%s,%s)"

        values = (self.id, self.StudentNumber, self.Name, self.Surname, self.Birthdate, self.Gender, self.ClassID)
        mycursor.execute(sql, values)
        print(f"{self.Name} {self.Surname} Is Just Added")




    @staticmethod
    def delete_student(id):
        try:
            mycursor.execute(f"Delete From student where ID ={id}")

            print(f"{id} Is Just Deleted")


        except:


            print("There Is No Student Like That")

    def __str__(self):
        return f'ID : {self.id}\nStudentNumber : {self.StudentNumber}\nName : {self.Name}\nSurname : {self.Surname}\nBirthdate : {self.Birthdate}\nGender : {self.Gender}\nClassID : {self.ClassID}'

class Teacher:
    def __init__(self,  Branch, Name, Surname, Birthdate, Gender):
        mycursor.execute("SELECT MAX(ID) FROM teacher ")

        self.id = mycursor.fetchone()[0] + 1
        self.Branch = Branch
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender


    def add_teacher(self):

        sql = "INSERT INTO teacher(ID,Branch,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s,%s)"

        values = (self.id, self.Branch, self.Name, self.Surname, self.Birthdate, self.Gender)
        mycursor.execute(sql, values)
        print(f"{self.Name} {self.Surname} Is Just Added")

    @staticmethod
    def delete(id):
        try:

            mycursor.execute(f"Delete From teacher where ID ={id}")
            print(f"{id} Is Just Deleted")
        except:
            print("There Is No Such ID")

    def __str__(self):
        return f'ID : {self.id}\nBranch : {self.Branch}\nName : {self.Name}\nSurname : {self.Surname}\nBirthdate : {self.Birthdate}\nGender : {self.Gender}\n'

class Lesson:
    def __init__(self,Name):
        mycursor.execute("SELECT MAX(ID) FROM lesson ")
        self.id =mycursor.fetchone()[0] + 1
        self.Name = Name

    def add_lesson(self):
        sql = "INSERT INTO lesson(ID,Name) VALUES (%s,%s)"

        values = (self.id,self.Name)
        mycursor.execute(sql, values)
        print(f"{self.Name} Lesson Is Just Added")



    @staticmethod
    def delete(id):

        try:
            mycursor.execute(f"Delete From lesson where ID ={id}")
            print(f"{id} Lesson Is Just Deleted")
        except:
            print("There Is No Such ID")

    def __str__(self):
        return f'Lesson Name : {self.Name} \nLesson ID : {self.id}'

class Class:

    def __init__(self,name,TeacherID):




        mycursor.execute("Select MAX(ID) from class ")
        id = mycursor.fetchone()[0]+1

        mycursor.execute("Select ID from teacher")
        holder =  mycursor.fetchall()

        p = []

        for i in holder:
            p.append(i[0])


        if TeacherID in p :

            sql = "INSERT INTO class(ID,Name,TeacherID) VALUES (%s,%s,%s)"
            values = (id,"12/E",4)
            mycursor.execute(sql, values)
            print(f"The Class Just Opened with {id} ID")

        else:

            print("There Is No Teacher Like That")

my = Class("12/E",2)



try:
    mydb.commit()
except mysql.connector.Error:
    pass

finally:
    mydb.close()
