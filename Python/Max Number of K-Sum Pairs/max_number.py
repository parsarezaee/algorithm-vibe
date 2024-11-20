from collections import Counter



nums = [1, 2, 3, 4]
k = 5
count = (Counter(nums))
opr = 0
for num in nums:
    if count[num] > 0 and count[k - num] > 0:
        if num == k - num and count[num] < 2:
            continue
        count[num] -= 1
        count[k - num] -= 1
        opr +=1

print(opr)