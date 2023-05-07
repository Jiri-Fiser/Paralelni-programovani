from mpi4py import MPI
from typing import Iterable, Tuple, List, Any, TypeVar
from functools import reduce
from operator import add

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def zeta(x:float, n:int = 5_000_000) -> float:
    suma = 0.0
    for i in range(1, n+1):
        suma += 1/(i**x)
    return suma


def part_iter(n:int, p:int) -> Iterable[Tuple[int]]:
    for i in range(p):
        start = (i * n) // p
        end = ((i+1) * n) // p
        yield  start, end


TItem = TypeVar("TItem")
def list_partitioner(l:List[TItem], p:int) -> List[List[TItem]]:
    return [l[start:end] for start, end in part_iter(len(l), p)]


print(f"start {rank}/{size}")
if rank == 0:
    xs = [float(i) for i in range (2, 20)] # načtení vstupu
    pxs = list_partitioner(xs, size) # partitiování
else:
    pxs = None # prázdná inicializace pro tasky != root
lxs = comm.scatter(pxs)
lres = [zeta(x) for x in lxs]
res = comm.gather(lres)

if rank == 0:
    print(reduce(add, res))