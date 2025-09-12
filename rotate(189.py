def rotate(nums, k):
    List=[]
    count=0
    for i in range(len(nums)-k,len(nums)):
            List.append(nums[i])
    for j in range(len(nums)-k):
        List.append(nums[j])
    return List
nums=list(map(int,input().split()))
k=int(input())
print(rotate(nums,k))
