'''Objective 
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, .
A string, .
An integer, .
An integer array (or vector) of test scores, .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading.png

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin: 
The first line contains , , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes .

Constraints

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80
Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
Explanation

This student had  scores to average:  and . The student's average grade is . An average grade of  corresponds to the letter grade , so our calculate() method should return the character'O'.'''


class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = sum(scores) / numScores

    def calculate(self):

        if self.scores >= 90 and self.scores <= 100:
            return "O"
        elif self.scores >= 80 and self.scores < 90:
            return "E"
        elif self.scores >= 70 and self.scores < 80:
            return "A"
        elif self.scores >= 55 and self.scores < 70:
            return "P"
        elif self.scores >= 40 and self.scores < 55:
            return "D"
        else:
            return "T"
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())  # not needed for Python
scores = map(int, raw_input().split())
print scores
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
