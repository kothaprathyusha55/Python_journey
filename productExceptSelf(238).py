"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
def productExceptSelf(nums):
    left = 0
    right = 0    
    List = []
    p = 1
    while left < len(nums):
        if right == len(nums):   
            List.append(p)
            left += 1
            right = 0
            p = 1
        elif right != left:
            p *= nums[right]
            right += 1
        else:   
            right += 1
    return List
nums=list(map(int,input().split()))
print(productExceptSelf(nums))
"""
#approach-2

def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

"""
