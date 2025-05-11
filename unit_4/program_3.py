import json
import csv
import os

def json_to_csv(json_file_path, csv_file_path):
    try:
        # Read JSON file
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Check if the data is a list/array
        if not isinstance(data, list):
            print("Error: JSON content is not an array")
            return False
        
        if not data:
            print("Error: JSON array is empty")
            return False
            
        # Extract field names from the first item (assuming all items have same structure)
        field_names = data[0].keys()
        
        # Write to CSV file
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
            
        print(f"Successfully converted JSON to CSV: {csv_file_path}")
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found")
        return False
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    # Sample JSON data to create a test file
    sample_data = [
        {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
        {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35}
    ]
    
    # Create directory for data files if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Define paths for our files
    json_path = os.path.join(data_dir, "sample_data.json")
    csv_path = os.path.join(data_dir, "output.csv")
    
    # Create a sample JSON file
    with open(json_path, 'w') as f:
        json.dump(sample_data, f, indent=4)
    print(f"Sample JSON file created at: {json_path}")
    
    # Convert JSON to CSV
    json_to_csv(json_path, csv_path)

if __name__ == "__main__":
    main()