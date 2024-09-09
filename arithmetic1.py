import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[2,3,4,5]})
#Add
var["sum"]=var["A"]+var["B"]
#sub
var["sub"]=var["A"]-var["B"]
#mul
var["mul"]=var["A"]*var["B"]
#div
var["div"]=var["B"]//var["A"]
print(var)