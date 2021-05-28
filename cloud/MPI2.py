from mpi4py import MPI

# rank 0 (1 - N/2) 
# rank 1 (N/2+1 - N)


def mpiPI(nroProcesso, rank):#funcao que calcula o valor aprox de pi
    N = 840
    i = int(1 + (N/nroProcesso)*rank)
    if rank == nroProcesso - 1:#quando for o ultimo processo
        k = 840
    else:
        k = int((N/nroProcesso)*(rank+1))
    somatorio = 0
    for j in range(i,k+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    #print(i,k)#intervalos
    #print((somatorio/N)*4)#somatorio de cada intervalo
    return (somatorio/N)*4

#1 fazer com que todos calculem o valor de PI 
#PS: Falta medir o tempo!!
#print("ID do processo = ["+str(rank)+"] na maquina "+str(idmaquina) + " PI = " + str(mpiPI()))


#Enviar um dado específico para algum processo 
#tag e o id da mensagem - envio uma msg com um id e espero receber a msg com o mesmo id

'''
if rank == 0:
	print("Processo " + str(rank) +  " enviando o numero 100 para o processo 1")
	comm.send(100, dest=1,tag=11)
if rank == 1:
	print("Processo " + str(rank) + " mostrando o que recebeu do processo 0")
	n = comm.recv(source=0,tag=11)
	#print(str(n))
	print("Processo",rank, "recebeu o numero ",n)
'''



if __name__ == "__main__": #main -- Segunda versão
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()#rank do processo atual
    idmaquina = MPI.Get_processor_name()#hostname damaquina
    res1 = mpiPI(comm.Get_size(),rank)
    k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
    print("-"*len(k)+"\n"+k+"\n")
