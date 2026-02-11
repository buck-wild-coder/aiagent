import os
import subprocess
from helper import path_controller
def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs, target_dir, valid_target_dir = path_controller(working_directory, file_path)

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if target_dir[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_dir]

        if args:
            command.extend(args)

        complete_process = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)

        if complete_process.returncode != 0:
            return f"Process exited with code {complete_process}"

        if (complete_process.stdout or complete_process.stderr) == None:
            return "No output produced"
        
        lst = []
        output = complete_process.stdout
        error = complete_process.stderr

        if output:
            lst.append(f"STDOUT: {output}")
        if error:
            lst.append(f"STDERR: {error}")
        
        return "\n".join(lst)

    except Exception as e:
        return f"Error: {e}"
