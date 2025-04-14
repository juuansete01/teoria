import matplotlib.pyplot as plt
import pandas as pd
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,5,8,11,13,16,19,22,25,28] 
plt.scatter(x,y,color= 'blue', marker= 'o')
plt.xlabel('eje x')
plt.ylabel('eje y')
plt.title('graficos')
plt.show()