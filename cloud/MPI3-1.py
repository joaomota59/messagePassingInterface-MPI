from mpi4py import MPI

arquivo = open("etapa3-1.txt","a")
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
            tfinal=MPI.Wtime()#tempo final
            #k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
            #print("-"*len(k)+"\n"+k+"\n")
            bufferAux = [tinicial - tfinal]
            for i in range(1,numDeProcessos):
                bufferAux.append(comm.recv(source = i)[1])
            arquivo.write(str(max(bufferAux))+"\n")
            arquivo.close()
            #print("Tempo de execução:",max(bufferAux))#tempo de execução do processo que demorou mais
            
        else:#se for qualquer processo diferente do processo 1
            
            tinicial = MPI.Wtime()#tempo inicial
            
            res1 = mpiPI(numDeProcessos,rank)

            tfinal=MPI.Wtime()#tempo final
            comm.send([res1,tfinal-tinicial],dest = 0)
            #print("Tempo: ",tfinal-tinicial)
            #k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
            #print("-"*len(k)+"\n"+k+"\n")
