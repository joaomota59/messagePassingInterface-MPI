from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
proc = MPI.Get_processor_name()
print("Ola processo",rank,"na maquina ",proc)

