# Learn-Python


Python Overview

-What is Python
* Python is a dynamically typed, General Purpose Programming Language that supports an object-oriented programming approach as well as a functional programming approach.
* Python is also an interpreted and high-level programming language.
* It was created by Guido Van Rossum in 1989.

-Features of Python
* Python is simple and easy to understand.
* It is Interpreted and platform-independent which makes debugging very easy.
* Python is an open-source programming language.
* Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
* It is possible to integrate other programming languages within python.

-What is Python used for
* Python is used in Data Visualization to create plots and graphical representations.
* Python helps in Data Analytics to analyze and understand raw data for insights and trends.
* It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
* It is used to create web applications.
* It can be used to handle databases.
* It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.


Installation & Getting Started

-Steps to Install Python:
1. Visit the official python website: https://www.python.org/
2. Download the executable file based on your Operating System and version specifications.
3. Run the executable file and complete the installation process.
   
Version:
After installation check the version of python by typing following command: ‘python --version’.

Starting Python:
Open Python IDE or any other text editor of your preferred choice. Let’s understand python code execution with the simplest print statement. Type the following in the IDE: 

print("Hello World !!!")
Now save the file with a .py extension and Run it. You will get the following output:
Output: Hello World !!!
 
Installing Packages:
To install packages in Python, we use the pip command. 
e.g. pip install "Package Name"

Following command installs pandas package in Python:
pip install pandas


Syntax

In simplest words, Syntax is the arrangement of words and phrases to create well-formed sentences in a language. In the case of a computer language, the syntax is the structural arrangement of comments, variables, numbers, operators, statements, loops, functions, classes, objects, etc. which helps us understand the meaning or semantics of a computer language.

For E.g. a ‘comment’ is used to explain the functioning of a block of code. It starts with a ‘#’.

For E.g. a block of code is identified by an ‘indentation’. Have a look at the following code, here print(i) is said to be indented with respect to the link above it. In simple words, indentation is the addition of spaces before the line "print(i)"
for i in range(5):
    print(i)


Python Comments
A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

Single-Line Comments:
To write a comment just add a ‘#’ at the start of the line.

Example 1:
#This is a 'Single-Line Comment'
print("This is a print statement.")
Output:   This is a print statement. 
 
Example 2:
print("Hello World !!!") #Printing Hello World
Output:   Hello World !!!
 
Example 3:
print("Python Program")
#print("Python Program")
Output:   Python Program

Multi-Line Comments:
To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

Example 1: The use of ‘#’.
#It will execute a block of code if a specified condition is true.
#If the codition is false than it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
Output:   p is greater than 5.

Example 2: The use of multiline string.
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
Output:   p is greater than 5.
