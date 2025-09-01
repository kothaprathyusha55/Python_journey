def reverse_Words(s):
    words=[]
    word=""
    for i in s:
        if i!=' ':
            word+=i
        else:
            if word:
                words.append(word)
                word=""
    if word:
        words.append(word)
    reversed_words=[]
    for i in range(len(words)-1,-1,-1):
        reversed_words.append(words[i])
    res=""
    for i in range(len(reversed_words)):
        res+=reversed_words[i]
        if i!=len(reversed_words):
            res+=' '
    print(res)
s=input()
reverse_Words(s)
        
        
            
