import pandas as pd     
df = pd.read_csv('StudentsPerformance.csv') 
print (df[["math score"," reading score","writing score"]].head(100))
print (df[["math score"," reading score","writing score"]].min())
print (df[["math score"," reading score","writing score"]].max())
print (df[["math score"," reading score","writing score"]].mean())
print (df[["math score"," reading score","writing score"]].dtypes)
print(f'Número de filas y columnas: {df.shape}')
print(df.to_string())