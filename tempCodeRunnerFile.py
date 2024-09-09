import pandas as pd
a=[1,2,3,1,4]
#print(pd.Series(a))
x=pd.Series(a,index=["a","b","c","d","e"],dtype="float" , name="Python")
print(x)

