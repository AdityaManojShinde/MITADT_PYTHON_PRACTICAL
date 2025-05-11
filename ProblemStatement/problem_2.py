# Problem Statement
# Given a tuple of mixed data types, write a Python function that returns the element type at a specific index. If the index is out of range, return a message indicating that the index is invalid.

def element_type(data_tuple, index):
    try:
        item = data_tuple[index]
        return type(item).__name__
    except IndexError:
        return "Index is invalid"
    
sample_tuple = (42, "hello", 3.14, True, [1, 2, 3])

print(element_type(sample_tuple, 1))  # Output: 'str'
print(element_type(sample_tuple, 3))  # Output: 'bool'
print(element_type(sample_tuple, 10))