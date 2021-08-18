import matplotlib.pyplot as plt
import math

x = []
y = []
numberOfX = int(input("Enter the number of x values"))
for q in range(numberOfX):
    x.append(q+1)
y = []
for i in range(len(x)):
    y.append(math.sin(i+1))
plt.plot(x, y, color = "green", marker = ".")
plt.title("Sin graph")
plt.grid()
plt.show()