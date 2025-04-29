import pandas as pd
df = pd.read_csv('users.csv')
conteo_generos = df['genero'].value_counts()
print(conteo_generos)
