import pandas as pd
import numpy as np
import tomllib
from pathlib import Path
import math

with open(Path("config.toml"), "rb") as f:
    config = tomllib.load(f)

data_path = config["data_path"]["data_path"]
df = pd.read_csv(data_path)

#モデル設計
def model( x_0, P_00, prop):


    length = len(df)
    train_length = math.floor(len(df) * prop)

    #初期値
    x = np.array(x_0)
    P = np.array(P_00)
    A, H = np.array(config["initial_value"]["A"]), np.array(config["initial_value"]["H"])
    Q, R = config["initial_value"]["Q"], np.array(config["initial_value"]["R"])
    vec_y = df["observed_sales"]

    #学習
    predict_lst = []
    for i in range(len(df)):
        x_prime = A @ x 
        y_prime = H @ x_prime
        P_prime = A @ P @ A.T + Q
        S = H @ P_prime @ H.T + R
        K = P_prime @ H.T @np.linalg.inv(S)
        predict_lst.append((H @ x_prime).item())
        #更新
        x = x_prime + K @ (vec_y[i] - y_prime) 
        P = (np.eye(2) - K @ H) @ P_prime

    return x, P ,predict_lst


