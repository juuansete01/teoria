import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('users.csv')

# Normalizar texto
df['pais'] = df['pais'].str.strip().str.lower()
df['genero'] = df['genero'].str.strip().str.lower()

# Filtrar usuarios de United Kingdom
uk_users = df[df['pais'] == 'united kingdom']

# Obtener los 20 usuarios más viejos
top_20_uk = uk_users.sort_values(by='edad', ascending=False).head(20)

# Contar cuántos son male y female
conteo_genero = top_20_uk['genero'].value_counts()

# Crear gráfico de barras
conteo_genero.plot(kind='bar', color=['lightcoral', 'skyblue'])

# Personalizar el gráfico
plt.title('Género de los 20 usuarios más viejos de United Kingdom')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostrar gráfico
plt.tight_layout()
plt.show()
