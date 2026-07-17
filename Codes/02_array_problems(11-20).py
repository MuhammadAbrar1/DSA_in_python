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



# problem_13__Replace even number with 0 in-place

def replace_odd_numbers_with_minus1(arr):
    for i in range(len(arr)):
        if arr[i]%2!=0:
            arr[i]=-1
    return arr
# time complexity = O(n)
# Space complexity = O(1)



# problem_14__count positive numbers

def count_positive_numbers(arr):
    positive_numbers=0
    for i in range(len(arr)):
        if arr[i]>0:
            positive_numbers+=1
    return positive_numbers
# time complexity = O(1) + O(n) = O(n)
# Space complexity = O(1)



# problem_15__count occurences of target

def count_occurences_of_target(arr,t1):
    occurences_of_target=0
    for i in range(len(arr)):
        if arr[i]==t1:
            occurences_of_target+=1
    return occurences_of_target

# time complexity = O(1) + O(n) = O(n)
# Space complexity = O(1)



# problem_16__numbers greater than x

def numbers_greater_than_x(arr,y):
    greater_than_x=[]
    for i in range(len(arr)):
        if arr[i]>y:
            greater_than_x.append(arr[i])
    return greater_than_x

# time complexity = O(1) + O(n) = O(n)
# Space complexity = O(n)


# problem_17__Second largest number

def second_largest_number(arr):
    largest=arr[0]
    second_largest = None

    for i in range(1,len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        elif arr[i]<largest and (second_largest is None or arr[i]>second_largest):
            second_largest=arr[i]
        else:
            continue
    return second_largest

# print(second_largest_number(2,3,4,8,3,7))


# problem_18__check ascending sorting

def check_asscending_sorting(arr):
    previous_value=arr[0]
    for i in range(1,len(arr)):
        if arr[i] >previous_value:
            previous_value=arr[i]
        elif arr[i]<previous_value:
            return False
    return True

# problem_19__Move Zeros to the end

    def move_zeros_to_end(arr):
        next_position=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[next_position]=arr[i]
                next_position+=1
        for i in range(next_position,len(arr)):
            arr[i]=0
        return arr




# problem_20__remove targeted value

def remove_targeted_value(arr,target):
    next_position=0
    for i in range(len(arr)):
        if arr[i]!=target:
            arr[next_position]=arr[i]
            next_position+=1
    return arr[:next_position]


    
print(negative_values_in_place([14, 83, -192, 337, -456, 523, 611, -784, -829, 905]))
print()
print(replace_even_numbers_with_0([14, 83, 12, 23, 632, 522, 613, 784, 829, 905]))
print()
print(replace_odd_numbers_with_minus1([14, 83, 192, 337, 456, 523, 611, 784, 829, 905]))
print()
print(count_positive_numbers([14, 83, -192, 337, -456, 523, 611, -784, -829, 905]))
print()
print(count_occurences_of_target([400, 400, 300, 200, 100, 44, 500, 200, 500, 300, 
                                  600, 400, 200, 100, 900, 900, 200, 400, 700, 100, 
                                  22, 300, 700, 77, 1000, 600, 500, 300, 400, 11, 
                                  55, 800, 600, 33, 200, 88, 66, 100, 500, 800, 
                                  100, 700, 100, 200, 200, 300, 300, 100, 100, 1000],200))
print()
print(numbers_greater_than_x([14, 83, 12, 23, 632, 522, 613, 784, 829, 905],200))
print()
print(second_largest_number([10,10,5]))
print()
print(check_asscending_sorting([14, 83, 12, 23, 632, 522, 613, 784, 829, 905]))
print()
print(remove_targeted_value([400, 400, 300, 200, 100, 44, 500, 200, 500, 300, 
                                  600, 400, 200, 100, 900, 900, 200, 400, 700, 100, 
                                  22, 300, 700, 77, 1000, 600, 500, 300, 400, 11, 
                                  55, 800, 600, 33, 200, 88, 66, 100, 500, 800, 
                                  100, 700, 100, 200, 200, 300, 300, 100, 100, 1000],200))