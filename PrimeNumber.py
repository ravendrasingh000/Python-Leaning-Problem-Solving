n = int(input("Enter Your Number: "))

count = 0
for i in range(1, n+1):
    if n%i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")






# Other way to Solve
import math

n = int(input("Enter Your Number: "))

for i in range(math.floor(n/2)):
    if n % 2 == 0:
        print("Not Prime Number")
        break

else:
    print("Prime Number")