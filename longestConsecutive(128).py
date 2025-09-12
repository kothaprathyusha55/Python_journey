"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

def longestConsecutive(nums):
    nums.sort()
    count=1
    maxSum=1
    if len(nums)<=0:
        return 0
    temp=nums[0]
    for i in range(1,len(nums)):
        if nums[i] == temp:
            continue
        elif(nums[i]-temp==1):
            temp=nums[i]
            count+=1
            maxSum=max(maxSum,count)
        else:
            count=1
        temp=nums[i]
    return maxSum
nums=list(map(int,input().split()))
print(longestConsecutive(nums))
