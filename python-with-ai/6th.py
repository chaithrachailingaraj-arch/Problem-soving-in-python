import pandas as pd

data = {
    "name" : ["Chaithra","Vanitha","Nayana"],
    "age" : [19,21,17],
    "Marks" : [95,95,88]
}

df = pd.DataFrame(data)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())
print(df.head(2))
print(df.tail(2))
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Marks"].sum())
print(df["Marks"].count())