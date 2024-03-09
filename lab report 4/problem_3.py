# 3. List Element Frequency: Given a nested list containing lists of integers, write a
# Python program to count the frequency of each element in the entire nested list.


nested_list = [[1, 2, 3], [2, 4, 5], [1, 3, 6]]
dic = {}
new_list = [j for i in nested_list for j in i]
n = len(new_list)
for i in range(n):
    if new_list[i] in dic.keys():
        dic[new_list[i]] += 1
    else:
        dic[new_list[i]] = 1
print(dic)
