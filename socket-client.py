import socket, time, pickle
import matplotlib.pyplot as plt

def show_options():
    option = input(
        'Digite 0 para sair:\n'
        'Digite 1 para visualizar uso de processamento:\n'
        'Digite 2 para visualizar informações de memória:\n'
        'Digite 3 para visualizar informações sobre arquivos e diretórios:\n'
        'Digite 4 para visualizar os nomes de 10 processos que estão executando:\n'
        'Digite 5 para visualizar as informações de IP, gateway e máscara de subrede da rede:\n'
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
    plt.plot(result, 'r-o')
    plt.savefig(f'images/{scope.lower()}.png')
    plt.show()
    plt.close()
    plt.cla()

HOST = socket.gethostbyname("")                     
PORT = 9008
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
                show_graphic('Processamento', result)
                print(f"No tempo de {monitoring_time}x, foram registrados as seguintes porcentagens: {result}\n")
            elif option == "2":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                memory_capacity, used_memory = result[0], result[1]
                print(
                    f"Capacidade de memória: {memory_capacity}\n"
                    f"Uso de memória: {used_memory}\n"
                )
            elif option == "3":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                files, directories = result[0], result[1]
                print(
                    f"Arquivos encontrados no diretório atual: {files}\n"
                    f"Diretótios encontrados: {directories}\n"
                )
            elif option == "4":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                print(f"processos em execução: {result}\n")
            elif option == "5":
                list_of_information = get_values_to_send_request()
                send_resquest(list_of_information)
                result = get_response()
                ip, gateway, subnet_mask = result[0], result[1], result[2]
                print(
                    f"IP: {ip}\n"
                    f"Gateway: {gateway}\n"
                    f"Máscara de subrede: {subnet_mask}\n"
                )
            option = show_options()
except Exception as erro:
    print('deu erro')
    print(str(erro))

# Fecha o socket
s.close()