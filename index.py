# Importing data from Excel file
import pandas as pd
df = pd.read_excel(r"data.xlsx", index_col=None, na_values=['NA'], usecols = "A")



