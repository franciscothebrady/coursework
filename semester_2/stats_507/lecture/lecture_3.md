## 2024-01-22

### functional programming

### basics
- decompose a problem into a set of fucntions 
- functions only take inputs and produce outputs, and don't have any internal state that affects the output produced for a given input

### mapping over sequences
- perform an operation on every element of a list

```python
def my_map(f, seq):
    results = []
    for s in seq:
        results.append(f(s))
    return results

x = range(1, 10) # excluding 10
sqrts = my_map(math.sqrt, x)
# more pythonic
sqrts2 = list(map(math.sqrt, x))
```
- `map()` is a function that will apply a function to every element of a sequence

### filtering sequences
- maps a predicate function to every element of a list, retaining only those elements for which the predicate returns `True`

```python
def my_filter(pred, seq):
    results = []
    for s in seq:
        if pred(s):
            results.append(s)
    return results

def is_even(x):
    return x % 2 == 0

x = range(1, 10)
evens1 = my_filter(is_even, x)
# pythonic
evens2 = list(filter(is_even, x))
# max python
evens3 = [y for y in x if is_even(y)]
```

### reduce 
- takes a binary function and applies it to a sequence 

```python
def my_reduce(f, seq):
ret = f(seq[0], seq[1])
for s in seq[2:]: # from third element to the end
    ret = f(ret, s)
return ret

# python reduce
from functools import reduce
from operator import add
numbers = [1,2,3,4]
reduce(add, numbers)
```

### lambda expressions
- let you define functions without using a def statement 
- called inline functions or anonymous functions

```python
def my_square(x):
    return x **2

list(map(my_square, range(1, 10)))

# lambda
list(map(lambda x: x **2, range(1, 10)))

# functions are equivalent
```

### parts of lambda expressions
- `lambda` keyword: tells python that you're defining a lambda expression
- parameter list: the inputs to your function
- colon: separates the parameter list from the body of the function
- body: the expression that is evaluated and returned when the function is called

note:
- you can pass multiple arguments to a lambda expression
- you don't have to use return statements in lambda expressions
- you can assign/name lambda expressions
```python
f = lambda x: x+'goat'
f('cat')
# 'catgoat'
```

- you can also use lambda expressions as arguments to other functions
```python
(lambda x: 2*x)(21)
# 42
```

### quantifiers over iterables
- any: returns True if any element of the sequence is True
- all: returns True if all elements of the sequence are True

```python
any([False, False, True])
# True
all([False, False, True])
# False
```

### variable keyword arguments (**kwargs)
- you can define a function that can receive a variable number of keyword arguments
- `kwargs` is a dictionary that maps keyword names to values

```python
def do_something(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
```

### iterators
- we've seen how to use for loops, which have the syntax
```python
for x in iterable:
    # do something with x
```
types of iterables:
- strings
- lists
- tuples
- dictionaries
- sets

### iteraters
`iter()` function returns an iterator object
- `next()` method returns the next element in the sequence
- `StopIteration` exception is raised when there are no more elements in the sequence

### what a for loop does
these are roughyl equivalnt:
```python
for a in iterable:
    f(a) # do
```
```python
it = iter(iterable)
while True:
    try:
        a = next(it)
    except StopIteration:
        break
    f(a) # do
```
### iteration tools
- itertools library provides a number of useful functions for working with iterators
```python
import itertools
suits = "SpadesHeartsDiamondsClubs"
ranks = list(map(str, range(2, 11))) + list("JQKA")
card_deck = it.product(ranks, suits)
next(card_deck)
# ('2', 'S')
```

### generators
- special type of function that can return multiple values 

```python
def my_func(num):
    for i in range(10):
        num += i
        yield num

f = my_func(5)
next(f) # 6
next(f) # 7
next(f) # 8
```

### exceptions
- `StopIteration` is an exception that is raised when there are no more elements in an iterator
- unhandled exceptions cause your program to crash
- you can also create an exception using the `raise` keyword

```python
raise Exception("Helpful message")
```

### handling exceptions
- you can handle exceptions using the `try` and `except` keywords
- in python it's usually easier to try something and handle the exception than to check if something will work before trying it

```python
# permission
if can_do_thing():
    do_thing()
else:
    handle_error()
```
```python
# forgiveness
try:
    do_thing()
except NoCantDo:
    handle_error()
```

### types of exceptions 
```python
def srqt(x)
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)
```

### except clauses 
```python
# ideal
# specify type of error
try:
    do_thing()
except RuntimeError:
    handle_error()

# sometimes
# catch any error
try:
    complicated_function()
except:
    handle_error()

# never
# skip error
try:
    do_thing()
except:
    pass
```

### files 
- files are created with the special function `open()`
- the mode argument specifies how the file will be used
    - `r`: read only
    - `w`: write only
    - `a`: append only
- note: opening a file for writing erases whatever is already in the file

```python
# text mode, read only
open("file.txt", "rt")
# text mode, write
open("file.txt", "wt")
# text mode, append
open("file.txt", "at")
# binary mode, read only
open("data.dat", "rb")
# binary mode, write 
open("data.dat", "wb")
# binary mode, append
open("data.dat", "ab")
```
### combining lists
- `zip()` function takes two or more lists and returns a list of tuples
- given different length lists, `zip()` will only combine elements up to the length of the shortest list

```python
t1 = ['apple', 'banana', 'orange']
t2 = [1.99, 0.99, 2.99]
list(zip(t1, t2))
# [('apple', 1.99), ('banana', 0.99), ('orange', 2.99)]
for tup in zip([1,2,3], ['a', 'b', 'c'], 'xyz):
    print(tup)
# (1, 'a', 'x')
# (2, 'b', 'y')
# (3, 'c', 'z')
```

