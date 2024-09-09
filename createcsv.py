import pandas as pd
dis={"A":[1,2,3,4],"B":[2,3,4,5],"C":[4,5,6,7]}
d=pd.DataFrame(dis)
print(d)
# d.to_csv("a.csv")
# d.to_csv("a1.csv",index=False)
d.to_csv("a2.csv",index=False,header=[1,2,3])
