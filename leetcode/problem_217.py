nums = [1, 2, 3, 4]
new = []

# def containsDuplicate(self, nums: list[int]) -> bool:
#     hashset = set()
#     for i in nums:
#         if i in hashset:
#             return True
#         hashset.add(i)
#     return False


# easy solution
if len(nums) == len(set(nums)):
    print('False')
print('True')
