from model import model
import pandas as pd
import numpy as np
import tomllib
from pathlib import Path
import math

with open(Path("config.toml"), "rb") as f:
    config = tomllib.load(f)

data_path = config["data_path"]["data_path"]
df = pd.read_csv(data_path)

x_0, P_00 = np.array(config["initial_value"]["x_0"]), np.array(config["initial_value"]["x_0"])
prop = config["train_sumple"]["proportion"]

x, P , predict_lst= model(x_0, P_00, prop)


