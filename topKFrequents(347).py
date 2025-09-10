
"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""
import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)
    heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(heap)
    result = []
    for _ in range(k):
        count, num = heapq.heappop(heap)
        result.append(num)
    return result
nums=list(map(int,input().split()))
k=int(input())
print(topKFrequent(nums,k))

