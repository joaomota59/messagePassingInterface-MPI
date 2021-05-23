from mpi4py import MPI

# rank 0 (1 - N/2) 
# rank 1 (N/2+1 - N)


def mpiPI(nroProcesso):#funcao que calcula o valor aprox de pi
    i = 1
    N = 840
    somatorio = 0
    for j in range(i,N+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    return ((somatorio/N)*4)/nroProcesso

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
    #Elementos na comunicação
    #print("Quantidade de processos no comunicador = " + str(comm.Get_size()))
    #versao = input("ok")
    if rank == 0:
            res0 = mpiPI(comm.Get_size())
            k = ("Resposta do processo [" + str(rank) + "] = " + str(res0)+ " ID Máquina = "+str(idmaquina))
            print("-"*len(k)+"\n"+k+"\n")
    if rank == 1:
            res1 = mpiPI(comm.Get_size())
            k = ("Resposta do processo [" + str(rank) + "] = " + str(res1) + " ID Máquina = "+str(idmaquina))
            print("-"*len(k)+"\n"+k+"\n")
    if rank == 2:
            res2 = mpiPI(comm.Get_size())
            k = ("Resposta do processo [" + str(rank) + "] = " + str(res2) + " ID Máquina = "+str(idmaquina))
            print("-"*len(k)+"\n"+k+"\n")
    if rank == 3:
            res2 = mpiPI(comm.Get_size())
            k = ("Resposta do processo [" + str(rank) + "] = " + str(res2) + " ID Máquina = "+str(idmaquina))
            print("-"*len(k)+"\n"+k+"\n")

