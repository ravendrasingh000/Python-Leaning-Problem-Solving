s = input("Enter Your Word: ")
rs = ""

for i in range(len(s)-1,-1,-1):
    a = s[i]
    rs = rs + a
print(rs)

