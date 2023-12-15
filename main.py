import csv_manage
import os
import file_manager

csv_manager = csv_manage.CSVManage()
file_manager = file_manager.FileManager()

def Option1():
    os.system("clear")
    print("You have selected Option 1\n")
    
    file_path = input("Enter the absolute file path: ")
    print()
    
    csvfile = csv_manager.read_csvfile(file_path)

    if csvfile:
        header = csvfile[0].keys()
        print(", ".join(header))

        for data in csvfile:
            values = [str(value) for value in data.values()]
            print(", ".join(values))
            print()
        print()
    input("Press Enter to Continue...")
    
def Option2():
    os.system("clear")
    print("You have selected Option 2\n")
    
    file_path = input("Enter the file path where you want to save the CSV file: ")
    
    field_names = []
    count = 1
    
    while True:
        column = input(f"Enter the name of column #{count}: ")
        field_names.append(column)
        
        stop = input("Do you want to continue? (Type 'n' to stop, any other key to continue): ")      
        if stop.lower()== "n":
            break
        
        count +=1
    input("Press Enter to Continue...")
    
    if csv_manager.create_csvfile(file_path, field_names):
        add_data_option = input("Do you want to add data? (Type 'Y' for yes, any other key for no): ")
        
        while add_data_option.lower() == "y":
            data = {}
            
            for field in field_names:
                value = input(f"Enter data for {field}: ")
                data[field] = value
                        
            csv_manager.add_data(file_path, data, field_names)
           
            continue_add_data = input("Do you want to continue adding data? (Type 'n' to stop, any other key to continue): ")
            if continue_add_data.lower() == "n":
                add_data_option = "n"

    input("Press Enter to Continue...")
    

def Option3():
    os.system("clear")
    print("You have selected Option 3")
    
    file_path = input("Enter the absolute filepath: ")
    old_value = input("Enter the old value: ")
    
    occurrences = csv_manager.search_occurrences(file_path, old_value)
    
    if occurrences:
        for index, row in enumerate(occurrences):
            print(f"{index}: {row}")
            
        while True:
            try:
                opt = int(input("Enter the number of the row that you want to change the value: "))
                if 0 <= opt < len(occurrences):
                    break
                else:
                    print("Enter a valid value within the range.")
            except ValueError:
                print("Enter a valid integer.")
            
        print(f"Selected row: {occurrences[opt]}")
        
        new_value = input("Enter the new value: ")
        
        new_row = csv_manager.change_value(occurrences[opt], old_value, new_value)
        
        csv_manager.updated_data(file_path, occurrences[opt], new_row)
        
    input("Press Enter to Continue...")
        
def Option4():
    os.system("clear")
    print("You have selected Option 4")
    
    new_folder_path = input("Enter the folder path you want to create: ")
    
    if file_manager.create_folder(new_folder_path):
        print("Folder path created successfully.")
    input("Press Enter to Continue...")
    
def Option5():
    os.system("clear")
    print("You have selected Option 5")
    
    file_path = input("Enter the file path you want to delete: ")
    
    file_manager.delete_file(file_path)
    input("Press Enter to Continue...")
    

def Option6():
    os.system("clear")
    print("You have selected Option 6")
    
    folder_path = input("Enter the folder path you want to delete: ")
    
    file_manager.delete_folder(folder_path)
    input("Press Enter to Continue...")
        
    
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

while True:
    os.system("clear")
    
    print("\n=== Menu ===")
    print("1. Read CSV File")
    print("2. Create a CSV File")
    print("3. Update Data")
    print("4. Create Folder")
    print("5. Delete File")
    print("6. Delete Folder")
    print("7. Exit")

    try:
        Option = int(input("Enter the number of the option you want: "))

        if Option == 1:
            Option1()
        elif Option == 2:
            Option2()
        elif Option == 3:
            Option3()
        elif Option == 4:
            Option4()
        elif Option == 5:
            Option5()
        elif Option == 6:
            Option6()
        elif Option == 7:
            exit_program()
        else:
            print("Invalid option. Try again.")

    except ValueError:
        print("Please enter a valid number.")
