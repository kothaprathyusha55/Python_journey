def split_array(nums,k):
    max_value = float('-inf')
    for i in range(len(nums)-k+1):
        s=0
        for j in range(i,i+k):
            s+=nums[j]
        if s>max_value:
            max_value=s
    print(max_value)
nums=list(map(int,input().split()))
k=int(input())
split_array(nums,k)
            
            
