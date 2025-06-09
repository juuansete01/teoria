import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("users.csv")

españa = df[df["pais"] == "Spain"]

total = len(españa)

conteo_genero = españa["genero"].value_counts()

print(f"Total en España: {total}")
print(conteo_genero)

conteo_genero.plot(kind='bar', color=['skyblue', 'lightpink'])
plt.title(f"Usuarios en España: {total}")
plt.xlabel("Género")
plt.ylabel("Cantidad de Personas")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
