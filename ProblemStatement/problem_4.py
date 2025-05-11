# Problem Statement
# Write a Python function that counts the occurrences of each element in a list and returns a dictionary with elements as keys and their frequencies as values.  

def count_occurrences(numbers):
    frequency = {}
    for i in numbers:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return frequency

test = ["apple", "banana", "cherry", "apple","banana","banana"]
print(count_occurrences(test)) # Output: {2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 5, 9: 2}