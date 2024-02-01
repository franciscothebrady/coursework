## 2024-01-31

### regular expressions

using regular expressions to manipulate strings

### the `re` package
some basic functions:
- `re.match(pattern, string)` - returns a match object if the pattern is found at the beginning of the string, otherwise returns `None`
- `re.sub(pattern, repl, string)` - replaces all occurrences of the pattern in the string with repl
- `re.search(pattern, string)` - returns a match object if the pattern is found anywhere in the string, otherwise returns `None`
- `re.findall(pattern, string)` - returns a list of all non-overlapping matches of the pattern in the string
- `re.split(pattern, string)` - splits the string by the occurrences of the pattern

Exam review:
- chapter 8: ebooks.mobibootcamp.com/python/index.html
- 45 mins
- 2 parts
- 1st part: multiple choice
- 2nd part: code challenge

### usage 

```python
import re
my_text = "catorangecatdogapplecatkiwi"
pattern = "cat"
re.sub(pattern, "CAT", my_text)
# 'CATorangeCATdogappleCATkiwi'
re.findall(pattern, my_text)
# ['cat', 'cat', 'cat']
re.split(pattern, my_text)
# ['', 'orange', 'dogapple', 'kiwi']
```

### matching and repetition

- `*` - zero or more repetitions
- `+` - one or more repetitions
- `?` - zero or one repetitions
- `.` - one of any character
- `{2}` - exactly 2 repetitions
- `{3,}` - 3 or more repetitions
- `{2,3}` - between 2 and 3 repetitions

```python
re.findall("ca*t", 'ct cat caat caaat')
# ['ct', 'cat', 'caat', 'caaat']
re.findall("ca+t", 'ct cat caat caaat')
# ['cat', 'caat', 'caaat']
re.findall("c?t", 'ct cat caat caaat')
# ['ct', 'cat', 'ct']
re.findall("c.t", 'ct cat cut cup')
# ['cat', 'cut']
re.findall("ca{2}t", 'ct cat caat caaat')
# ['caat']
re.findall("ca{3,}t", 'ct cat caat caaat')
# ['caaat']

```

### sets and ranges
- `[abc]` - one of the characters a, b, or c
- `[a-z]` - one of the characters a through z
- `[A-Z]` - one of the characters A through Z
- `[0-9]` - one of the characters 0 through 9
- `[^abc]` - any character except a, b, or c

### using raw strings
- `r"string"` - raw string
- prevents python from interpreting backslashes as escape characters
- avoids escaping every backslash in the regular expression

```python
re.sub(r'\\\$', '-', 'A\$bc')
# 'A-bc'
re.sub(r'\\z', '-', 'a\zbc')
# 'a-bc')

```

### or operator
- `|` - or operator
- `a|b` - either a or b

```python
re.findall("cat|dog", 'cat dog catdog')
# ['cat', 'dog', 'cat', 'dog']
```

### extracting groups
example: matching the user and domain of an email address

```python
email = "an email is fbrady@umich.edu"
m = re.search(r'([\w.-]+)@([\w.-]+)', email)
m.group()
# 'fbrady@umich.edu'
m.group(1)
# 'fbrady'
m.group(2)
# 'umich.edu'
```

### backreferences
Can refer to an earlier match within the same regex
`\n` - matches the nth group

```python
m = re.search(r'(\S+) \1', 'cat cat')
m.group()
# 'cat cat'
m = re.search(r'(\S+) \1', 'cat dog')
m.group()
# None
```

