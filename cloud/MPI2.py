from mpi4py import MPI

arquivo = open("etapa2.txt","a")
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

if __name__ == "__main__": #main -- Segunda versão
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()#rank do processo atual
    numDeProcessos = comm.Get_size()#numero de processos
    idmaquina = MPI.Get_processor_name()#hostname damaquina
    comm.Barrier()#barreira inicio
    tinicial = MPI.Wtime()
    res1 = mpiPI(comm.Get_size(),rank)
    comm.Barrier()#barreira fim
    tfinal=MPI.Wtime()
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
