
def encrypt(word, k):
    t=''
    for i in word:
        m=letters.index(i)+k
        t=t+letters[m]
    return t

global letters 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
word=input("Please enter the word: ")
k = int(input("Please enter k: ")) 

print(encrypt(word, k))
