# probelm_11__replace Negative values in-place

def negative_values_in_place(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=0
    return arr
# time complexity = O(n)
# Space complexity = O(1)


# problem_12__Replace even number with 0 in-place

def replace_even_numbers_with_0(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]=0
    return arr
# time complexity = O(n)
# Space complexity = O(1)


print(negative_values_in_place([14, 83, -192, 337, -456, 523, 611, -784, -829, 905]))
print(replace_even_numbers_with_0([14, 83, 12, 23, 632, 522, 613, 784, 829, 905]))