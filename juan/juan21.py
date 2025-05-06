import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('users.csv')

# Contar cuántos hombres y mujeres hay
conteo = df['genero'].value_counts()

# Mostrar los resultados
print(conteo)

# Crear un gráfico circular (pie chart)
plt.figure(figsize=(6, 6))
plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
plt.title('Distribución de Hombres y Mujeres')
plt.show()
