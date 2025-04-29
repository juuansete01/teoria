import pandas as pd
df = pd.read_csv('users.csv')
primeros_5_mas_viejos = df[df['pais'] == 'Germany'].sort_values(by='edad', ascending=False).head(5)
print(primeros_5_mas_viejos)
