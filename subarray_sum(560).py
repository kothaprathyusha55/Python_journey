"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
def subarray_sum(n,k):
    count=0
    prefix_sum=0
    prefix_map={0:1}
    for i in n:
        prefix_sum+=i
        if prefix_sum-k in prefix_map:
            count+=prefix_map[prefix_sum-k]
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1

    print(count)
n=list(map(int,input().split()))
k=int(input())
subarray_sum(n,k)
    
