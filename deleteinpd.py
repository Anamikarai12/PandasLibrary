import pandas as pd
var=pd.DataFrame({"A":[1,2,3],"B":[2,3,4],"C":[5,6,7]})
a=var.pop("B")
print(a)
print(var)

del var["A"]
print(var)