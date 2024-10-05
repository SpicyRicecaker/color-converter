from tivars.models import *
from tivars.types import *
from tivars.var import *

import csv
import json


# Path to your .8xl file
input_path = "./8xl_files/L1.8xl"
output_path = "output.csv"

my_var = TIVar.open(input_path)

with open(input_path, 'rb') as file:
    my_var.load_var_file(file)
    
    # file.seek(0)
    # my_var.load_bytes(file.read())

    numbers = str(my_var.entries[0])[1:-1].split(', ')
    numbers = list(map(lambda s : float(s), numbers))
    print(numbers)


# Load the TI list file
# ti_file = TIVar.open(input_path)
# print(dir(ti_file))
# print(dir(ti_file.entries))
# data = ti_file.contents.data

# # Write the list data to a CSV file
# with open(output_path, 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(data)

# print(f"List data exported to {output_path}")
