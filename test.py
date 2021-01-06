import os

lista = os.listdir()

dic_arq = {} # dict que vai abrigar os arquivos por tipo
diretorios = []

for i in lista:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1]
        if not ext in dic_arq:
            dic_arq[ext] = []
        dic_arq[ext].append(i)
    else:
        diretorios.append(i)
        
if len(dic_arq) > 0:
    print("Arquivos:")
    for i in dic_arq:
        for j in dic_arq[i]:
            print(j)
    print("\n")
    
if len(diretorios) > 0:
    print("Diretórios:")
    for i in diretorios:
        print(f"\t\t{i}")
    print("\n")