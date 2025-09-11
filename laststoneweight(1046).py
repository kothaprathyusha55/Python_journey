import heapq

def lastStoneWeight(stones):
    stones=[-s for s in stones]
    heapq.heapify(stones)
    for i in range(len(stones)-1):
        if len(stones)<2:
            break
        first=-heapq.heappop(stones)
        second=-heapq.heappop(stones)
        if first!=second:
            heapq.heappush(stones,-(first-second))
    return -stones[0] if stones else 0
stones=list(map(int,input().split()))
print(lastStoneWeight(stones))



        
