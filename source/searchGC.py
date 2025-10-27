#!usr/bin/env python
import pandas as pd
import os
import re
import io
import time
from ast import literal_eval

my_dir = "~/GC_4" # this is where the corpus lies already unzipped and split with mysplit
files = sorted([os.path.join(my_dir, file) for file in os.listdir(my_dir) if file.startswith("de_head")])
print(files)

# compile one regex to find them all
regexes = pd.read_excel("../GeflügelteWorte.ods", engine="odf")

sep = "[-,.:;'’?!/ –\\r\\n]+"
word = "\\w+"
regex = "|".join(regexes.regex) + "|" + "|".join(regexes[regexes.regex2.notna()].regex2)
regex = regex.replace("#", sep).replace("%", word)
regex = re.compile("(" + regex + ")")
print(regex)

# test whether all quotes are found with the corresponding regex
regexes["test"] = regexes.Redewendung.str.extract(regex)
print(regexes[regexes.test.isna()])

# look for quotes in corpus, write findings to pickle file
min_date_list = []
max_date_list = []
start = time.time()
for i, file in enumerate(files):
    iter_start = time.time()
    with open(file, "r") as text:
        a = text.readlines()
    print(len(a))
    df = pd.DataFrame.from_dict([literal_eval(x) for x in a])
    print(df.info())
    df.source_domain.value_counts().to_pickle(re.sub(".*/", "search_results/", file) + "_urls")
    min_date, max_date = df.date_download.min(), df.date_download.max()
    min_date_list.append(min_date)
    max_date_list.append(max_date)
    print(len(df), min_date, max_date)
    step = time.time()
    print("Reading and preparation took", step-iter_start, "s")

    df["hasQuote"] = df['raw_content'].str.extract(regex)
    results = df[df["hasQuote"].notna()]
    print(results.info())
    print(results.head())
    print(results.source_domain.value_counts()[:10])
    results.to_pickle(re.sub(".*/", "search_results/", file) + "_result")
    iter_end = time.time()
    print("First file took", iter_end-iter_start, "s")
end = time.time()
print("Total search took", end-step, "s")
print("Downloaded between", min(min_date_list), "and", max(max_date_list))
print(end-start, "s")
