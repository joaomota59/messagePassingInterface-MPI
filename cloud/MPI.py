from mpi4py import MPI

arquivo = open("etapa1.txt","a")
def mpiPI():#funcao que calcula o valor aprox de pi
    i = 1
    N = 840
    somatorio = 0
    for j in range(i,N+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    return (somatorio/N)*4

if __name__ == "__main__": #main -- Primeira versão
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()#rank do processo atual
    numDeProcessos = comm.Get_size()#numero de processos
    idmaquina = MPI.Get_processor_name()#hostname damaquina
    comm.Barrier()
    tinicial = MPI.Wtime()#tempo inicial
    res1 = mpiPI()
    comm.Barrier()
    tfinal=MPI.Wtime()#tempo final
    k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
    #print("-"*len(k)+"\n"+k+"\n")
    if rank == 0:
        bufferAux = [tfinal-tinicial]
        for i in range(1,numDeProcessos):
            bufferAux.append(comm.recv(source = i))
        arquivo.write(str(max(bufferAux))+"\n")
        arquivo.close()
        #print("Tempo de execução:",max(bufferAux))#tempo do processo que durou mais
    else:
        comm.send(tfinal-tinicial,dest = 0)

    #Elementos na comunicação
    #print("Quantidade de processos no comunicador = " + str(comm.Get_size()))
    

