import pandas as pd
df = pd.read_csv('users.csv')
usuarios_40_50 = df[df['edad'].between(40, 50)]
print(usuarios_40_50)
