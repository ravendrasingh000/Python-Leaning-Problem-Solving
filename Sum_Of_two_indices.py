'''Q. Statement: Array nums aur target t diya hai. Do indices return karo jinke elements ka sum t ho. Agar multiple ho to koi bhi ek pair.
Input: nums = [2,7,11,15], t = 9
Output: [0,1]'''


nums = [3,6,7,8,12,67,43]
t = 10
a = 0
b = 0

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if t == (nums[i] + nums[j]):
            a = i
            b = j
print(f"These Are Indices {a} and {b}")