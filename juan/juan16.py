import pandas as pd
df = pd.read_csv('users.csv')
usuarios_alemanes = df[df['pais'] == 'Germany']
edad_media = usuarios_alemanes['edad'].mean()
print("Edad media de los usuarios de Alemania:", edad_media)
