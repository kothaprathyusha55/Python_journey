"""
2062. Count Vowel Substrings of a String

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.
"""
def countVowelSubstrings(word):
    n=len(word)
    count=0
    vowels=set('aeiou')
    for i in range(n):
        freq={}
        for j in range(i,n):
            if word[j] in vowels:
                freq[word[j]] = freq.get(word[j],0)+1
                if len(freq)==5:
                    count+=1
            else:
                break
    print(count)
word=input()
countVowelSubstrings(word)
