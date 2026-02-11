import os
from helper import path_controller

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs, target_dir, valid_target_dir = path_controller(working_directory, file_path)

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        parent = os.path.dirname(target_dir)
        os.makedirs(parent, exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"