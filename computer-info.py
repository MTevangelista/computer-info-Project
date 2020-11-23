import psutil
import numpy as np 
import matplotlib.pyplot as plt

option = input(
    'Digite 1 para visualizar o gráfico da porcentagem do uso de memória:\n'
)

plt.title("Monitoramento e Análise do Computador")
plt.ylim(0, 100)

def show_memory_usage_graph():
    values = []
    for i in range(10):
        memory = psutil.virtual_memory()
        values.append(memory)
   
    plt.plot(values)
    
    plt.show()


if int(option) == 1:
    show_memory_usage_graph()
else:
    print("Opção inválida")