import csv
import os

def count_rows_in_csv(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found.")
            print(f"Current working directory: {os.getcwd()}")
            return -1
            
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Count rows using sum and a generator expression
            row_count = sum(1 for _ in csv_reader)
            return row_count
    except Exception as e:
        print(f"Error: {e}")
        return -1

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_dir, "data.csv")
    print(f"Looking for CSV file at: {csv_file_path}")
    row_count = count_rows_in_csv(csv_file_path)
    
    if row_count >= 0:
        print(f"Total number of rows in 'data.csv': {row_count}")