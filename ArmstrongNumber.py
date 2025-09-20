num = 1534

power = len(str(num))
n = str(num)
sum = 0
for d in n:
    sum += int(d)**power

if num == sum:
    print(" Armstrong")
else:
    print("Not ArmStrong")
