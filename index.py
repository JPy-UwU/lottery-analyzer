# Importing data from Excel file
import pandas as pd
df = pd.read_excel(r"data.xlsx", index_col=None, na_values=['NA'], usecols = "A")

data = df.value_counts()
print(data)

# creating dictionary of dictionary
dict = {}

for i in range(50):
    dict[i] = 0
    

print(dict)