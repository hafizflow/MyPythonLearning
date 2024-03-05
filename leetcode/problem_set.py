nums = [2, 7, 11, 15]
t = 9
lists = []

for i in range(len(nums)-1):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == t:
            lists.append(i)
            lists.append(j)
            break

print(lists)
