## 2024-01-17

### sequences
any object that supports:
- s[i]: i'th element of s, origin 0
- s[i:j]: slice of s from i to j
- len(s): length of s
- can be used in an iteration

### common sequences
- string
    - "i am a string"
- list
    - [1, 2, 3, 4]
- tuple
    - (1, 2, 3, 4)

### slicing
- a segment of a python sequence is called a slice
- seq[m:n] returns the subsequence:
    seq[m], seq[m+1], ..., seq[n-1]
- seq[:n] == seq[0:n]
- seq[m:] == seq[m:len(seq)]
- negative indices count from the end of the string
    - Note: does not contain right-most index

### advanced slicing
the step argument
slice supports a third argument, step
- seq[::2]: Every second element of the sequence
- seq[1::1]: Every second element of the sequence, starting at index 1

The step argument can also be negative
- seq[::-1]: the whole sequence, reversed
- seq[1::-1]: the second two elements, reversed

### constructing lists
- we create a list by putting it's elements between square brackets, separated by commas
- less commonly, we can use the list() function
- an empty list is []

### list operations
- lists are sequences so they support all of the same indexing operations as strings (and other sequences)

```python
len(my_list) # 3
```

### mutability
- rules are teh same for strings with one major exception.
- strings are immutable: assigning to individual elements of a string is not allowed
- tuples are immutable as well
- lists are mutable: individual elements of a list can be reassigned

### other useful list methods
- my_list.append(x): add an item to the end of the list
- my_list.extend(l): extend the list by appending all the items in the given list
- my_list.sort(): sort the items of the list in place
- my_list.remove(x): remove the first item from the list whose value is x. It is an error if there is no such item
- my_list.pop(i): remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list
**note**: all of these operations modify the underlying list

### iteration
- quite often we fine ourselves needing ot run the same bit of code over and over again
- this is called iteration
- examples you may have heard of:
    - for loop: run code over every element of some set
    - while loop: repeat until some condition is met

```python
def countdown(n):
    while n > 0:
        print(n)
        n -= n
    print('we have liftoff!')
countdown(3)
# 3
# 2
# 1
# we have liftoff!
```

### while loops
- while <condition>:
    <body>

### caution
- infinite loops are possible
!careless use of while loops can lead to a program that hangs

### example: collatz conjecture
- start with any positive integer n
- if n is 1 return n else loop
- if n is even, divide by 2
- else
- compute 3n + 1
- and assign new result to n

```python
def collatz(n):
    while n != 1:
        print(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n // 2
    return n

collatz(20)
# 20
# 10
# 5
# 16
```

### breaking out
- the break keyword lets you manually exit a loop
- newtons method for finding square roots
```python
def newton:
    """ locate root of f(x) = (x-a)^2
    by newton's method"""
    while True:
        print(x)
        x_prime = x - (x - a) / 2
        if abs(x - x_prime) < 1e-8:
            break
        x = x_prime

newton(3.5, 4)
```

### iterating over sequences 
- for loop is more general 
- general syntax:
for x in iterable:
    <code that uses x>

- the for...in are special python keywords that signify iteration
- iterable is anything that supports iteration (duck typing)

```python
for i in range(3)
    print(i)
# 0
# 1
# 2

for letter in 'abc':
    print(letter)
# 'a'
# 'b'
# 'c'
```

### recursion
- a final method of repeatedly calling code is recursion
- functions are allowed to call themselves
- lends itself well to functions which can be broken down into subproblems which have the same structure.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### example: string traversal
- let's see how to use for loops and sequence iteration to write a useful function
```python
def count(data, item):
    """ return the number of occurences of item in data"""
    count = 0
    for i in data:
        if i == item:
            count += 1
    return count
```
### common patterns

```python
fruits = ['apple', 'banana', 'cherry']
for f in fruits:
    print(f.upper())
# APPLE
# BANANA
# CHERRY
```

list traversal, modify in place
- the built-in function enumerate() takes a sequence as an argument and returns a tuple of the index and value of each element in the sequence

```python
for i, f in enumerate(fruits):
    fruits[i] = f.upper()
```

### list comprehension
- a list comprehension is a compact way to write an expression that expands to a whole list

```python
# long form
my_list = []
for num in [1,4,5,9,10]:
    if num % 2 == 0:
        my_list.append(num * 3)

# same function using list comprehension
my_list = [num * 3 for num in [1,4,5,9,10] if num % 2 == 0]
```
### generators
- generators are a special class of functions that simplify the task of writing iterators
- regular functions compute a value and return it, but generators return an iterator that returns a stream of values
- you can iterate on generators using the same syntax as regular functions

```python
list1 = [i for i in range(5)]
gen = (i for i in range(5))
print(list1)
print(gen)
# [0, 1, 2, 3, 4]
# <generator object <genexpr> at 0x7f9b1c1b6f68>
```

### dictionary
- a dictionary is a collection of key-value pairs
- dictionaries are indexed by keys
- keys can be any immutable type

### example
- uofm wants to crate a map between umids and actual names
- a dict is a simple type of database
- dictionaries have length
- can quickly tell you key membership

```python
umid2name = {}
umid2name["jravi"] = "Jayashree Ravi"
umid2name["jdoe"] = "John Doe"

len(umid2name) # 2
"jravi" in umid2name # True
"aeinstein" in umid2name # False
```

### dicts vs. lists

```python
# dict comprehension
huge_dict = {x: x for x in range(100_000_000)}
huge_list = list(range(100_000_000))
x = 1_234_567
x in huge_dict # fast
x in huge_list # slooow
# this is because lists are ordered
# note: the underscore separating the digits is allowed in python 3.6+
```

### common patterns
dict traversal
- iterating over a dicts returns each of it's keys
```python
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
for name, score in fruits.items():
    print(name, score)
```

### unpacking
- in python, typicall the expression a,b,c creates a tuple

### set
```python
my_set = {1,1,2}
len(my_set) # 2
```

- another unordered collection with no duplicate elements
- similar to dictionary you use {} to create a set 
- a default {} is a dictionary however adding individual values (not key:value pairs) makes it a set
- set methods: intersetion, union, issubset, etc
- set operations

