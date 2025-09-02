
def lengthOfLongestSubstring( s):
    max_len=0
    for i in range(len(s)):
        res=[]
        for j in range(i,len(s)):
            if s[j] in res:
                break
            else:
                res.append(s[j])
        max_len=max(max_len,len(res))
    print(max_len)
s=input()
lengthOfLongestSubstring(s)
