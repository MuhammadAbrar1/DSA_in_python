### Time Cmplexity

## Big O notation.
it measures how an algorithm grows as the input size (n) increases.
it measures:
- time complexity
- Space complexity.

----

# Formula

time = a*n + b

a = work done per element.
n = input size.
b = constant work.

----------

## Rules

- Rule 1

keep the fastest growing term

n + n**2 --> n**2

- Rule 2

ignore constants 
2n --> n

----

# Fundamental Big O Rule:

- 1 Loops after one another --> Add
  n + n = 2n --> O(n)

- 2 Nested Loops --> Multiply
  n * n = O(n**2) 

- 3 if there are multiple terms, keep the fastest-growing one
  n + n**2 --> O(n**2)
  
  n + log n --> O(n)

  100 + n --> O(n)

----

# Examples

- ex 1.

``` python
print ("start")             # runs once --> b=1

for num in arr:             # run n times
    print(num)

print("done")               # runs once --> b=1

```
Runs:
start --> once
Loop --> n times
done --> once 
so
~   time = a*n + b

    time = 1+ a*n + 1

    time = a*n + 2

we drop b= 1+1 = 2 and keep the fastest growing term --> a*n

time = a*n --> O(n)

----------



### O(1) 

- why does it become O(1)?

sometimes increasing the inputsize(n) does not affect the running time.

----

# Example:

```python

def get_first(arr):
    return arr[0]

```
- what happens?

if the array has:

10 elements         --> 1 operation
100 elements        --> 1 operation
1000 elements       --> 1 operation
1,000,000 elements  --> 1 operation

- the runnning time stays almost the same no matter how large the array becomes.


           Time

            ^
            |  
            |
            |   
            |   ~~~~~~~~~~~~~~~~~~~~~
            |
            |
            |-------------------------> n (input size)

----

# O(1)Growth Graph

![O(1) Time Complexity Graph](O(1).PNG)

**Observation:**
- Input size: 100 → 0.22 ms
- Input size: 1000 → 0.23 ms
- Execution time is almost constant.
- Small zig-zags are measurement noise (CPU, OS, cache, etc.).
- The overall trend is flat.
- Therefore, the algorithm is **O(1)**.



### O(n^2)

``` python

numbers=[1,2,3,4,5,6]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers))
    if if numbers[i]==numbers[j]:                   # n**2(n square) iterations
        print(numbers[i]+"is a duplicate")
        break
```
- nested loop --> time = a(n*n) + b

-    fasted growing term is selected

                        = a(n**2) 

 -   constant is dropped

                      time = O(n**2)

# again

``` python

numbers=[1,2,3,4,5,6]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers))
    if numbers[i]==numbers[j]:                   # n**2(n square) iterations
        print(numbers[i]+"is a duplicate")
        duplicate = numbers[i]
        break
for i in range(len(numbers)):
    if numbers[i] == duplicate:                  # n iterations
        print(i)
```

                    time = a(n*n) + b*n + c

-    fasted growing term is selected

                        time = a(n**2) 

 -   constant is dropped

                      time = O(n**2)

