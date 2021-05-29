from mpi4py import MPI
import numpy as np

arquivo = open("etapa3-2.txt","a")
def mpiPI(nroProcesso, rank):#funcao que calcula o valor aprox de pi
    N = 840
    i = int(1 + (N/nroProcesso)*rank)
    k = int((N/nroProcesso)*(rank+1))
    somatorio = 0
    for j in range(i,k+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    #print(i,k)#intervalos
    #print((somatorio/N)*4)#somatorio de cada intervalo
    return (somatorio/N)*4

if __name__ == "__main__": #main -- Terceira versão
    comm = MPI.COMM_WORLD
    numDeProcessos = comm.Get_size()
    rank = comm.Get_rank()#rank do processo atual
    buffer = []
    if(840 % numDeProcessos != 0):#retorna erro se o numero de processos nao for divisivel p 840
        if rank == 0 :
            print("ERRO!\nEntre com um número de processos que seja divisivel por 840!")
    else:#se for divisivel por 840 entao divide entre os processos
        idmaquina = MPI.Get_processor_name()#hostname damaquina
        if rank == 0:
            tinicial = MPI.Wtime()#tempo inicial
            res1 = mpiPI(numDeProcessos,rank)   
            buffer = [[res1,tinicial]]#buffer que guarda todos os resultados dos processos
            for i in range(1,numDeProcessos):
                buffer.append(comm.recv(source = i))
            tfinal=MPI.Wtime()#tempo final é igual para todos processos
            tinicialDefinitivo = np.array(buffer).min(axis=0)[1]#pega o menor tempo inicial dos processos
            #print("Tempo de execução:",tfinal - tinicialDefinitivo)#tempo de execução em relação ao processo que demorou mais
            arquivo.write(str(tfinal - tinicialDefinitivo)+"\n")
            arquivo.close()
            totalPI = np.array(buffer).sum(axis=0)[0]
            #print("Soma de todos processos:",totalPI)#exibe a soma de todos processos
            
            
        else:#se for qualquer processo diferente do processo 1
            tinicial = MPI.Wtime()#tempo inicial
            res1 = mpiPI(numDeProcessos,rank)
            comm.send([res1,tinicial],dest = 0)
            #print("Inicio",tinicial,"rank:",rank)
            #k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
            #print("-"*len(k)+"\n"+k+"\n")      
            #k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
            #print("-"*len(k)+"\n"+k+"\n")
