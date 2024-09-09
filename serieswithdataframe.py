import pandas as pd
sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([2,3,4,5])}
z=pd.DataFrame(sr)
print(z)