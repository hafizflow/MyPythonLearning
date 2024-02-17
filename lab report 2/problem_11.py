# Problem 9: Write a recursive function that takes in a list of integers,
# and returns the sum of only odd numbers inside the list.


def sum_of_odd_recursive(lst):
    if not lst:  # Base case: empty list
        return 0
    else:
        current_number = lst[0]
        rest_of_the_list = lst[1:]

        if current_number % 2 != 0:  # Check if the current number is odd
            return current_number + sum_of_odd_recursive(rest_of_the_list)
        else:
            return sum_of_odd_recursive(rest_of_the_list)


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_recursive = sum_of_odd_recursive(input_list)
print(f"The sum of odd numbers in the list {input_list} is: {result_recursive}")
