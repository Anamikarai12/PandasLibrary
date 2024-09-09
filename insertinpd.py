import pandas as pd
var=pd.DataFrame({"A":[1,2,3],"B":[2,3,4]})
var.insert(1,"New",[5,6,7])
#copy limited data
var["ppython"]=var["A"][:1]
print(var)