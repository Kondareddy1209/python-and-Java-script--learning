nums=[5,12,49,1,65,6,100,3,2,7,9,11,33,55,88]
mid=len(nums)//2
left_half=nums[:mid]
right_half=nums[mid:]
print(left_half)
print(right_half)
i=0
j=0
arr=[]
while i<len(left_half) and j<len(right_half):
    if left_half[i] < right_half[j]:
        arr.append(left_half[i])
        i+=1
    else:
        arr.append(right_half[j])
        j+=1
print(arr)