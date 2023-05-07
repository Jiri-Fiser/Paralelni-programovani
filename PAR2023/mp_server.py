from multiprocessing.managers import BaseManager
from queue import Queue

cq = Queue()
rq = Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_cq', callable=lambda: cq)
QueueManager.register('get_rq', callable=lambda: rq)
address = '127.0.0.1'
m = QueueManager(address=(address, 50000), authkey=b'abracadabra')
s = m.get_server()
print(f"Server started at address {address}")
s.serve_forever()