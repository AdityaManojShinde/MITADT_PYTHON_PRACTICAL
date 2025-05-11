# Problem Statement 1: Write a Python function that takes two lists as input, merges them, and 
# removes any duplicates in the merged list. The resulting list should maintain the order of 
# elements from both lists as much as possible.

def merge_lists(list1, list2):
    merged_list = []
    seen = set()
    for item in list1+list2:
        if item not in seen:
            merged_list.append(item)
            seen.add(item)
    return merged_list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(merge_lists(list1, list2)) # Output: [1, 2, 3, 4, 5, 6, 7]

list1 = ["apple", "banana", "cherry"]
list2 = ["banana", "date", "fig"]
print(merge_lists(list1, list2))
# Expected Output: ['apple', 'banana', 'cherry', 'date', 'fig']
