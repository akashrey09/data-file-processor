import os
def validate_file(path):

    if os.path.exists(path):
        print("Path exists!")
        _, ext = os.path.splitext(path)
        if ext.lower() == ".csv":
            print("Extension matches!")
        else:
            raise ValueError("Error: File must be a .csv file.")
    else:
        raise FileNotFoundError("Error: File not found.")
        
    
    
    