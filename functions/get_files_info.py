import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

    except Exception as e:
        return f"Error: {e}"

    items = os.listdir(target_dir)
    lines = []
    for item in items:
        try:
            path = os.path.join(target_dir, item)
            is_dir = os.path.isdir(path)
            size = os.path.getsize(path)
            lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        except Exception as e:
            lines.append(f"Error: {e}")
    
    return "\n".join(lines)