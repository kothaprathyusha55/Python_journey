def max_sum_subarray(num):
    max_value=float('-inf')
    n=len(num)
    current_sum=0
    for i in num:
        current_sum+=i
        if (max_value<current_sum):
            max_value=current_sum
        if current_sum<0:
            current_sum=0
    print(max_value)
num=list(map(int,input().split()))
max_sum_subarray(num)
