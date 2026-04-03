nums=[1,2,3,4,5,2,9,5,68,3,3,3555,82,100]
if len(nums)==0:
    print("Array is empty")
if len(nums)==1:
    print("Array ahve only one element")
else:
    mid=len(nums)//2
    left_max,left_min=max(nums[:mid]),min(nums[:mid])
    right_max,right_min=max(nums[mid:]),min(nums[mid:])
print(max(left_max,right_max),min(left_min,right_min))
