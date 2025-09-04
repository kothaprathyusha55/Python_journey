"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
def max_area(n):
    left=0
    right=len(n)-1
    max_area=0
    while(left<right):
        min_height=min(n[left],n[right])
        width=right-left
        area=min_height*width
        max_area=max(max_area,area)
        if(n[left]<n[right]):
            left+=1
        else:
            right-=1
    print(max_area)
n=list(map(int,input().split()))
max_area(n)
