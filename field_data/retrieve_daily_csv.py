from tivars.models import *
from tivars.types import *
from tivars.var import *
import pandas as pd
import numpy as np

import csv
import json

column_name = {
    1: "L",
    2: "A",
    3: "B",
    4: 'Type',
    5: "Face"
}

type_name = {
    1: "jp maple",
    2: "tulip tree",
    3: "american elm",
    4: "red maple",
    5: "quaking aspen"
}

face_name = {
    1: 'f',
    0: 'b'
}

output_path = "output.csv"

df = pd.DataFrame()

# bob doesn't want to waste space in his csv sheet
# when he records a new number in a column, he assumes that the following rows in that column has the same number, until he records a new number in that column
# help him save space by converting redundant (same) numbers in an array to None
def conv(A):
    if len(A) <= 1:
        return A
    
    prev = A[0]

    for i in range(1, len(A)):
        if A[i] == prev:
            A[i] = None
        elif A[i] != prev:
            prev = A[i]
    return A

for i in range(1, 6):
    # Path to your .8xl file
    input_path = f"./8xl_files/L{i}.8xl"

    my_var = TIVar.open(input_path)
    with open(input_path, 'rb') as file:
        my_var.load_var_file(file)


        row = str(my_var.entries[0])[1:-1].split(', ')
        row = list(map(lambda s : float(s) if i in [1, 2, 3] else int(s), row)) 
        # print(numbers)
        if column_name[i] == 'Type':
            row = list(map(lambda n : type_name[n] if n != 0 else "", row))
        if column_name[i] == 'Face':
            row = list(map(lambda x: face_name[x] if not (x is None) else "", conv(row)))
            # print(row)
        df[column_name[i]] = row

df.to_csv('daily.csv', index=False)

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
