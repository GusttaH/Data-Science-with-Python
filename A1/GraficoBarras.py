import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 10]

#Titulo / Legendas
plt.title("Meu primeiro gráfico com Python!")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x,y)
plt.show()