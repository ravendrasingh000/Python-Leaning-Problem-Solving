num = 12321

renum = num
rv = 0
digit = 0

while num > 0:
    digit = num%10
    rv = rv*10+digit
    num = num//10

if renum == rv:
    print("Palindrome")
else:
    print("Not Palindrome")

