s1 = str(input("enter first string"))
s2 = str(input("enter another string"))
anagrams = lambda s1,s2 : sorted(s1) == sorted(s2)
print("true" if anagrams(s1,s2) else  "no")

