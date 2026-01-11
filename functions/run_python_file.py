import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_target = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_dir):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_dir]
    if args:
        command.extend(args)
    try:
        completed_process = subprocess.run(command,capture_output=True,text=True,timeout=30)
        ret_string = ""
        if completed_process.returncode != 0:
            ret_string += f"Process exited with code {completed_process.returncode}"
        if not completed_process.stdout and not completed_process.stderr:
            ret_string += f"No output produced"
        else:
            if completed_process.stdout:
                ret_string += f" STDOUT: {completed_process.stdout}"
            if completed_process.stderr:
                ret_string += f" STDERR: {completed_process.stderr}"
        return ret_string
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs specified python function if it exists",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the .py file to execute",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of string arguments to pass to the script",
                items=types.Schema(
                    type=types.Type.STRING,
                )
            ),
        },
        required=["file_path"]
    ),
)