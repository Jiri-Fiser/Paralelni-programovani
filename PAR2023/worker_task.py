from multiprocessing.managers import BaseManager
from os import getpid
from multiprocessing import cpu_count, Process
from socket import gethostname

class QueueManager(BaseManager):
    pass


def zeta(x:float, n:int = 5_000_000) -> float:
    suma = 0.0
    for i in range(1, n+1):
        suma += 1/(i**x)
    return suma

def worker_id():
    return f"{gethostname()}-{getpid()}"

def worker(cq, rq):
    while True:
        x = cq.get()
        #if x is None:
        #    return
        z = zeta(x)
        rq.put((worker_id(), x, z))


if __name__ == "__main__":
    QueueManager.register('get_cq')
    QueueManager.register('get_rq')
    #address = '192.168.80.42'
    address = '127.0.0.1'
    m = QueueManager(address=(address, 50000), authkey=b'abracadabra')
    m.connect()
    cq = m.get_cq()
    rq = m.get_rq()
    for i in range(cpu_count()):
        p = Process(target=worker, args=(cq, rq))
        p.start()



