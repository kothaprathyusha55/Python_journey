"""
1876. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.
"""
def countGoodSubstrings(s):
    count=0
    for i in range(len(s)-2):
        ch1=s[i]
        ch2=s[i+1]
        ch3=s[i+2]
        if ch1!=ch2 and ch1!=ch3 and ch2!=ch3:
            count+=1
    print(count)
s=input()
countGoodSubstrings(s)
