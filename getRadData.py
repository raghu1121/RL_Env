import pandas as pd

df=pd.read_csv('pred_kaiserslautern.csv',usecols=[5,11,13,14])
#df=pd.read_csv('pred_19_06_2018_kaiserslautern.csv',usecols=[11,13,14])
year=pd.DatetimeIndex(df['time']).year
month=pd.DatetimeIndex(df['time']).month
day=pd.DatetimeIndex(df['time']).day
hour=pd.DatetimeIndex(df['time']).hour+pd.DatetimeIndex(df['time']).minute / 60
df['month']=month
df['day']=day
df['hour']=hour
df['year']=year

#df=df[(df.Diffuse_Strahlung > 50) | (df.Direkt_Strahlung > 50)]
df=df[df.Globalstrahlung > 2]
df=df[df.year < 2016]
df=df.round({'Direkt_Strahlung': 0, 'Diffuse_Strahlung': 0,'hour':2})
df=df[['month','day','hour','Direkt_Strahlung','Diffuse_Strahlung','year']]
df.to_csv('kaiserslautern.wea', sep=',', index=False)
#df.to_csv('kaiserslautern_19_06_2018.wea', sep=',', index=False)

