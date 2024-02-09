# Given the participants' score sheet for your
# University Sports Day, you are required to find
# the runner-up score.
# You are given  scores. Store them in a list
# and find the score of the runner-up.

# solution 1
def find_second_max(arr):
    if len(arr) < 2:
        return 'The array must have more than one element'

    max_value = float('-inf')
    second_max = float('-inf')

    for i in arr:
        if i > max_value:
            second_max = max_value
            max_value = i
        elif i > second_max and i != max_value:
            second_max = i

    if second_max == float('-inf'):
        return 'No second max found'

    return second_max


arr = list(map(int, input().split()))
result = find_second_max(arr)
print("Second maximum:", result)

# solution 2 found by GPT
# def find_second_max_number():
#     lists = map(int, input().split())
#     unique_value = list(set(lists))
#     unique_value.sort(reverse=True)
#     print('Second maximum:', unique_value[1])
#
#
# find_second_max_number()
