"""
532. K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
"""
"""
def Pairs(nums,k):
    List=[]
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            List1=[]
            diff= abs(nums[i]-nums[j])
            if diff==k:
                pair=sorted([nums[i],nums[j]])
                if pair not in List:
                    List.append(pair)
    print(len(List))
    print(List)
nums=list(map(int,input().split()))
k=int(input())
Pairs(nums,k)
"""
from collections import Counter

def Pairs(nums, k):
    freq = Counter(nums)   
    result = set()

    for num in freq:
        if k > 0 and (num + k) in freq:
            result.add(tuple(sorted([num, num + k])))
        elif k == 0 and freq[num] > 1:
            result.add((num, num))  

    print(len(result))
    print([list(p) for p in result])

nums=list(map(int,input().split()))
k=int(input())
pairs(nums,k)


                
                
