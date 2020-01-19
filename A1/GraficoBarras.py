import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 7, 1, 10]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

#Titulo / Legendas
plt.title("Comparaçao de gráficos de barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()

plt.show()