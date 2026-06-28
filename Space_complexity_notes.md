
### Space Complexity

Space complexity shows how much extra memory an algorithm uses as input size n grows.

Time complexity asks:

How many operations?

Space complexity asks:

How much extra memory?

Important point:

We usually count extra memory created by the algorithm.
We usually do not count the input itself.

⸻

## O(1) space means the algorithm uses a fixed amount of extra memory.

The memory does not grow when input size n grows.

Example:

```python
def find_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

Extra memory used:

total
num

Even if the array has:

10 elements
1000 elements
1,000,000 elements

the algorithm still uses only a few extra variables.

So:

Time Complexity = O(n)
Space Complexity = O(1)

⸻

## O(n) Space - Linear Space

O(n) space means the algorithm creates extra memory that grows with input size n.

Example:

``` python
def double_numbers(arr):
    result = []
    for num in arr:
        result.append(num * 2)
    return result
```
If input has 5 elements, result will have 5 elements.

If input has 1000 elements, result will have 1000 elements.

So the extra memory grows with n.

Time Complexity = O(n)
Space Complexity = O(n)

⸻

## O(n²) Space - Quadratic Space

O(n²) space means the algorithm creates a 2D structure, like a matrix or grid, with n × n values.

Example:

```python
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix
```
If n = 3:

3 × 3 = 9 values

If n = 10:

10 × 10 = 100 values

If n = 100:

100 × 100 = 10,000 values

So the extra memory grows like:

n × n = n²

Therefore:

Space Complexity = O(n²)

⸻

Quick Memory Rule

Few extra variables       → O(1) space
New list/dict/set of n    → O(n) space
Matrix or grid n × n      → O(n²) space

⸻

My Understanding

Space complexity is about memory, not operations.

If the algorithm only creates a few variables, space is O(1).

If the algorithm creates a new list that grows with input size, space is O(n).

If the algorithm creates a matrix or grid with n rows and n columns, space is O(n²).