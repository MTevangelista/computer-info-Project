import socket, time, pickle
import matplotlib.pyplot as plt
from tabulate import tabulate

def show_options():
    option = input(
        'Digite 0 para sair:\n'
        'Digite 1 para visualizar uso de processamento:\n'
        'Digite 2 para visualizar informações de memória:\n'
        'Digite 3 para visualizar informações de disco:\n'
        'Digite 4 para visualizar informações sobre arquivos e diretórios:\n'
        'Digite 5 para visualizar os nomes de 10 processos que estão executando:\n'
        'Digite 6 para visualizar as informações de IP, gateway e máscara de subrede da rede:\n'
        'Digite 7 para visualizar as informações pertencentes a subrede do IP específico:\n'
    )
    return option

def get_response():
    info_bytes = s.recv(BUFFER_SIZE)
    list_of_data = pickle.loads(info_bytes)
    return list_of_data

def get_values_to_send_request():
    list_of_information = []
    list_of_information.append(option)
    if can_monitor_the_time:
        monitoring_time = input('Digite o tempo de monitoramento:\n')
        list_of_information.append(monitoring_time)
    return list_of_information

def send_resquest(value):
    value_type = type(value)
    if value_type is list:
        bytes_resp = pickle.dumps(value)
        s.send(bytes_resp)
    else:
        s.send(value.encode('ascii'))

def show_loading(value):
    if can_monitor_the_time:
        for i in range(1, int(value)):
            print(f"[{i} / {value}] -> Carregando informações...")
            time.sleep(1.2)

# ---------------------------------------------------
def show_graphic(scope, data):
    plt.title(f'Monitoramento e Análise do Computador - {scope}\n')
    plt.plot(data, 'r-o')
    plt.savefig(f'images/{scope.lower()}.png')
    plt.show()
    plt.close()
    plt.cla()

HOST = socket.gethostbyname("")                     
PORT = 9009
BUFFER_SIZE = 1024

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    s.connect((HOST, PORT))
    option = show_options()
    while option != 0:
        can_monitor_the_time = False
        if option == "0":
            data = get_values_to_send_request()
            send_resquest(data)
            break
        else:
            if option == "1":
                can_monitor_the_time = True
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                monitoring_time = list_of_information[1]
                show_loading(monitoring_time)
                result = get_response()
                processor_name, cpu_freq, cpu_freq_total  = result[0], result[1], result[2]
                cpu_count, cpu_count_logical, cpu_percent_values = result[3], result[4], result[5]
                cpu_architecture, cpu_name, cpu_word = result[6], result[7], result[8]
                show_graphic('Processamento', cpu_percent_values)
                print(
                    f"Nome de CPU: {cpu_name}\n"
                    f"Tipo da arquitetura (arch): {cpu_architecture}\n"
                    f"Palavra do processador (em bits): {cpu_word}\n"
                    f"Nome do processador: {processor_name}\n"
                    f"frequência de uso: {cpu_freq}\n"
                    f"frequência total: {cpu_freq_total}\n"
                    f"Número total de núcleos: {cpu_count}\n"
                    f"Número total de threads: {cpu_count_logical}\n"
                    f"No tempo de {monitoring_time}x, foram registrados as seguintes porcentagens: {cpu_percent_values}\n"
                )
            elif option == "2":
                initial_time = time.time()
                initial_time_clock = time.process_time()
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                memory_capacity, used_memory, percent_memory = result[0], result[1], result[2]
                end_time = time.time()
                end_time_clock = time.process_time()
                print(f'O tempo total utilizado para chamar a função foi: {end_time - initial_time}')
                print(f'A quantidade total de clocks utilizados pela CPU para a realização dessa função foi: {end_time_clock - initial_time_clock}\n')
                print(
                    f"Capacidade de memória: {memory_capacity} GB\n"
                    f"Uso de memória: {used_memory} GB\n"
                    f"Percentual de uso de memória: {percent_memory}%\n"
                )
            elif option == "3":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                total, in_use, free, percent_disk = result[0], result[1], result[2], result[3]
                print(
                    f"Capacidade de disco: {total} GB\n"
                    f"Quantidade de disco em uso: {in_use} GB\n"
                    f"Quantidade de disco livre: {free} GB\n"
                    f"Percentual do uso de disco: {percent_disk}%\n"
                )
            elif option == "4":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                files, directories = result[0], result[1]
                print(
                    f"Arquivos encontrados no diretório atual: {files}\n"
                    f"Diretótios encontrados: {directories}\n"
                )
            elif option == "5":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                print(f"processos em execução: {result}\n")
            elif option == "6":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                ip, gateway, subnet_mask = result[0], result[1], result[2]
                print(
                    f"IP: {ip}\n"
                    f"Gateway: {gateway}\n"
                    f"Máscara de subrede: {subnet_mask}\n"
                )
            elif option == "7":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                print(tabulate(result, 
                    headers=["Host", "Protocolo", "Porta", "Status"], 
                    tablefmt="fancy_grid"))
                print()
            option = show_options()
except Exception as erro:
    print('deu erro')
    print(str(erro))

# Fecha o socket
s.close()