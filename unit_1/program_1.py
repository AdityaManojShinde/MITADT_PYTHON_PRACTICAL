
# 1.1) create and access list elements
num_list = [1,2,5,2,7,7,2,6,9,8,11,10]
print("List : ",num_list)
print("Fist Element : ",num_list[0])
print("Last Element : ",num_list[-1])
print("First 3 Elements : ",num_list[0:3])

# 1.2) add and remove list elemets
num_list.append(100)
print("new element 100 added :")
print(num_list)
num_list.remove(11)
print("removed element 11 added :")
print(num_list)

# 1.3) Sort List Elements

def sort_list(arr):
    n = len(arr)
    for i in range(n - 1):  
        for j in range(n - 1 - i):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print("Sorted List:", sort_list(num_list))

# 1.4) Reverse List Elements
def reverse_list(lst):
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]

print("Reversed List:", reverse_list(num_list))