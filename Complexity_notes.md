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



----------


### O(log n)

# Binary search  

- Examle 
number_list = [4,9,15,21,34,57,68,91]        # search for 68

we can use 

``` python 
for i in number_list:
    if number_list[i] == 68:
        print(i)

"""it is a long and time consuming if the arr is too long."""
```

- sowe use Binary search.

1. split the arr in half and discard the left elements i.e. so numbers from 4-21 will be discarded.
    first Iteration          remaining --> [34,57,68,91]   Remaining elements after Iteration 1 = n/2

2. now again the same process and this time from 34-57
    second iteraton             remaining --> [68,91]      Remaining elements after Iteration 2 = (n/2)/2 = n/2**2

3. now in this Iteration we will find 68 which was the target.
                                answer --> [68]              Remaining elements after Iteration 3 = (n/2**2)/2 = n/2**3

- so in just 3 Iterations we can reach to the answer.

so the general formula is 

                       Remaining elements after Iteration k = n/2**k

                        after k Iterations, the remaning arr size is:

                            remaining size = n/2**k
        
                        we stop only when one element remains.
        
                                1 = n/2**k

                                2**k = n

                        applying log(base 2) on both sides

                                k log2 (2) = log2 n  

                                k = O(log n)

 - so as in our example we have 8 elements then,

                                k = log2 (8)
                                k = log2 (2**3)
                                k = 3 log2 (2)
                                k = 3 (Iterations)



----------


### O(n log n)

O(n log n) happens when:

- the problem is divided again and again.
- there are log n levels.
- at each level, we process all n elements.

----

# Formula

work per levele x number of levels.

    n x log n = O(n log n)

Example:
Merge Sort

l = [8,3,5,1,9,2,4,7]

step 1: Divide

we split agian and again.

8 elements 

4 + 4 elements                  (level 1)    8 elements are processed.

2 + 2 + 2 + 2                   (level 2)    8 elements are processed.

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1   (level 3)    8 elements are processed.




----------

### O(2ⁿ)

O(2ⁿ) is called exponential time.

It usually happens when every element has 2 choices.

Examples:

- include / don't include
- take / skip
- yes / no

If there are n elements:

2 × 2 × 2 ... n times = 2ⁿ

Example:

arr = [A, B, C]

Each element has 2 choices:

take or skip

Total possibilities:

2³ = 8

Subsets:

[]
[A]
[B]
[C]
[A, B]
[A, C]
[B, C]
[A, B, C]

So generating all subsets has time complexity:

O(2ⁿ)




----------

### O(n!) - Factorial Time

O(n!) happens when we try every possible order/arrangement.

Example: permutations

arr = [A, B, C]

Possible arrangements:

ABC
ACB
BAC
BCA
CAB
CBA

Total:

3! = 3 × 2 × 1 = 6

So generating all permutations takes:

O(n!)

Memory line:

If the algorithm tries every possible ordering, think O(n!).