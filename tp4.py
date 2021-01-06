import psutil
import matplotlib.pyplot as plt
import platform
import os
import socket 

option = input(
    'Tecle "Barra" para visualizar um resumo de todas as informações:\n'
    'Digite 0 para sair:\n'
    'Digite 1 para visualizar o gráfico da porcentagem do uso de memória:\n'
    'Digite 2 para visualizar o gráfico da porcentagem do uso de CPU:\n'
    'Digite 3 para visualizar o gráfico da porcentagem do uso de disco:\n'
)

def show_machine_ip():
    hostname = socket.gethostname()
    ip_internal = socket.gethostbyname(hostname)
    return ip_internal

def show_plt_title(scope): 
    plt.title(f'Monitoramento e Análise do Computador - {scope}\n')

plt.ylabel(f'IP: {show_machine_ip()}\n')
plt.ylim(0, 100)

def show_memory_usage_graph():
    values = []
    time = int(input('Digite o tempo de monitoramento:\n'))
    memory = psutil.virtual_memory()
    total = round(memory.total/(1024*1024*1024), 2) # convert to GB
    in_use = round(memory.used/(1024*1024*1024), 2) # convert to GB
    free = round(memory.used/(1024*1024*1024), 2) # convert to GB

    for i in range(time-1, -1, -1):
        plt.xlabel(
            f"Tempo de monitoramento: {i}\n"
            f"Total: {total} GB / Em uso: {in_use} GB / Livre: {free} GB"
        )
        memory = psutil.virtual_memory().percent
        values.append(memory)
        plt.plot(values, 'r-o')
        plt.pause(1)
    
    plt.xlabel(
        f"Monitoramento finalizado com sucesso!\n"
        f"Total: {total} GB / Em uso: {in_use} GB / Livre: {free} GB"
    )
   
def show_cpu_usage_graph():
    values = []
    time = int(input('Digite o tempo de monitoramento:\n'))
    processor_name = platform.processor()
    cpu_freq = psutil.cpu_freq().current
    cpu_freq_total = psutil.cpu_freq().max
    cpu_count = psutil.cpu_count()
    cpu_count_logical = psutil.cpu_count(logical=False)
    
    for i in range(time-1, -1, -1):
        plt.xlabel(
            f"Tempo de monitoramento: {i}\n"
            f"CPU: {processor_name} / frequência de uso: {cpu_freq} / frequência total: {cpu_freq_total}\n"
            f"Número total de núcleos: {cpu_count} / Número total de threads: {cpu_count_logical}"
        )
        cpu = psutil.cpu_percent()
        values.append(cpu)
        plt.plot(values, 'r-o')
        plt.pause(1)
          
    plt.xlabel(
        f"Monitoramento finalizado com sucesso!\n"
        f"CPU: {processor_name} / frequência de uso: {cpu_freq} / frequência total: {cpu_freq_total}\n"
        f"Número total de núcleos: {cpu_count} / Número total de threads: {cpu_count_logical}"
    )  
   
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

def show_files_and_directories():
    list_of_data = os.listdir()

    dic_arq = {}
    directories = []

    for i in list_of_data:
        if os.path.isfile(i):
            ext = os.path.splitext(i)[1]
            if not ext in dic_arq:
                dic_arq[ext] = []
            dic_arq[ext].append(i)
        else:
            directories.append(i)
            
    if len(dic_arq) > 0:
        print("Arquivos:")
        for i in dic_arq:
            for j in dic_arq[i]:
                print(j)
        print("\n")
        
    if len(directories) > 0:
        print("Diretórios:")
        for i in directories:
            print(i)
        print("\n")

while option != 0:
    if option == " ":
        print("Resumo:")
        memory = psutil.virtual_memory()
        memory_total = round(memory.total/(1024*1024*1024), 2) # convert to GB
        memory_used = round(memory.used/(1024*1024*1024), 2) # convert to GB
        disk = psutil.disk_usage('.')
        disk_total = round(disk.total/(1024*1024*1024), 2) # convert to GB
        print(f'IP: {show_machine_ip()}\n')
        print(f'Memória total: {memory_total} GB')
        print(f'Memória usada: {memory_used} GB')
        print(f'Nome do processador: {platform.processor()}')
        print(f'Disco Total: {disk_total} GB')
        print("\n")
        if show_files_and_directories() != None:
            print(f'{show_files_and_directories()}')
    elif int(option) == 0:
        break
    elif int(option) == 1:
        show_plt_title('Memória')
        plt.ion()
        show_memory_usage_graph()
        plt.ioff()
        plt.show()
    elif int(option) == 2:
        show_plt_title('CPU')
        plt.ion()
        show_cpu_usage_graph()
        plt.ioff()
        plt.show()
    elif int(option) == 3:
        show_plt_title('Disco')
        plt.ion()
        show_disk_usage_graph()
        plt.ioff()
        plt.show()
    else:
        print("Opção inválida")
    
    option = input(
        'Tecle "Barra" para visualizar um resumo de todas as informações:\n'
        'Digite 0 para sair:\n'
        'Digite 1 para visualizar o gráfico da porcentagem do uso de memória:\n'
        'Digite 2 para visualizar o gráfico da porcentagem do uso de CPU:\n'
        'Digite 3 para visualizar o gráfico da porcentagem do uso de disco:\n'
    )

print('FIM')