# 3.1) Create and access tuple elements
num_tuple = (10, 20, 30, 40, 50)
print("Tuple:", num_tuple)


print("First element:", num_tuple[0])
print("Last element:", num_tuple[-1])
print("Tuple slice (2nd to 4th element):", num_tuple[1:4])

# 3.2) Nested Tuple
nested_tuple = (1, 2, (3, 4, 5), (6, (7, 8)))
print("Nested Tuple:", nested_tuple)


print("Element inside nested tuple:", nested_tuple[2][1])  
print("Deeply nested element:", nested_tuple[3][1][0]) 

# 3.3) Repetition of tuple
repeat_tuple = ("Hello",) * 3 
print("Repeated Tuple:", repeat_tuple)

# 3.4) Concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)