from mpi4py import MPI
import os
import random
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

file_list = os.listdir('.')
part_size = math.ceil(len(file_list) / size)

data = os.listdir('.')[rank * part_size: (rank + 1) * part_size]

max_per_process = -1

if len(data) != 0:
    for item in data:
        with open(os.path.join('.', item), 'r') as f:
            max_per_process = max(max_per_process, sum(1 for _ in f))

global_max = comm.reduce(max_per_process, op=MPI.MAX, root=0)

if rank == 0:
    print('the answer is {}'.format(global_max))

