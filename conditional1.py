import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
var["python"]=var["A"]<=3
var["python_1"]=var["B"]>=3
print(var)