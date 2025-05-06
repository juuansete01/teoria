import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("users.csv")
conteo_genero = df['genero'].value_counts()
colores = ['#66c2a5', '#fc8d62', '#8da0cb']  # Ajusta según cuántos géneros tengas

plt.figure(figsize=(6, 6))
plt.pie(conteo_genero, labels=conteo_genero.index, colors=colores, autopct='%1.1f%%', startangle=90)
plt.title('Distribución por género')
plt.axis('equal')
plt.show()
