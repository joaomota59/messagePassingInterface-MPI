from mpi4py import MPI


def mpiPI(i=1,N=840):#funcao que calcula o valor aprox de pi
    somatorio = 0
    for j in range(i,N+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    return (somatorio/N)*4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
idmaquina = MPI.Get_processor_name()

#Elementos na comunicação
print("Quantidade de processos no comunicador = " + str(comm.Get_size()))

#1 fazer com que todos calculem o valor de PI 
#PS: Falta medir o tempo!!
#print("ID do processo = ["+str(rank)+"] na maquina "+str(idmaquina) + " PI = " + str(mpiPI()))


#Enviar um dado específico para algum processo 
#tag e o id da mensagem - envio uma msg com um id e espero receber a msg com o mesmo id
if rank == 0:
	print("Processo " + str(rank) +  " enviando o numero 100 para o processo 1")
	comm.send(100, dest=1,tag=11)
if rank == 1:
	print("Processo " + str(rank) + " mostrando o que recebeu do processo 0")
	n = comm.recv(source=0,tag=11)
	#print(str(n))
	print("Processo",rank, "recebeu o numero ",n)


