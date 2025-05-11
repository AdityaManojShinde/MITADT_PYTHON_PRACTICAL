#  Problem Statement 7: Write a Python function to find the missing number. You have a list of 
# integers that contains all but one number in the range from 1 to n.  

def find_missing_number(arr):
    num_set = set(arr)  
    n = len(arr) 
    for i in range(1, n + 2):  
        if i not in num_set:  
            return i         

def find_missing_num(arr):
    n = len(arr) + 1
    total =  (n*(n+1)) // 2
    sum_of_arr = 0
    for i in arr:
        sum_of_arr += i
    return total - sum_of_arr

print(find_missing_num([1, 2, 3, 5]))  # Output: 4
print(find_missing_num([10, 7, 8, 9, 6, 5, 3, 1, 2]))  # Output: 4
print(find_missing_num([2]))  # Output: 1
print(find_missing_num([1]))  # Output: 2

