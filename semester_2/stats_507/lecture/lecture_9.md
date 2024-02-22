## 2024-02-12

### Midterm Exam
- 50 minutes to finish the exam
- Enter from the back
- Sit in the back

2 Parts:
- Covering through Lecture 8
- Canvas quiz online
- Programming Challenge
- Cheatsheet will be included

### CAP Theorem or Brewer's Theorem
A distributed datastore can have only 2 of the 3 properties:
- Consistency: all nodes see the same data at the same time.
- Availability: a guarantee that every request receives a response about whether it was successful or failed.
- Partition-tolerance: the system continues to operate despite arbitrary message loss or failure of part of the system.

What data transactions properties are required?
SQL follows ACID properties: Atomicity, Consistency, Isolation, Durability
- this means that SQL is consistent, but not available or partition-tolerant

NoSQL follows BASE properties: Basically Available, Soft-state, Eventually consistent
- this means that NoSQL is available and partition-tolerant, but not consistent (eventually consistent)

NoSQL = Not Only SQL
- Does not use Schemas
    - Multiple different standards: NoSQL, DynamoDB (Amazon), Cassandra (Facebook), MongoDB (JSON)
- Horizontal scaling: adding more servers to increase capacity
    - contract with vertical scaling: adding more power/capacity to a single server
- Simple API

### Implementation Differences
- Key-Value Store
- Document Store
- Row, Column Store
- In-memory Store

https://db-engines.com/en/ranking

### What do you get with NoSQL
- High scalability for simple operations (SO) on multiple nodes
    - Simple Operations = CRUD (Create, Read, Update, Delete)
- Data partitioning (sharding) and replication on multiple nodes
    - relaxed consistency
    - flexibility in data structure

Cons:
- Transactions management is less rigorous
- Relaxed consistency
- Queries that span multiple shards are very inefficient or impossible

### What you lose with NoSQL
many database innovations remain unique to SQL databases:
- variety of indexing
- query optimization
- storage optimization

## Lecture 8

### Numerical computing in Python: Numpy
- everything in python data science is based on numpy

### numpy data types
Five basic data types:
- integer (int)
- floating point (float)
- boolean (bool)
- unsigned integer (uint)
- complex (complex)

### numpy arrays
can be created from a python list
```python
np.array([1, 2, 3], dtype='uint')
# array([1, 2, 3], dtype=uint32)
```
by "shaping" an array
```python
np.zeros((2, 3))
# array([[0., 0., 0.],
#        [0., 0., 0.]])
```
by ranges:
```python
np.arange(2,3,0.1(, dfype='float'))
# array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
```

### numpy allows arrays of arbitrary dimensions
```python
# 1-dimensional array
x = np.arange(12)
x
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
# 2-dimensional array (matrices)
x = x.reshape(3, 4) # now x is a 3x4 matrix
x # observe that shape fills the new matrix by rows
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
```
### more array indexing
```python
x = np.arange(10)
x[2:5] # array([2, 3, 4])
x[x>7] # array([8, 9])
```
#### Boolean indexing
```python
x = np.arange(10)
x[x%2==0] # array([0, 2, 4, 6, 8])
np.any(x>7) # True
np.any([x>7, x<2]) # True
```
### random number generation
```python
rng = np.random.default_rng()
rng.random(3) # array([0.5488135 , 0.71518937, 0.60276338])
np.random.default_rng().integer(0, 10, 3) # array([3, 7, 9])
```
