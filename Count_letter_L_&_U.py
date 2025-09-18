# Q. Count Upper Case & Lower Case and Print in object

s = "RaMkriShNa"

L = 0
U = 0
count = {}
for i in s:
    if i == i.upper():
        U += 1
    else:
        L += 1
count["Upper Case"] = U
count["Lower Case"] = L

print(count)