#  https://github.com/RafaRpso

import psutil as ps 
import platform
import math  
import os 
import time 
import socket
import subprocess
import pymysql ; 
from datetime import datetime
# CREATE TABLE tbDadosDisco( 
# 	idDadosDisco INT PRIMARY KEY AUTO_INCREMENT, 
# 	espacoLivreDisco DOUBLE NOT NULL ,
# 	espacoUsadoDisco DOUBLE NOT NULL , 
# 	usoAtualDisco INT NOT NULL, 
# 	dataDisco DATETIME NOT NULL
 
# );

# CREATE TABLE tbDadosCpu( 
# 	idDadosCpu INT PRIMARY KEY  AUTO_INCREMENT, 
# 	freqAtualCpu DOUBLE NOT NULL, 
# 	temperaturaAtualCpu DOUBLE NOT NULL, 
# 	dataCpu DATETIME NOT NULL  
# );


#select * from tbDadosCpu ORDER BY dataCpu DESC LIMIT 5
#select * from tbDadosDisco ORDER BY dataDisco DESC LIMIT 5 ; 
conn = pymysql.connect(
        host='localhost',
        user='aluno', 
        password = "sptech",
        db='dbBancoCpu',
        )

cursor = conn.cursor() ; 


usuario = "aluno"
senha = "sptech"



dados_os =  { 

        'SISTEMA_TIPO' : platform.system(), 
      
}
dados_ram = {
            'RAM_DISPONIVEL':ps.virtual_memory().available >>30 , 
            'RAM_TOTAL':ps.virtual_memory()[0] ,
}
# para pegar um dado, use dados_ram[nome]
# 1.90 - 100 
# 1.1 - x 

# 1.90x = 100*1.1 
#x = 100*1.1 / 1.90
dados_cpu = { 
    'CPU_NOME' : platform.processor(),
    'CPU_FREQ_MINIMA':  ps.cpu_freq().min,
    'CPU_FREQ_MAX' :  ps.cpu_freq().max,
}

def sistemaOperacional(): 
    print("\033[1;36m Sistema Operacional  \n ================= \033[0m\n  ")
    print("Tipo do sistema: " + str(dados_os["SISTEMA_TIPO"]))
    print("Horário atual: ") 
    os.system('date')
    print('\n')

def memoriaRam() : 
    uso_ram = ps.virtual_memory()[3]
    percent = round((uso_ram*100/ps.virtual_memory()[0] )) 


    print("\033[1;36m MEMÓRIA RAM \n ================= \033[0m\n  ") 
    print("Uso atual da Ram: "+str(percent) + "%/100%")

    print("Uso em memória da Ram: "+ str(round(uso_ram/pow(10,9),2))+"GB/" +str(round(dados_ram['RAM_TOTAL']/pow(10,9),2))+"GB")

    print('\n')

def cpu() :


    print("\033[1;36mCPU \n ================= \n \033[0m ")
    
    print(platform.processor())
    print("Frequência mínima da CPU: "+ str(dados_cpu['CPU_FREQ_MINIMA']) + "GHz")

    print("Frequência máxima da CPU: " + str(dados_cpu['CPU_FREQ_MAX']) + "GHz")

    print("Frequência atual da  CPU: " + str(round(ps.cpu_freq().current * 10 / ps.cpu_freq().max) ) + "%/100% ") 
    print("Arquitetura do processador: " + platform.machine())
    print('\n')


    

    cursor.execute("INSERT INTO tbDadosCpu (freqAtualCpu,temperaturaAtualCpu,dataCpu)  VALUES('{0}','{1}','{2}')".format(
    
    round(ps.cpu_freq().current / 1024,2)   ,ps.sensors_temperatures()['pch_skylake'][0][1], datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    )

def disco() : 
    print("\033[1;36mDisco \n ================= \n \033[0m ")


    disco_total = ps.disk_usage('/').total >> 30
    disco_livre = ps.disk_usage('/').free >> 30
    disco_percent = round(disco_total * 10 / disco_livre,2)
    tempo_leitura = ps.disk_io_counters()[5]
    tempo_escrita = ps.disk_io_counters()[6] 
  


    cursor.execute("INSERT INTO tbDadosDisco (espacoLivreDisco,espacoUsadoDisco,usoAtualDisco,dataDisco)  VALUES('{0}','{1}','{2}','{3}')".format(
    
    disco_livre, (disco_total - disco_livre),disco_percent,datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    )


    print("Uso do Disco: " + str(round(disco_total-disco_livre))  + "GB/" + str(disco_total) + "GB"  +  " ("+str(disco_percent)+"%)")

    print("Tempo de escrita: " + str(tempo_escrita)[0:3]+"ms")
    print("Tempo de leitura "+ str(tempo_leitura)[0:3]+"ms")
    print('\n')

    print('\n')


def network() : 
    print("\033[1;36mInternet \n ================= \033[0m\n")
    bytes_recebidos = ps.net_io_counters()[0]
    bytes_enviados = ps.net_io_counters()[1]
    nome_internet = socket.gethostname()
    ip_internet = socket.gethostbyname(socket.gethostname())
    # internet tá com problema na conversão => ver com a Marise
    print("Hostname: " + str(nome_internet))
    print("ip: " + str(ip_internet))
    print("Velocidade de Download: " + str(round( bytes_enviados/10000000 ,2 ))  + "mb")

    print("Velocidade de Upload: " + str(round(bytes_recebidos/1000000,2) ) + "mb")




def processoTotal() : 
    os.system("clear")
    sistemaOperacional()
    memoriaRam() 
    cpu()
    disco()
    network()
    time.sleep(1)

    conn.commit()



    processoTotal()
processoTotal()
