na=int(input("Enter the Length of array: "))
nums=[]
for i in range(na):
    num=int(input("enter number : "))
    nums.append(num)
n=len(nums)
post=[1]*n
prefix=1
for i in range(n):
    post[i]=prefix
    prefix*=nums[i]
postfix=1
for i in range(n-1,-1,-1):
    post[i]*=postfix
    postfix*=nums[i]
print(post)

