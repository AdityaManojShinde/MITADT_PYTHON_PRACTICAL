from temperature.fahrenheit_to_celsius import fahrenheit_to_celsius
from temperature.celsius_to_fahrenheit import celsius_to_fahrenheit
from temperature.celsius_to_kelvin import celsius_to_kelvin

def main():
    while True:
        print("\nWhat do you want to perform?")
        print("1. Celsius to Fahrenheit conversion")
        print("2. Fahrenheit to Celsius conversion")
        print("3. Celsius to Kelvin conversion")
        print("4. Exit")
        op = input("Enter number of operation (1/2/3/4): ")
        
        if op not in ["1","2","3","4"]:
            print("Please enter a valid number")
            continue
            
        if op == "4":
            print("Exiting program. Goodbye!")
            break
            
        if op == "1":
            temp = input("Enter Temperature in Celsius: ")
            fah = celsius_to_fahrenheit(float(temp))
            print(f"{temp} C = {fah} Fah")
            
        elif op == "2":
            temp = input("Enter Temperature in Fahrenheit: ")
            output = fahrenheit_to_celsius(float(temp))
            print(f"{temp} Fah = {output} C")
            
        elif op == "3":
            temp = input("Enter Temperature in Celsius: ")
            kel = celsius_to_kelvin(float(temp))
            print(f"{temp} C = {kel} K")

if __name__ == "__main__":
    main()
