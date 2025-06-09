import numpy as np

datos = np.array([10, 20, 30, 40, 50])

media = np.mean(datos)
std = np.std(datos, ddof=1)    
varianza = np.var(datos, ddof=1)
mediana = np.median(datos)

print("Media:", media)
print("Desviación estándar (ddof=1):", std)
print("Varianza (ddof=1):", varianza)
print("Mediana:", mediana)
