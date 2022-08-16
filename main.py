#
#
# @autor = https://github.com/RafaRpso
# 
import psutil
import math  
import os 
import time 
os.system('clear')




def memoriaRam() : 
    uso_ram = psutil.virtual_memory().percent
    disponivel_ram_percent = psutil.virtual_memory().available * 100
    
    print("MEMÓRIA RAM \n ================= \n  ") 
    print("Uso atual da Ram: "+str(uso_ram)+ "%")

    print("Restante da Ram: "+ str(round(disponivel_ram_percent / psutil.virtual_memory().total,2))+"%")

    print('\n')


def cpu() :
    freq_atual_cpu =  psutil.cpu_freq()[0]
    freq_minima_cpu = psutil.cpu_freq()[1]
    freq_max_cpu = psutil.cpu_freq()[2]
    
    freq_percent = (freq_atual_cpu * 100 ) / (freq_max_cpu/1000)
    print("CPU \n ================= \n  ")
    
    print("Frequência mínima da CPU: "+ str(freq_minima_cpu) + "GHz")

    print("Frequência máxima da CPU: " + str(freq_max_cpu) + "GHz")

    print("Frequência atual da  CPU: " + str(freq_percent )[0:2]+"%/100%")
    print('\n')

def disco() : 
    print("Disco \n ================= \n  ")

    disco_total = psutil.disk_usage("/")[0] 
    disco_usado = psutil.disk_usage("/")[1]
    disco_percent = round(disco_total * 100 / disco_usado/100,2)
    tempo_leitura = psutil.disk_io_counters()[5]
    tempo_escrita = psutil.disk_io_counters()[6]

    
    print("Uso do Disco: " + str(disco_usado )[0:3] + "GB/" + str(disco_total)[0:3] + "GB"  +  " ("+str(disco_percent)+"%)")

    print("Tempo de escrita: " + str(tempo_escrita)[0:3]+"ms")
    print("Tempo de leitura "+ str(tempo_leitura)[0:3]+"ms")
    print('\n')
def network() : 
    print("Internet \n ================= \n")
    bytes_recebidos = psutil.net_io_counters()[0]
    bytes_enviados = psutil.net_io_counters()[1]
    # internet tá com problema na conversão => ver com a Marise
    print("Velocidade de Download: " + str(round( bytes_enviados/10000000 ,2 ))  + "mb")

    print("Velocidade de Upload: " + str(round(bytes_recebidos/1000000,2) ) + "mb")
 


while True : 
    os.system('clear')
    print("""
____  ___ __                 __    
\   \/  //  |______    _____|  | __
 \     /\   __\__  \  /  ___/  |/ /
 /     \ |  |  / __ \_\___ \|     \ 
/___/\  \|__| (____  /____  >__|_       
      \_/          \/     \/     \/
      \n\n
""")
    memoriaRam() 
    cpu()
    disco()
    network()
    time.sleep(1)