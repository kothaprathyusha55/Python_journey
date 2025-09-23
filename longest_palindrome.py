def longest_palindrome(s):
    res=""
    max_len=0
    for i in range(len(s)):
        s1=""
        for j in range(i,len(s)):
            s1=s1+s[j]
            if s1==s1[::-1] and max_len<len(s1):
                res=s1
                max_len=len(s1)    
    print(res)
s=input()
longest_palindrome(s)
        
            
            
        
