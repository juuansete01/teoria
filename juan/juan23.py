import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

plt.figure(figsize=(8, 5))
plt.hist(df["math score"], bins=10, color='green', edgecolor='black')
plt.title("Distribución de puntajes de Matemáticas")
plt.xlabel("Puntaje")
plt.ylabel("Cantidad de estudiantes")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
