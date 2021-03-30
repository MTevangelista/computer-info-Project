import socket, psutil, pickle, os, time, netifaces, platform, cpuinfo

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# Obtem o nome da máquina
HOST = socket.gethostbyname("")                     
PORT = 9008
BUFFER_SIZE = 1024
# Associa a PORT
socket_servidor.bind((HOST, PORT))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", HOST, "esperando conexão na porta", PORT)
# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

def get_processing_info(time):
    values = []
    processor_name = platform.processor()
    values.append(processor_name)
    cpu_freq = psutil.cpu_freq().current
    values.append(cpu_freq)
    cpu_freq_total = psutil.cpu_freq().max
    values.append(cpu_freq_total)
    cpu_count = psutil.cpu_count()
    values.append(cpu_count)
    cpu_count_logical = psutil.cpu_count(logical=False)
    values.append(cpu_count_logical)
    cpu_percent_values = []
    for i in range(time):
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_percent_values.append(cpu_percent)
    values.append(cpu_percent_values)
    info = cpuinfo.get_cpu_info()
    cpu_architecture = info['arch']
    cpu_name = info['brand_raw']
    cpu_word = info['bits']
    values.append(cpu_architecture)
    values.append(cpu_name)
    values.append(cpu_word)
    return values

def get_memory_data():
  informations = []
  mem = psutil.virtual_memory()
  memory_capacity = round(mem.total/(1024*1024*1024), 2) # convert to GB
  used_memory = round(mem.used/(1024*1024*1024), 2) # convert to GB
  percent_memory = mem.percent
  informations.append(memory_capacity)
  informations.append(used_memory)
  informations.append(percent_memory)
  return informations

def get_files_and_directories():
    list_of_data = os.listdir()
    dic_arq = {}
    directories = []
    files = []

    for i in list_of_data:
        if os.path.isfile(i):
            ext = os.path.splitext(i)[1]
            if not ext in dic_arq:
                dic_arq[ext] = []
            dic_arq[ext].append(i)
        else:
            directories.append(i)

    for i in dic_arq:
        for j in dic_arq[i]:
            files.append(j)

    return (files, directories)

def get_process_data():
    process = [proc.name()for proc in psutil.process_iter()]
    return process[:10]

def network_info():
    info = psutil.net_if_addrs()
    ip = info['en1'][0][1]
    gateway = netifaces.gateways()
    gateway = gateway['default'][2][0]
    subnet_mask = info['en1'][0][2]
    return (ip, gateway, subnet_mask)

def get_response():
  info_bytes = socket_cliente.recv(BUFFER_SIZE)
  list_of_data = pickle.loads(info_bytes)
  return list_of_data

def send_response(result):
  bytes_resp = pickle.dumps(result)
  socket_cliente.send(bytes_resp)

while True:
    list_of_information = get_response()
    if len(list_of_information) > 1:
        option = int(list_of_information[0])
        time = int(list_of_information[1])
    option = int(list_of_information[0])
    if option == 0:
        break
    if option == 1:
        result = get_processing_info(time)
        send_response(result)
    elif option == 2:
        result = get_memory_data()
        send_response(result)
    elif option == 3:
        result = get_files_and_directories()
        send_response(result)
    elif option == 4:
        result = get_process_data()
        send_response(result)
    elif option == 5:
        result = network_info()
        send_response(result)

# Fecha socket do servidor e cliente
socket_cliente.close()
socket_servidor.close()