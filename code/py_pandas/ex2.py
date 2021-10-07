import numpy as np
import pandas as pd
# df = pd.read_csv("./data/dogNames2.csv")
# print(df)
t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("abcd"))
print(t)