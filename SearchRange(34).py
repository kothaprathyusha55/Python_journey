
"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
def searchRange(nums,target):
    index=[]
    for i in range(len(nums)):
        if nums[i]==target:
            index.append(i)
    if len(index)>2:
        return [index[0],index[-1]]
    elif len(index)==2:
        return index
    else:
        return [-1,-1]
nums=list(map(int,input().split()))
target=int(input())
print(searchRange(nums,target))
    
