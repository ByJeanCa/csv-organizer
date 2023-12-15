import os

class FileManager:

    @staticmethod
    def create_folder(folder_path):
        try:
            os.mkdir(folder_path)
            return True
        except Exception as e:
            print(f"Error creating folder: {e}")
            return False
        
    @staticmethod     
    def delete_folder(folder_path):
        try:
            os.rmdir(folder_path)
            print(f"File '{folder_path}' deleted successfully.")
            return True
        except Exception as e:
            print(f"Error deleting folder: {e}")
            return False
            
    @staticmethod       
    def delete_file(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
            
        