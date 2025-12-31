from functions.write_file import *

print("Result from test writing to lorem.txt")
print(write_file("calculator","lorem.txt","wait, this isn't lorem ipsum"))

print("Result from test writing morelorem")
print(write_file("calculator","pkg/morelorem.txt","lorem ipsum dolor sit amet"))

print("Result from test writing to file outside permitted area")
print(write_file("calculator","/tmp/temp.txt","this should not be allowed"))