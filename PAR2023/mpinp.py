from typing import Iterable, Tuple

import numpy
import numpy as np
from mpi4py import MPI
from numba import jit

@jit(boundscheck=False, nopython=True)
def zeta_np(x:np.ndarray, y:np.ndarray, n:int = 5_000) -> np.ndarray:
    for j in range(x.shape[0]):
        y[j] = 0.0
        for i in range(1, n+1):
            y[j] += 1/(float(i)**x[j])


def part_iter(n:int, p:int) -> Iterable[Tuple[int]]:
    for i in range(p):
        start = (i * n) // p
        end = ((i+1) * n) // p
        yield  start, end-start # změna oproto mpipy (vrací počátek a velikost partition)


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    n = 80

    if rank == 0:
        xs = np.linspace(2.0, 10.0, n)
        ys = np.empty_like(xs)
        print("start")
    else:
        xs = None
        ys = None

    displ, count = zip(*part_iter(n, size))
    lxs = np.empty(count[rank])
    comm.Scatterv([xs, count, displ, MPI.DOUBLE], lxs)
    lys = np.empty_like(lxs)
    zeta_np(lxs, lys)
    comm.Gatherv(lys, [ys, count, displ, MPI.DOUBLE])

    if rank == 0:
        print(ys)





