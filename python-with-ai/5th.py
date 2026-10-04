import pandas as pd

data = {
    "name" : ["Chaithra","Vanitha","Nayana"],
    "age" : [19,21,17],
    "marks" : [95,95,88]
}

df = pd.DataFrame(data)
print(df.iloc[0,1])