"""
926. Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.
"""

def flip_string(s):
    ones=0
    flips=0
    for i in s:
        if i=='1':
            ones=ones+1
        else:
            flips=min(flips+1,ones)
    print(flips)
s=input()
flip_string(s)
