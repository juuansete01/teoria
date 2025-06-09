import pandas as pd
import pandas as pd

df = pd.read_csv("users.csv")  

usuarios_francia = df[df["pais"] == "France"].head(5)

usuarios_jovenes_aus = df[df["pais"] == "Australia"].sort_values(by="edad").head(5)


print("Usuarios de Francia:")
print(usuarios_francia)

print("\nUsuarios más jóvenes de Australia:")
print(usuarios_jovenes_aus)
