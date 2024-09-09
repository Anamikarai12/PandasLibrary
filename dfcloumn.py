import pandas as pd
x={"0":[1,2,3,4,5],"1":[1,2,3,4,5]}
a=pd.DataFrame(x,columns=["0"])
print(a)
print(a["0"][1])