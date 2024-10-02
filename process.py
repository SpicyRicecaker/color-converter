import pandas as pd
import numpy as np
import json

df = pd.read_csv("data.csv", dtype={"Date": str})


# output should be dict
# leaf type into an two array of objects, one for front, one for back
# each object has date and l, a, b properties

o = {}


# print(df.head())

current_date = None
current_face = None
current_type = None

updated_date = False

sum = {"n": 0, "l": 0, "a": 0, "b": 0}

for i, r in df.iterrows():
    [local_date, local_face, local_type, l, a, b] = [
        r["Date"],
        r["Face"],
        r["Type"],
        r["L"],
        r["A"],
        r["B"],
    ]

    # if we have a new face
    #   do not add or change any values
    # or we are at the end of the dataframe
    #   change values

    # calculate the average lab, add value
    # add datum
    # reset

    if not r.isnull()["Face"] and i != 0:
        avg = {
            "l": sum["l"] / sum["n"],
            "a": sum["a"] / sum["n"],
            "b": sum["b"] / sum["n"],
        }
        sum = {"n": 0, "l": 0, "a": 0, "b": 0}

        if not current_type in o:
            o[current_type] = {}
        if not current_face in o[current_type]:
            o[current_type][current_face] = []

        o[current_type][current_face].append(
            {"date": current_date, "l": avg['l'], "a": avg['a'], "b": avg['b']}
        )

    if not r.isnull()["Date"]:
        current_date = local_date
    if not r.isnull()["Face"]:
        current_face = local_face
    if not r.isnull()["Type"]:
        current_type = local_type

    sum["l"] += r["L"]
    sum["a"] += r["A"]
    sum["b"] += r["B"]
    sum["n"] += 1

    if i == len(df) - 1:
        o[current_type][current_face].append(
            {"date": current_date, "l": l, "a": a, "b": b}
        )

with open("./static/data.json", "w") as outfile:
    json.dump(o, outfile)
