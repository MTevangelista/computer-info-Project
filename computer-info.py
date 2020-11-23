import psutil
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import platform

option = input(
    'Digite 1 para visualizar o gráfico da porcentagem do uso de memória:\n'
    'Digite 2 para visualizar o gráfico da porcentagem do uso de CPU:\n'
    'Digite 3 para visualizar o gráfico da porcentagem do uso de disco:\n'
)

def show_machine_ip():
    dict_interfaces = psutil.net_if_addrs()
    return dict_interfaces['Ethernet'][0].address

plt.title(
    'Monitoramento e Análise do Computador\n'
    f'{platform.processor()}'
)
plt.ylabel(f'IP: {show_machine_ip()}\n')
plt.ylim(0, 100)

def show_memory_usage_graph():
    values = []
    time = int(input('Digite o tempo de monitoramento:\n'))
    memory = psutil.virtual_memory()
    capacity = round(memory.total/(1024*1024*1024), 2) # convert to GB

    for i in range(time-1, -1, -1):
        plt.xlabel(
            f"Tempo de monitoramento: {i}\n"
            f"Total de memória: {capacity} GB"
        )
        memory = psutil.virtual_memory().percent
        values.append(memory)
        plt.plot(values, 'r-o')
        plt.pause(1)
    
    plt.xlabel(
        f"Monitoramento finalizado com sucesso!\n"
        f"Total de memória: {capacity} GB"
    )
   
def show_cpu_usage_graph():
    values = []
    time = int(input('Digite o tempo de monitoramento:\n'))

    for i in range(time-1, -1, -1):
        plt.xlabel(f"Tempo de monitoramento: {i}")
        cpu = psutil.cpu_percent(interval=0.5)
        values.append(cpu)
        plt.plot(values, 'r-o')
        plt.pause(0.5)
          
    plt.xlabel(f"Monitoramento finalizado com sucesso!")  
   
def show_disk_usage_graph():
    values = []
    time = int(input('Digite o tempo de monitoramento:\n'))
    disk = psutil.disk_usage('.')
    total = round(disk.total/(1024*1024*1024), 2) # convert to GB
    in_use = round(disk.used/(1024*1024*1024), 2) # convert to GB
    free = round(disk.free/(1024*1024*1024), 2) # convert to GB

    for i in range(time-1, -1, -1):
        plt.xlabel(
            f"Tempo de monitoramento: {i}\n"
            f"Total: {total} GB / Em uso: {in_use} GB / Livre: {free} GB"
        )
        disk = psutil.disk_usage('.').percent
        values.append(disk)
        plt.plot(values, 'r-o')
        plt.pause(1)
    
    plt.xlabel(
        f"Monitoramento finalizado com sucesso!\n"
        f"Total: {total} GB / Em uso: {in_use} GB / Livre: {free} GB"
    )
    
if int(option) == 1:
    plt.ion()
    show_memory_usage_graph()
    plt.ioff()
    plt.show()
elif int(option) == 2:
    plt.ion()
    show_cpu_usage_graph()
    plt.ioff()
    plt.show()
elif int(option) == 3:
    plt.ion()
    show_disk_usage_graph()
    plt.ioff()
    plt.show()
else:
    print("Opção inválida")