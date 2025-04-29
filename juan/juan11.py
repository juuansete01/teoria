import pandas as pd
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
a=np.random.randint(1,100, size=1000)
df ["columna de arreglo"] = a
print(df)