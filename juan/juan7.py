import matplotlib.pyplot as plt
datos = [25,35,20,20]
color = ["gold","lightcoral","lightskyblue","lightgreen"]
label = ["a","b","c","d"]
plt.pie(datos,labels = label, colors = color, autopct= '%1.1f%%', startangle= 140)
plt.axis("equal")
plt.show()