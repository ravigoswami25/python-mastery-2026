import pandas as pd

data = {
    "name": ["Ravi","Aman","Neha"],
    "age": [25,30,22],
    "salary": [50000,60000,45000]
}

df = pd.DataFrame(data)

print(df)

df = pd.read_csv("data.csv")
print(df)


