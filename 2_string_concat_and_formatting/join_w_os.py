#! usr/bin/env python3

import os

location_of_file = "/Users/carsoncook/PythonProjects/IntermediatePython/2_string_concat_and_formatting"

file_name = "random_file.txt"

print("YOUR FILEPATH:\n")
print("/".join([location_of_file, file_name]))

print("Your file says:\n")

with open(os.path.join(location_of_file, file_name)) as f:
    print(f.read())


