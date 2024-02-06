import pandas as pd 

df = pd.read_csv('.learn/assets/us_baby_names_right.csv')

grouping = df.groupby('Name').sum()

result = len(grouping)

print(result)

