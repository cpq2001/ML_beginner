import numpy as np
import pandas as pd
# CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。
# CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。
# df = pd.read_csv("./data/dogNames2.csv")
# print(df)
t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("abcd"))
print(t)