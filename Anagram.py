# Anagram

# str1 = "listen"
# str2 = "silent"

# sstr1 = sorted(str1.lower())
# sstr2 = sorted(str2.lower())

# if sstr1 == sstr2:
#     print("Anagram")
# else:
#     print("Not Anagram")


# ..............................................................................................
# in detailed way

str1 = "listen"
str2 = "silent"

f = str1.lower()
s = str2.lower()
count = 0 

if len(f) != len(s):
    print("Not Anagram")
else:
    for ch in f:
        if ch in s:
            count += 1
            s = s.replace(ch, "", 1)
        else:
            print("Not Anagram")
            break

    if count == len(f):
        print("Anagram")
    else:
        print("Not Anagram")         