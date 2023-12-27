# Importing data from Excel file
import pandas as pd
df = pd.read_excel(r"data.xlsx", index_col=None, na_values=['NA'], usecols = "A")

# creating dictionary of dictionary
frequency_dict = {}

# initializing the dictionary
for i in range(1, 51):
  frequency_dict[i] = 0

# creating frequency dictionary
for i in df.values:
  frequency_dict[i.item()] += 1


# printing the frequency dictionary
for (key, value) in frequency_dict.items():
  print(key, " : ", value)