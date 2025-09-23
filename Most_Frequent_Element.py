'''Input: [1, 3, 2, 3, 4, 3, 5]
Output: 3 (frequency = 3)

Input: ["a", "b", "b", "c", "a", "b"]
Output: "b" (frequency = 3)'''


data = [1, 3, 2, 3, 4, 3, 5]

fq = {}
for item in data:
    if item in fq:
        fq[item] += 1
    else:
        fq[item] = 1

max_fq = 0
max_item = None

for key, value in fq.items():
    if value > max_fq:
        max_fq = value
        max_item = key

print("Element:", max_item, "Frequency:", max_fq)