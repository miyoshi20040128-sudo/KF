from predict import x, P, predict_lst
import pandas as pd
import tomllib
from pathlib import Path
import math
import matplotlib.pyplot as plt

with open(Path("config.toml"), "rb") as f:
    config = tomllib.load(f)

data_path = config["data_path"]["data_path"]
df = pd.read_csv(data_path)

length = len(df) 
actual_lst = df["observed_sales"]

print(len(predict_lst),len(actual_lst))

plt.plot(predict_lst, label ="predict")
plt.plot(actual_lst, label = "actual")
plt.legend()


plt.savefig("output/predict vs acutual.png")
