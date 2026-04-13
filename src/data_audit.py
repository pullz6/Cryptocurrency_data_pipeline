from data_import import importing_to_df
from datetime import datetime 
dt = datetime.now()
df = importing_to_df()
print(df.info())
df_test = df[df['date'] > '2026-04-07']
print(df_test)