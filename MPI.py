from mpi4py import MPI


def mpiPI(i=1,N=840):#funcao que calcula o valor aprox de pi
    somatorio = 0
    for j in range(i,N+1):
        somatorio += 1/(1+((j-0.5)/N)**2)
    return (somatorio/N)*4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1) 
    print(mpiPI())
elif rank == 1:
    data = comm.recv(source=0)
    print(mpiPI())

