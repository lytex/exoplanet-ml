import os
import shutil
import pandas as pd

TCE_CSV_FILE = os.environ.get("TCE_CSV_FILE", os.environ["HOME"] + "/astronet/dr24_tce.csv")
i = 0
with open(TCE_CSV_FILE) as f:
    for i, line in enumerate(f.readlines()):
        if not line.startswith("#"):
            break

df = pd.read_csv(TCE_CSV_FILE, skiprows=i)
if "rowid" not in df.columns:
    df["rowid"] = df.index + 1
    shutil.copy(TCE_CSV_FILE, TCE_CSV_FILE + ".original")
    df = df[df.columns.drop("rowid").insert(0, "rowid")]
    df.to_csv(TCE_CSV_FILE, index=False)


cols = {"rowid", "kepid", "tce_plnt_num", "tce_period", "tce_time0bk", "tce_duration", "av_training_set"}

if not set(df.columns.intersection(cols)) == cols:
    print(f"Missing columns: {cols.difference(df.columns)}")
