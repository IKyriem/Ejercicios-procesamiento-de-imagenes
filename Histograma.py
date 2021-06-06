from random import random
import matplotlib.pyplot as plt


#Datos aleatorios para el ejemplo
mos = [int(random()*100) for _ in range(3000)]

plt.title('MOS')
plt.hist(mos, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
plt.grid(True)
plt.show()
plt.clf()