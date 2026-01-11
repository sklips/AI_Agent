import os
from google.genai import types

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_target = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_dir):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        os.makedirs(os.path.dirname(target_dir),exist_ok=True)
        with open(target_dir,"w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to specified file, creating directories as needed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                 description="Path of file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                   description="Content to write to file",
            )
         },
         required=["file_path", "content"]
     ),
 )