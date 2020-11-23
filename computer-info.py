import psutil
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

option = input(
    'Digite 1 para visualizar o gráfico da porcentagem do uso de memória:\n'
    'Digite 2 para visualizar o gráfico da porcentagem do uso de CPU:\n'
    'Digite 3 para visualizar o gráfico da porcentagem do uso de disco:\n'
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

def show_cpu_usage_graph():
    values = []
    for i in range(5):
        cpu = psutil.cpu_percent(interval=1)
        values.append(cpu)

    plt.plot(values)
    plt.show()

def show_disk_usage_graph():
    values = []
    for i in range(5):
        disk = psutil.disk_usage('.')
        values.append(disk)
    
    plt.plot(values)
    plt.show()

if int(option) == 1:
    show_memory_usage_graph()
elif int(option) == 2:
    show_cpu_usage_graph()
elif int(option) == 3:
    show_disk_usage_graph()
else:
    print("Opção inválida")