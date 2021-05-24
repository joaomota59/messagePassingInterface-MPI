from mpi4py import MPI
import numpy

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

if __name__ == "__main__": #main -- Segunda versão
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
        processoPI[0]= mpiPI(numDeProcessos)
        print("Resposta do processo [" + str(rank) + "] = " + str(processoPI[0]) + " ID Máquina = "+str(idmaquina))
        comm.Reduce(processoPI,total,op = MPI.SUM,root = 0)
        if rank == 0:
            print("Soma de todos processos:",total[0])
