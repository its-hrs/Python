#19011
#HARSH SAXENA
#Define a class Student to store his/her name and marks in 3 subjects.Use a class variable to store the maximum average marks
#of the class.Use constructor and destructor to initialize and destroy the objects

class Student:
    avg_max=0
    
    def __init__(self,name,mrk1=0,mrk2=0,mrk3=0):
            self.mrk1=mrk1
            self.mrk2=mrk2
            self.mrk3=mrk3
            if((mrk1+mrk2+mrk3)/3) > Student.avg_max:
               Student.avg_max=round((mrk1+mrk2+mrk3)/3,2)

    def calAvg(self):
        return round((self.mrk1+self.mrk2+self.mrk3)/3,2)

    def __del__(self):
        print("DESTRUCTOR CALLED !!")

            
def main():
    n=int(input("Enter the number of students: "))
    for i in range (n):
        name = input("Enter name of student: ")
        marks=eval(input("Enter marks in 3 subjects as a list(mrk1,mrk2,mrk3...): "))
        obj=Student(name, marks[0], marks[1], marks[2])
        print("Average marks of ",name," are: ",obj.calAvg())

    print("\nMaximum Average marks of class are: ",obj.avg_max)
    
if __name__ == '__main__':
    main()
        
'''
OUTPUT:
= RESTART: C:\Users\shiv\AppData\Local\Programs\Python\Python38-32\19011_StudentClass.py
Enter the number of students: 4
Enter name of student: Harry
Enter marks in 3 subjects as a list(mrk1,mrk2,mrk3...): 80,85,90
Average marks of  Harry  are:  85.0
Enter name of student: Hermione
Enter marks in 3 subjects as a list(mrk1,mrk2,mrk3...): 90,95,89
Average marks of  Hermione  are:  91.33
Enter name of student: Ron
Enter marks in 3 subjects as a list(mrk1,mrk2,mrk3...): 80,75,70
DESTRUCTOR CALLED !!
Average marks of  Ron  are:  75.0
Enter name of student: Draco
Enter marks in 3 subjects as a list(mrk1,mrk2,mrk3...): 80,75,91
DESTRUCTOR CALLED !!
Average marks of  Draco  are:  82.0

Maximum Average marks of class are:  91.33
DESTRUCTOR CALLED !!
DESTRUCTOR CALLED !!
>>> 
'''
