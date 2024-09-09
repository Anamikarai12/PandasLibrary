import pandas as pd
x=pd.Series(12,index=[1,2,3,4,5])
x1=pd.Series([10,8,12],index=[1,2,3])
print(x+x1)
