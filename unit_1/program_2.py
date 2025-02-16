# 2.1) Create and access set elements
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

print("Elements of set A:")
for element in A:
    print(element, end=" ")
print("\n")

# 2.2) Union of the elements
union_set = A | B  
print("Union of A and B:", union_set)

# 2.3) Intersection of the elements
intersection_set = A & B 
print("Intersection of A and B:", intersection_set)

# 2.4) Difference of the elements
difference_A_B = A - B  
difference_B_A = B - A  
print("Difference (A - B):", difference_A_B)
print("Difference (B - A):", difference_B_A)
