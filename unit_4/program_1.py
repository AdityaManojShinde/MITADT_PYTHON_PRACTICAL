# Python program to demonstrate fundamental file handling operations

def main():
    filename = "text.txt"

    # Writing data to a file (this will create the file or overwrite if it exists)
    with open(filename, 'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
    print(f"Data written to {filename}.")

    # Reading the contents of the file
    with open(filename, 'r') as file:
        content = file.read()
    print(f"Contents of {filename} after writing:")
    print(content)

    # Appending additional content to the file
    with open(filename, 'a') as file:
        file.write("This line is appended.\n")
    print(f"Additional data appended to {filename}.")

    # Reading the contents again after appending
    with open(filename, 'r') as file:
        content = file.read()
    print(f"Contents of {filename} after appending:")
    print(content)

if __name__ == "__main__":
    main()
