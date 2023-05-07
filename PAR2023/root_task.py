from multiprocessing import cpu_count
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# address = '192.168.80.42'
address = '127.0.0.1'

QueueManager.register('get_cq')
QueueManager.register('get_rq')

m = QueueManager(address=(address, 50000), authkey=b'abracadabra')
m.connect()
cq = m.get_cq()
rq = m.get_rq()

xs = [float(i) for i in range(2, 10)]
for x in xs:
    cq.put(x)

for i in range(len(xs)):
    print(rq.get())
