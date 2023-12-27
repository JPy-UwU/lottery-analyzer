# Importing data from Excel file
import pandas as pd
df = pd.read_excel(r"data.xlsx", index_col=None, na_values=['NA'], usecols = "A")

# creating dictionary of dictionary
frequency_dict = {}
data_dict = {}

# initializing the dictionary
for i in range(1, 51):
  frequency_dict[i] = 0

# initializing the dictionary of dictionary
for i in range(1, 51):
  data_dict[i] = frequency_dict.copy()

# creating frequency dictionary
for i in df.values:
  frequency_dict[i.item()] += 1

# creating data dictionary
for i in range(0, df.values.size, 8):
  flattened = df.values[i:i+8].flatten()
  # print(flattened)

  for j in flattened:
    for k in range(8):
      if j != flattened[k]:
        data_dict[flattened[k]][j] += 1

# printing the frequency dictionary
# for (key, value) in frequency_dict.items():
#   print(key, " : ", value)

# for (key, value) in data_dict.items():
#   for (key1, value1) in value.items():
#     if (value1 > 0):
#       print(key, " => ", key1, " : ", value1)

df1 = pd.DataFrame.from_dict(data_dict)
df2 = pd.DataFrame.from_dict(frequency_dict, orient='index')

# exporting the data to excel file
with pd.ExcelWriter('output.xlsx') as writer:
  df1.to_excel(writer, sheet_name='Sheet1')
  df2.to_excel(writer, sheet_name='Sheet2')