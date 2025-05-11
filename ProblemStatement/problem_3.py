# Problem Statement
# Write a Python function that takes a list of numbers as input and returns the largest number. If the list is empty, return a message indicating that the list is empty.

def largest_number(numbers):
    # check if the list is empty
    if not numbers:
        return "List is empty"
    # Assume the first number is the largest
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(largest_number([10, 20, 30]))  # Output: 30
print(largest_number([1]))           # Output: 1
print(largest_number([-10, -20, -5])) # Output: -5
print(largest_number([]))            # Output: "List is empty"
