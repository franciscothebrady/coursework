## 2024-02-07

### python sqlite3 package 
- connection object represents a database connection
    - connections object can be used to create a cursor object
    - cursor facilitates the execution of SQL commands

```python
import sqlite3
conn = sqlite3.connect('example.db')
# estabilish a connection to the database
# return connection object
c = conn.cursor()
# create a cursor object for interacting with the database
c.execute([SQL command])
# runs the given SQL command
# cursor now contains query results
```

### sql injection
When developing python functions that interact with a database, it is important to avoid SQL injection attacks.
Do not use string formatting to insert values into SQL commands. 
```python
# do not do this
def insert_user(name, age):
    c.execute(f"INSERT INTO users (name, age) VALUES ('{name}', {age})")
# instead use the following
def insert_user(name, age):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
```
This is because the first method is vulnerable to SQL injection attacks.

### strftim() function

- The strftime() function returns a string representing date and time using date, time or datetime object.

```python
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
# 2024-02-07 14:00:00
```

### sqlite3 package

- The sqlite3 package is a built-in package that allows python to interact with SQLite databases.
- SQLite is a lightweight, disk-based database that does not require a separate server process.
- SQLite databases are stored in a single file, making them easy to share and move.
- SQLite databases are useful for small to medium-sized databases.

