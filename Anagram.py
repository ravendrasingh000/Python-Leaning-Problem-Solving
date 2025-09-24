# Anagram

str1 = "listen"
str2 = "silent"

sstr1 = sorted(str1.lower())
sstr2 = sorted(str2.lower())

if sstr1 == sstr2:
    print("Anagram")
else:
    print("Not Anagram")