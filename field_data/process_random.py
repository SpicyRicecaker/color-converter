import pandas as pd
import numpy as np
import json
import helper


def is_null_or_empty(value):
    if isinstance(value, str):
        return value.strip() == ""
    return pd.isna(value)


def main():
    df = pd.read_csv("random.csv")

    # output should be dict
    # leaf type into an two array of objects, one for front, one for back
    # each object has date and l, a, b properties

    o = {}

    # print(df.head())

    current_type = None

    for i, r in df.iterrows():
        [l, a, b, local_type] = [
            r["l"],
            r["a"],
            r["b"],
            r["type"],
        ]

        current_face = "f" if i % 2 == 0 else "b"

        # print(
        #     "\t\t".join(
        #         map(
        #             lambda x: f"\"{str(x)}\"",
        #             [
        #                 r["Date"],
        #                 r["L"],
        #                 r["A"],
        #                 r["B"],
        #                 r["Type"],
        #                 r["Face"],
        #             ],
        #         )
        #     )
        # )

        # if we have a new face
        #   do not add or change any values
        # or we are at the end of the dataframe
        #   change values

        # calculate the average lab, add value
        # add datum
        # reset

        if not r.map(is_null_or_empty)["type"]:
            current_type = local_type

        if not current_type in o:
            o[current_type] = {}
        if not current_face in o[current_type]:
            o[current_type][current_face] = []


        o[current_type][current_face].append({"date": "10/14", "l": l, "a": a, "b": b})

    with open("../static/random.json", "w") as outfile:
        json.dump(o, outfile)


if __name__ == "__main__":
    main()
