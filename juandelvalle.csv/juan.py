import pandas as pd

# Ruta al archivo CSV
df = pd.read_csv ('nombres.csv')

print(df.tail(20))