import pandas as pd
t1 = pd.Series([1,9,0,8,7])
print(t1)
t2 = pd.Series([1,2,4,1],index=list("abcd"))
print(t2)
temp_d = {"name":"cpq","age":"20","sex":"male"}
t3 = pd.Series(temp_d)
print(t3)
for i in t3.index:
    print(i)
for k in t3.values:
    print(k)