from concurrent.futures import ThreadPoolExecutor
import time
# something is wrong with this...
executor = ThreadPoolExecutor(max_workers=5)

def computation(start, end):
    array = []
    for i in range(start, end):
        array.append(i)
    return array

def by_threading(start, end):

    future1 = executor.submit(computation, start, end//4)
    future2 = executor.submit(computation, end//4, end//2)
    future3 = executor.submit(computation, end//2, 3*end//4)
    future4 = executor.submit(computation, 3*end//4, end)

    return future1.result() + future2.result() + future3.result() + future4.result()

def by_normal(start, end):
    return computation(start, end)

t1 = time.time()
n = by_normal(0,10**7)
t2 = time.time()
print(len(n))
print(t2-t1)

t3 = time.time()
t = by_threading(0,10**7)
t4 = time.time()
print(len(t))
print(t4-t3)






