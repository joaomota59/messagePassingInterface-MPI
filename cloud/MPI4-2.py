from mpi4py import MPI
import numpy


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

if __name__ == "__main__": #main -- Quarta versão
    comm = MPI.COMM_WORLD
    numDeProcessos = comm.Get_size()
    rank = comm.Get_rank()#rank do processo atual
    processoPI = numpy.zeros(1)#inicializa o processoPI com 0
    total = numpy.zeros(1)#inicializa o processo total com 0
    if(840 % numDeProcessos != 0):#retorna erro se o numero de processos nao for divisivel p 840
        if rank == 0 :
            print("ERRO!\nEntre com um número de processos que seja divisivel por 840!")
    else:#se for divisivel por 840 entao divide entre os processos
        idmaquina = MPI.Get_processor_name()#hostname damaquina
        #se for qualquer processo diferente do processo 1
        comm.Barrier()
        tinicial = MPI.Wtime()
        processoPI[0]= mpiPI(numDeProcessos,rank)
        #print("Resposta do processo [" + str(rank) + "] = " + str(processoPI[0]) + " ID Máquina = "+str(idmaquina))
        comm.Reduce(processoPI,total,op = MPI.SUM,root = 0)
        comm.Barrier()
        tfinal=MPI.Wtime()
        comm.send(tfinal - tinicial,dest = 0)#Envia para o rank 0 o tempo de todos processos
        if rank == 0:
            print("Soma de todos processos:",total[0])
            bufferAux = []
            for i in range(0,numDeProcessos):
                bufferAux.append(comm.recv(source = i))
            print("Tempo de execução:",max(bufferAux))#exibe o tempo do processo que demorou mai
            
