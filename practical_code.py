import pandas as pd
Data={
    "name":["Saransh Rai","Rohit Singh","Yash Mittal","Sumit Gupta"],
    "Age":[21,22,23,24],
    "profession":["Programmer","Police Officer","Business Man","Buiseness Man"],
    "Anual Income":[5000000,6000000,6000000,7000000]
}
df=pd.DataFrame(Data)
df.index=range(1,len(df)+1)
print(df[["name","profession","Age"]])
print(df.loc[1:3,["name","profession","Age"]])