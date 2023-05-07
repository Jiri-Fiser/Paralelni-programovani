from timeit import timeit
from contextlib import contextmanager
from time import perf_counter
from statistics import mean, stdev
from numba import jit
from multiprocessing import Pool, Queue, Process, cpu_count
import os

@jit(boundscheck=False, nopython=True)
def zeta(x:float, n:int = 5_000_000) -> float:
    suma = 0.0
    for i in range(1, n+1):
        suma += 1/(i**x)
    return suma


@contextmanager
def bm(text):
    t = perf_counter()
    yield
    dt = perf_counter() - t
    print(f"{dt:.2g}: {text}")


def bmx(text, f, n=20):
    times = []
    for i in range(n):
        t = perf_counter()
        f()
        dt = perf_counter() - t
        times.append(dt)
    m = mean(times)
    d = stdev(times)
    print(f"{m-3*d:.2g} – {m+3*d:.2g} {text}")


# bmx("zeta", lambda: zeta(2.0))

p = Pool(os.cpu_count())
x = [float(i) for i in range (2, 10)]
for y in p.imap(zeta, x):
    print(y)

def worker(cq, rq):
    while True:
        x = cq.get()
        if x is None:
            return
        z = zeta(x)
        rq.put((x, z))


if __name__ == "__main__":
    cq = Queue()
    rq = Queue()

    for i in range(cpu_count()):
        p = Process(target=worker, args=(cq, rq))
        p.start()

    xs = [float(i) for i in range (2, 10)]
    for x in xs:
        cq.put(x)

    for i in range(cpu_count()):
        cq.put(None)

    for i in range(len(xs)):
        print(rq.get())

