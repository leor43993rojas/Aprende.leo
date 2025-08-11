'Hola, iPad'
# main.py
import numpy as np, pandas as pd

df = pd.DataFrame({"x": np.arange(1,6), "y": [2,1,3,5,4]})
df["z"] = df["x"] * df["y"]
print(df)
print("numpy:", np.version, "pandas:", pd.version)
