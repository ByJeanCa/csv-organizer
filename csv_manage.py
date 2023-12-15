import csv
import os

class CSVManage:
    def __init__(self):
        pass

    def read_csvfile(self, filepath):
        """Read the contents of a CSV file and return the data as a list of dictionaries."""
        try:
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                return data
        except FileNotFoundError:
            print(f"Error: The file '{filepath}' was not found.")
        except Exception as e:
            print(f"Error while reading the CSV file: {e}")

        return None

    def create_csvfile(self, filepath, header):
        """Create a new CSV file with the specified header if it doesn't exist."""
        if not os.path.exists(filepath):
            try:
                with open(filepath, "w", newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=header)
                    writer.writeheader()
                print(f"CSV file '{filepath}' created successfully.")
                return True
            except Exception as e:
                print(f"Error while creating the CSV file: {e}")
                return False
        else:
            print(f"Error: The file '{filepath}' already exists.")
            return False
        
    def add_data(self, filepath, data, header):
        """Add a new row of data to an existing CSV file."""
        try:
            if not os.path.exists(filepath):
                print(f"Error: The file '{filepath}' does not exist.")
                return False
            
            with open(filepath, "a", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=header)

                # Check if the file is empty and write the header if needed
                if file.tell() == 0:
                    writer.writeheader()

                writer.writerow(data)

            print(f"Data added successfully to the file '{filepath}'.")
            return True
        except Exception as e:
            print(f"Error while adding data to the CSV file: {e}")
            return False
        
    def search_occurrences(self, filepath, value):
        """Search for occurrences of a specific value in a CSV file."""
        if not os.path.exists(filepath):
            print(f"Error: The file '{filepath}' does not exist.")
            return False

        occurrences = []

        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames

            for data in reader:
                for head in header:
                    if data[head] == value:
                        occurrences.append(data)

        if occurrences:
            return occurrences
        else:
            print(f"No occurrences found for value '{value}' in the file '{filepath}'.")
            return False
                    
        
    def updated_data(self, filepath, old_data, new_data):
        """Update data in a CSV file based on old and new data."""
        if not os.path.exists(filepath):
            print(f"Error: The file '{filepath}' does not exist.")
            return False

        data_list = []
        updated = False

        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for data in reader:
                if all(data[key] == str(old_data[key]) for key in old_data):
                    data_list.append(new_data)
                    updated = True
                else:
                    data_list.append(data)
            header = reader.fieldnames

        if not updated:
            print("No data found to update.")
            return False

        with open(filepath, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(data_list)
        
        print(f"Data updated successfully in the file '{filepath}'.")
        return True
    
    def change_value(self, old_data, old_value, new_value):
        """Change the value in a dictionary based on the old value."""
        new_data = dict(old_data)
        value_changed = False
        
        for key, value in old_data.items():
            if value == old_value:
                new_data[key] = new_value
                value_changed = True

        if not value_changed:
            return None 

        return new_data
            
