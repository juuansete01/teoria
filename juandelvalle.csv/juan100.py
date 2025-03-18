import pandas as pd

# Ruta al archivo CSV
df = pd.read_csv ('nombres.csv')
# mosrar los 10 primeros
print(df["nombre"].head(100))