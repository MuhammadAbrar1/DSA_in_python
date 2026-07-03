# problem_1__Find maximum

def find_maximum(maxi):
    maximum=maxi[0]
    for num in maxi:
        if num > maximum:
            maximum = num
    return maximum


#  problem_2__Find minimum

def find_minimum(min):

    minimum=min[0]

    for num in min:
        if num <minimum:
            minimum=num
    return minimum


#  problem_3__sum of array

def sum_array(a2):
    sum_of_a2=0
    for num in a2:
        sum_of_a2+=num
    return sum_of_a2
print()


# problem_4__count even numbers

def count_even(even):
    count = 0
    for i in even:
        if i%2==0:
            count+=1
    return count



# problem_5__serch target number

def search_target_number(arr,target):
    for num in arr:
        if num==target:
            return "found"
    else:   
        return "not found"
    

# problem_6__serch target and return index

def find_index(values,n1):
    for i in range(len(values)):
        if values[i] ==n1:
            return (f"index is {i}")
    
    return "not found"        


# problem_7__Count numbers greater than x.

def greter_than_x(number,x):
    count_x=0
    for value in number:
        if value>x:
            count_x+=1
    return f"total number greater than x is {count_x}"


# problem_8__list of even numbers

def list_of_even_numbers(list):

    even=[]
    for value in list:
        if value%2==0:
            even.append(value)
            count_even+=1
    return even

print(find_maximum([32,53,78,10,17,33,94,95,55,20,99]))
print()
print(find_minimum([655, 115, 26, 760, 282, 251, 229, 143,755, 105, 
                    693, 759, 914, 559, 90, 605,433, 33, 31, 96, 224, 
                    239, 518, 617, 28]))
print()
print(sum_array([17, 44, 93, 102, 149, 316, 521, 888]))
print()
print(count_even([54, 109, 218, 381, 443, 612, 705, 827, 888, 937]))
print()
print(search_target_number([14, 83, 192, 337, 456, 523, 611, 784, 829, 905],14))
print()
print(find_index([117,4,39,102,189,316,52,808],189))
print()
print(greter_than_x([54, 109, 218, 381, 443, 612, 705, 827, 888, 937],612))
print()
print(list_of_even_numbers([655, 115, 26, 760, 282, 251, 229, 143,755, 105, 
                    693, 759, 914, 559, 90, 605,433, 33, 31, 96, 224, 
                    239, 518, 617, 28]))
print()