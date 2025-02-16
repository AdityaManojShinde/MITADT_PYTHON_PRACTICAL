# 4.1) Create and access dictionary elements
student = {
    "name": "Aditya",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Computer Science"]
}

print("Student Dictionary:", student)


print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Subjects:", student["subjects"])
print("First Subject:", student["subjects"][0])

# 4.2) Update Dictionary
student["age"] = 21
student["city"] = "Pune" 
print("Updated Dictionary:", student)

# 4.3) Removing Elements
del student["grade"]  
removed_subjects = student.pop("subjects") 
print("Dictionary after removal:", student)
print("Removed Subjects:", removed_subjects)

# 4.4) Merging dictionaries
extra_info = {
    "phone": "123-456-7890",
    "email": "aditya@example.com"
}

student.update(extra_info)  
print("Merged Dictionary:", student)
