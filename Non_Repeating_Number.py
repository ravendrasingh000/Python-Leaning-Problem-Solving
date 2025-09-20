num = [2,4,5,4,2,5,8,6,6]

# count = 0
# uq = 0
# for i in range(len(num)):
#     count = 0
#     for j in range(len(num)):
#         if num[i] == num[j]:
#             count += 1
#             uq = num[i]
#     if count == 1:
#         print(uq)
#         break
# else:
#     print("Doesn't have any Repeated Number ")







# short method 

for n in num:
    if num.count(n) == 1:
        print(f"Non Repeating Number: {n}")
        break
else:
    print("Doesn't have any Repeated Number")