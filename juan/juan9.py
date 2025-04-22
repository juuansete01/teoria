import pandas as pd
import numpy as np
df = pd.read_csv('StudentsPerformance.csv')
df["nueva columna"]=70 #crear columna nueva
a=np.arange(0,1000)
df["columnadearreglo"]=a
print(df)