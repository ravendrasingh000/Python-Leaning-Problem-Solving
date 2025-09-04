str = input("Enter your String: ")

count = 0
for i in range(len(str)):
    if str[i] == "A" or str[i] == "E" or str[i] == "I" or str[i] == "O" or str[i] == "U":
        count += 1
print(count)




# other way


s = input("Enter your String: ")

count = 0
for ch in s:
    if ch.upper() in "AEIOU":   # automatically capital check
        count += 1

print(count)
