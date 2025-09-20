num = [2,4,5,4,2,5,8,6,6,8,1,1]

count = 0
uq = 0
for i in range(len(num)):
    count = 0
    for j in range(len(num)):
        if num[i] == num[j]:
            count += 1
            uq = num[i]
    if count == 1:
        print(uq)
        break
else:
    print("Doesn't have any Repeated Number ")