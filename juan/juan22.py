import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv('users.csv')

# Filtrar datos
filtered_df = df[
    ((df['pais'] == 'Canada') | (df['pais'] == 'Germany') | (df['pais'] == 'France')) &
    (df['edad'] > 30) &
    (df['nombre'].notnull()) & (df['nombre'] != '')
]

# Contar usuarios por país
counts = filtered_df['pais'].value_counts()

# Crear lista de colores diferentes (puedes personalizarlos)
colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'violet']

# Graficar
plt.figure(figsize=(8, 6))
counts.plot(kind='bar', color=colors[:len(counts)], edgecolor='black')
plt.title('Usuarios mayores de 30 por país')
plt.xlabel('País')
plt.ylabel('Cantidad de usuarios')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
