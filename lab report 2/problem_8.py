# Problem 6: Write a python program where you will be given
# a list [5,2,4,3,2,3] and target value 2, and you have to
# get the index of the list when the target value appears for
# the first time. (do it by user inputting the list and target value)

def find_index(lists, target):
    for i in lists:
        if i == target:
            return lists.index(i)
    return -1


random_list = list(map(int, input().split()))
val = int(input("Enter the target value: "))
print(find_index(random_list, val))
