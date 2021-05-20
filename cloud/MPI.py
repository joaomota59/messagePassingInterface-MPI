from mpi4py import MPI


def mpiPI(i=1,N=840):#funcao que calcula o valor aprox de pi
    somatorio = 0
    for j in range(i,N+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    return (somatorio/N)*4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
idmaquina = MPI.Get_processor_name()
print("Ola processo",rank,"na maquina ",idmaquina)


