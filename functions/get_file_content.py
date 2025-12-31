import os

def get_file_content(working_directory, file_path):

    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    try:
        with open(target_dir,"r") as file:
            file_content_string = file.read(MAX_CHARS)
            if file.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"