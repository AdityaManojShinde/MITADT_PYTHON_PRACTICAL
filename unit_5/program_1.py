
# Exeption Handling 
try :
    with open("somedata.csv",'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("File not found. Please check the file path.")
except PermissionError as e:
    print("Permission denied. Please check your file permissions.")