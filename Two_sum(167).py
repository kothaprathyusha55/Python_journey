"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


"""
def target(nums,t):
    List=[]
    for i in range(len(nums)):
        s=0
        s+=nums[i]
        for j in range(i+1,len(nums)):
            s+=nums[j]
            if s==t:
                List.append(i+1)
                List.append(j+1)
                break
            else:
                s-=nums[j]
    print(List)
nums=list(map(int,input().split()))
t=int(input())
target(nums,t)
"""
def target(nums,t):
    left=0
    right=len(nums)-1
    s=0
    List=[]
    while(left<right):
        s=0
        s=nums[left]+nums[right]
        if(s==t):
            List.append(left+1)
            List.append(right+1)
            break
        elif(s>t):
            right-=1
        else:
            left+=1
    print(List)
nums=list(map(int,input().split()))
t=int(input())
target(nums,t)
        
           
        
                
