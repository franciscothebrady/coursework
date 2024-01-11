 ## 2024-01-10  Administrative stuff and introduction  

### admin stuff  

 Overview 
 - lecutres and readings linked in the syllabus
 - broadly:
    - weeks 1-5: core pytohn programming topics
    - weeks 5-13: databases, data science skills and tools (numpy, scipy, matplotlib, scikit-learn, spark & mapreduce)
    - weeks 13-14: OOP, deep learning

Course schedule: https://docs.google.com/document/d/1WnmD8Fm1_Gl-rxXp9msM4gJjrgYFcW-ftuy2WynfBKk/edit
TODO: check readings, follow instructions to download docker and other software.

Sickness:
- if you are sick, please do not come to class

Homework: 
- policy is lenient to allow for sickness and absences

grading: 
- 25% homework, 50% 2 midterms, 25% final project
- curve:
    - if you score 90% overall, you are guaranteed a grade of at least A-
    - if you score 80% overall, you are guaranteed a grade of at least B-

Homework advice: try to solve the problem yourself first. 

Problem sets: 
- there will be 10 problem sets 
    - get started early,
    - drop the 2 lowest scores
    - you are encouraged to discuss the problems with each other, use the internet
    - solutions that are elegant will get extra credit. 

getting help:
- post on piazza
- GSI office hours 
- professor office hours

Tips: 
- start early on the problem sets
- backup your work, use version control like github
- python is case sensitive
- office hours can be used for tech support or homework clarifications, but no hinst or guidance will be given. 

### introduction to python  

why python? 
- increasingly the language of data science (and deep learning)

what is python:  
- design philosophy: simple, readable code
- python syntax differs from R, java:
    - whitespace delimited 
    - limited use of brackets, semicolons, etc 

python is dynamically typed and interpreted. 

Running python:
several options for running python:
    - locally installed python interpreter
    - jupyter
    - google colab

your homeworks must be installed as jupyter lab notebooks but you should also be comfortable running python on the command line. 
installing juypter lab: https://jupyter.org/install
note: jupyter recommends Anaconda: https://www.anaconda.com/
but it's your choice whether to use anaconda or just download jupyter lab 

note: course has a docker container that you can use to run everything that you need for the course. 

jupyter lab:
- jupyterlab runs the interpreter in the background, passing it your input and printing the output to the screen.

dockerized jupyterlab 
for this class, i highly recommend usingthe docker container that we have created. 
[fill in later]

data types:
programs work with literal values, that come in different types: 
- the value 42 is an integer
- the value 3.14 is a float(ing point number)
- the value "bird" is a string
A variables type determines what operations we can and cannot perform on it:
- 2*3 makes sense, but what "cat"*"dog"? 

note: you do not have to declare the datatype, python will detect it automatically.

Duck typing: unlike some languages, you don't tell python the type of a variable when you declare it. This is often called "duck typing". (if it looks like a duck, quacks like a duck, it's a duck).
Other languages are "strongly typed" which means you need to set types before you declare a variable.

Type conversion: 
we can (usually) convert between types using the int(), float(), and str() functions.

```python
approx_pi = 3.14
type(approx_pi)
# float
pi_int = int(approx_pi)
# int
pi_int
# 3
int_from_str = int("1234")
type(int_from_str)
# int
int_from_str
# 1234
```

Expressions
- expressions act on values to produce new values
```python
col_means = [1,2,3,4,5]

```

Mathematical expressions:
- python supports the usual mathematical operators: +, -, *, /, %, **, //
- remainder (modulus) operator: %
- integer division: //
- exponentiation: **
- bitwise operators: &, |, ^, ~, <<, >>
    - 5 & 2 # 0
    - 5 in binary is 101
    - 2 in binary is 010
    - check link in slides for more explanation 

Boolean expressions: 
- True and False are the only boolean values (note uppercase)
```python
x = 1
y = 2
x == y # False
x != y # True
x < y # True
x > y # False
```

Variables
- variables are names that refer to values
- givin a value to a variable is called assignment
- variables may contain any combinations of letters, numbers, and underscores, but may not start with a number.
- some words are reserved and cannot be used as variable names (e.g. True, False, and, or, not, if, else, elif, for, while, etc)
```python
mystring = "hello"
pi = 3.14
number_of_planets = 9
# change value 
number_of_planets = 8
```

Types 
- find the data type using the type() function

Undefined variables
- variables must be declared

Strings
- strings = text values 
- python has built in support for strings
- define a script using either single, double, or triple quotes
```python
"I am a string"
# assign a string to a variable
name = "Roger Federer"
name
# 'Roger Federer'
```

Strings as sequences
- it's helpful to think of strings as an ordered sequence of characters
- the kth character can be accesed using the syntax string[k]
- negative indexing counts from the end of the string
- case insensitive

```python
name = "Roger Federer"
name[0]
# 'R'
```

string operations
- python has many built in string operations
- a few of the most useful:
    - .upper() and .lower() to change case
    - .replace() to replace one string with another 
    - .find() to find the index of a substring, or -1 if not found

> the dot notation indicated that these are **methods** being called on an **object** of **type** string.

note: strings are immutable, so you cannot change them in place. 

```python
name = "Roger Federer"
name.upper()
# 'ROGER FEDERER'
name.lower()
# 'roger federer'
name.replace("Roger", "Rafael")
# 'Rafael Federer'
name.find("Federer")
# 6
name.find("Nadal")
# -1
```

Functions
- we've already seen some examples of functions, like type(), int(), and str()
- function calls take the form: function_name(arg1, arg2, ...)
- a function takes zero or more arguments, does something, and returns a value

```python
import math
math.sqrt(4)
# 2.0
```

Defining functions
we can define our own new functions using the *def* keyword
```python
def i_like_pizza():
    print("I like pizza!")
```
- the function body is indented
- rules for function names are the same as for variables because functions are variables in python

# comments
- comments are lines that are ignored by the interpreter
- now emphasis is given to writing clean code that is self-documenting
- giving meaningful names for variables and functions make extensive comments less necessary

```python
# this is a comment
""" multi-line comments
are also possible
"""
```

Function arguments:
- function arguments are separated by a comma
- arguments can be named or unnamed
- named arguments can be given in any order
- unnamed arguments must be given in the order they are defined

Return values: 
- many functions you write will return a value for later use
- the return keyword is used to return a value from a function
```python
def multiply_by_two(x):
    "multiplies by 2"
    return 2 * x
multiply_by_two(5)
# 10
```

exercise: write a function that determines whether a number is even or false
```python
def is_even(x):
    return x % 2 == 0
is_even(4)
# True
```

Conditional Logic
- sometime we want to do different things depending on certain conditions 
- in python we use the if, elif, and else keywords to do this

```python
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

Exercise: [fill in later from ppt]
additional exercises: [fill in later from ppt]
installing docker: [review from ppt]