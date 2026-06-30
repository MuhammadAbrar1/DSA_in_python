arr=[1,2,3,4,5]
left =0
right = len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)

#  Time Complexity = O(n)
#  Space Complxity = O(1)

"""In-Place Array reversal / Two-pointer Technique"""