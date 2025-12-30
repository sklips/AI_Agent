from functions.get_file_content import *

print(f"Result for current lorem in calculator:")
print(get_file_content("calculator", "lorem.txt"))

print(f"Result for main.py:")
print(get_file_content("calculator", "main.py"))

print(f"Result for calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py"))

print(f"Result for outside working_dir:")
print(get_file_content("calculator", "/bin/cat"))


print(f"Result for nonexistant file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))

