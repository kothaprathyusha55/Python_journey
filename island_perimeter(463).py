nums=[]
for i in range(4):
    List=[]
    for j in range(4):
        List.append(int(input()))
    nums.append(List)
#print(nums)
p=0
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if nums[i][j]==1:
            p+=4
            if i>0 and nums[i-1][j]==1:
                p-=2
            if j>0 and nums[i][j-1]==1:
                p-=2
print(p)


        
