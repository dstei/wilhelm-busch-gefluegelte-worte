#!usr/bin/env python
import pandas as pd
import os
import re
import io
import time
from ast import literal_eval

def good_toulmin(m, i, phi):
        t = m/sum(phi)
        f1 = pow((-t), (i+1))
        f2 = phi
        if len(f1) != len(f2):
            raise ValueError("i and phi have different lengths!")
        return sum([f1[x] * f2[x] for x in range(len(f1))])

if __name__ == "__main__":
    data = pd.read_excel("../GeflügelteWorte.ods", engine="odf")
    stats = data.Punkte.value_counts().reset_index()
    entries = 40

    expected_new_quotes = good_toulmin(entries, stats["index"], stats["Punkte"])

    print(f"In a new collection with {entries} entries, we expect to find {expected_new_quotes} new entries, i.e. not yet seen quotes.")
