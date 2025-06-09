import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('users.csv')

# Normalizar valores de 'genero'
df['genero'] = df['genero'].str.strip().str.lower()

# Filtrar usuarios mayores de 50
mayores_50 = df[df['edad'] > 50]

# Contar cuántos hay por género
conteo_genero = mayores_50['genero'].value_counts()

# Crear el gráfico de barras
conteo_genero.plot(kind='bar', color=['skyblue', 'lightcoral'])

# Personalizar el gráfico
plt.title('Usuarios mayores de 50 por género')
plt.xlabel('Género')
   