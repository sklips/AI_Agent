from functions.run_python_file import *

print("Result for main.py")
print(run_python_file("calculator","main.py"))

print("Result for main.py with arguments")
print(run_python_file("calculator","main.py",["3 + 5"]))

print("Result for calculator tests.py ")
print(run_python_file("calculator","tests.py"))

print("Result for illegal directory ../main.py")
print(run_python_file("calculator","../main.py"))

print("Result for nonexistant file")
print(run_python_file("calculator","nonexistent.py"))

print("Result for non .py file")
print(run_python_file("calculator","lorem.txt"))