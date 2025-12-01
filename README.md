Student Average Marks Calculator (Python OOP)

This Python script demonstrates a simple use of Object-Oriented Programming (OOP) to calculate the average marks of different students.

📘 Overview

The script defines a Student class that stores:

The student's name

A list of their marks

The class also includes a method to calculate and display the student’s average score.

🛠️ How It Works
1. Class Definition
class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


__init__ initializes each student object with a name and a list of marks.

2. Average Calculation
def avg(self):
    sum = 0
    for i in self.mark:
        sum += i
    sum = sum / len(self.mark)
    print(f"Hy {self.name} your avg score is: {sum:.2f}")


Iterates through the marks list.

Computes the total and divides by the number of subjects.

Prints the average up to two decimal places.

👨‍🏫 Creating Student Objects & Displaying Results
s1 = Student("y", [99, 98, 90, 0, 0, 2, 5])
s1.avg()

s2 = Student("x", [100, 100, 100])
s2.avg()

s3 = Student("z", [-5, -10, 12])
s3.avg()


Each student object calls the avg() method to display its own average score.

📌 Example Output
Hy y your avg score is: 42.00
Hy x your avg score is: 100.00
Hy z your avg score is: -1.00

✨ Key Concepts Demonstrated

Object-Oriented Programming

Class definition and instance creation

Method implementation

List iteration

Basic arithmetic and formatted strings
