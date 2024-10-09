s = str(input("enter string : "))
def Vowel(s):
    s = s.lower()
    Vowels = ['a','e','i','o','u']
    count  = 0
    for i in s :
        if i in Vowels:
            count += 1
    return count

print(Vowel(s))

