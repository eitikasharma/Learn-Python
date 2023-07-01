'''   Python 3.9

print("hello world")
print("hello")   
#Python is case sensitive
Print("hello")   #This is throw an error   NameError: name 'Print' is not defined. Did you mean: 'print'?

#Variables
name="Sweta"
age=23

name="aman"
age=19.0

is_adult= True  #true will throw error   NameError: name 'true' is not defined. Did you mean: 'True'?
print(name,age)

#Exercise:
first_name ="Tony"
last_name="Stark"
age=51
is_genius=True

print(first_name,last_name,age,is_genius)

#User Input

name= input("What is your name? ")
print("Hello " + name)

#Erercise:
e_name=input("What is Your name? ")
print("Hello "+e_name)
super_heroname= input("What is your superhero name? ")
print(e_name+"'s superhero name is "+ super_heroname)  

#Type Conversion

old_age=input("enter your old age: ")
new_age= old_age +2    #All inputs are stored as String by default
print(new_age)         #TypeError: can only concatenate str (not "int") to str

old_age=input("enter your old age: ")
new_age= int(old_age) +2     #used int() to convert String input to integer
print(new_age)               # float()    str()    bool()   

number= 18
print(float(number))   
a=input("Enter first number: ")
b=input("Enter second number: ")
sum= int(a) + int(b)
#print("The sum is" +sum)     #TypeError: can only concatenate str (not "int") to str
print("The sum is "+ str(sum))   

name="Tony Stark"

print(name.upper())  # TONY STARK

print(name.lower())  #tony stark

print(name.find('S')) #Returns index 5
print(name.find('z')) #Returns index -1 not present 
print(name.find('stark')) #Returns index -1 not present 

print(name.replace("Tony Stark", "Ironman"))  # Ironman
print(name)       #Tony Stark 

print('T' in name)  # True
print('m' in name)  #False
print("Ironman" in name)  #False 

#Operator

print(2+3) #5
print(9-2) #7
print(4*5) #20
print(5**2) #25 => 5*5
print(9/3) #3.0
print(9//3) #3
print(7%2) #1 

i=5;
i+=2;
print(i)  

#Operator Prescedence

#P – Parentheses.
#E – Exponentiation.
#M – Multiplication.
#D – Division.
#A – Addition.
#S – Subtraction.

result= 2 + 3 * 5  //17
result= (2 + 3) * 5 //25
print(result)       

#Comparison Operator

print(3 > 2) #True
print(3 == 2) #False
print(3 != 2) #True 

# Logical Operator

print ( 3>2 or 2>5) #True
print ( 3>2 and 2>5) #False
print (not 3>2 ) #False     

# Conditional 

age = 19
if age >=18:  
  print("You are an adult")    # you are an adult
  print("you can vote")        #you can vote

print("thank you")             #thank you

age = 16
if age >=18: 
  print("You are an adult")   
  print("you can vote")

print("thank you")        #thank you 

age = 16
if age >=18: 
  print("You are an adult")   
  print("you can vote")
elif age<18 and age>3:
  print("you are in school")        #you are in school
else:
  print("you are a child")

print("thank you")                  #thank you      


#Calculator

first = input("Enter first number: ")
second = input("Enter second number: ")
operator =  input("Enter operator (+,-,*,/,%): ")

if operator == '+' :
  print("Sum: "+ str(int(first)+int(second)))
elif operator == '-' :
  print("Subtract: "+ str(int(first)-int(second)))
elif operator =='*':
  print("Multiply: "+ str(int(first)*int(second)))
elif operator == '/':
  print("Divide: "+ str(int(first)/int(second)))
elif operator == '%':
  print("Remainder: "+ str(int(first)%int(second)))
else:
  print ("Please enter valid operator")

print("Thank You")                          


#Range

numbers=range(5)
print(numbers)     #range(0,5)  5 not included     


#Loop

While

i=1
while i<=5:
  print(i)
  i=i+1           # 1 2 3 4 5    

i=1                                  # *
while i<=4:                          # **
  print(i * "*")                     # ***
  i=i+1                              # ****    

i=1                                  #hello
while i<4:                           #hellohello
  print(i * "hello")                 #hellohellohello
  i+=1                                                     

i=5
while i>=0:
  print(i * "*")
  i-=1                                      

for item in range(5):
  print(item)                      # 0 1 2 3 4

for item in range(6):
  print(item +1)                  # 1 2 3 4 5 6

#List                Collection of datatypes                    

marks = [95, 98, 97, "maths"]
print(marks)                  #[95, 98, 97, 'maths']
print(marks[1])               #98
print(marks[-1])              #maths

print(marks[0:3])              #[95, 98, 97] 

marks = [95, 98, 97]
for score in marks:
  print(score)                #95 98 97

marks.append(87)
print(marks)                 #[95, 98, 97, 87]       

marks.insert(0,67)
print(marks)                 # [67, 95, 98, 97, 87]

print(95 in marks)          # True

print(len(marks))           #5          

marks = [95, 98, 97]

i=0
while i<len(marks):
  print(marks[i])         # 95 98 97
  i+=1

marks.clear()
print(marks)              #[]


# Break and Continue          

students = ["ram", "shyam", "kishan", "radha", "radhika"]

for s in students:
  if s =="radha":
    break;
  print(s)            # ram shyam kishan

for s in students:
  if s =="kishan":
    continue;
  print(s)           # ram shyam radha radhika     


# Tuple      immutable

marks =(89,87,93)
marks[0]=99       # 'tuple' object does not support item assignment 

marks =(89,87,93,92,87,56,34,76,89,67,87)
print(marks.count(87))     # 3
print(marks.index(87))     #1


# Set               unique elements                 

marks ={89,87,93,92,87,56,34,76,89,67,87}
print(marks)     # {34, 67, 76, 87, 56, 89, 92, 93}  unique

#print(marks[2])  #'set' object is not subscriptable

for score in marks: 
  print(score)      # 34 67 76 87 56 89 92 93          

# Dictionary      Key value pair

marks= {"english" : 97, "chemistry" : 78}

print(marks["chemistry"])      #78
print(marks)                   # {'english': 97, 'chemistry': 78}

marks["physics"]= 88
print(marks)                   #{'english': 97, 'chemistry': 78, 'physics': 88}

marks["english"] = 92
print(marks)                   #{'english': 92, 'chemistry': 78, 'physics': 88} 


#Functions

1. In-Build Functions         
int()  str()
2. Module Functions           
                            
import math
print(dir(math))          # prints all the available functions from math module  

from math import *

from math import sqrt
print(sqrt(25))          #5.0        

3. User defined Functions  

def print_sum(first,second):
  print(first+second)              #6

print_sum(2,4)

def print_sum(first,second=3):
  print(first+second) 

print_sum(2)                       #5  '''
