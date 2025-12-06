import pandas as pd

dfk = pd.read_csv('Exc 2.csv')
print(dfk.to_string())

print(pd.options.display.max_rows)