import os
from helper import path_controller

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs, target_dir, valid_target_dir = path_controller(working_directory, file_path)

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        MAX_CHARS = 10000
        with open(target_dir) as f:
            file_content_string = f.read(MAX_CHARS)
            content = ""

            if f.read(1):
                content = f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                
            return file_content_string
            
            
    except Exception as e:
        return f"Error: {e}"
        