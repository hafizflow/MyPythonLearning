nums = [-1, 0, 3, 5, 9, 12]
target = 9

left = 0
right = len(nums) - 1

# mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
