import pandas as pd

name='Potsdam'
df = pd.read_csv(name+'.wea', delimiter=' ',skiprows=6,header=None)
df =df[df.iloc[:,4] > 0]
print(df.iloc[:,4].size * 64 * 4)