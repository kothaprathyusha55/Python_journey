"""
43. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
"""
def avg_max_subarray(nums,k):
    n=len(nums)
    List=[]
    for i in range(n-k+1):
        avg=0
        sums=0
        count=0
        for j in range(i,i+k):
            sums+=nums[j]
            count+=1
            if count==k:
                avg=sums/float(k)
                List.append(avg)
    print(f"{max(List):.5f}")
nums=list(map(int,input().split()))
k=int(input())
avg_max_subarray(nums,k)
