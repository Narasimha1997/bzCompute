import pyCompute
import numpy
import time

#multiple workers mode : 
#Domain Decomposition : 

#example : execution 100 matmuls in parallel : 

#create a placeholder , x and y : 

x = pyCompute.placeholder(shape = (100,100), name = "pl_1")

y = pyCompute.placeholder(shape = (100,100), name = "pl_2")

op = pyCompute.matmul(x, y, name = "mul")

#setup the inputs : 

inputs = [{
    "pl_1" : numpy.random.randint(low = 1, high = 10, size = (100,100)),
    "pl_2" : numpy.random.randint(low = 1, high = 10, size = (100,100))
}] * 100

#setup parallel master session : 

#you can use MasterSession in 2 modes : 
#if pooled , the library will create a pre-forked thread-pool for each worker
#if not, threads are created on-demand
session = pyCompute.MasterSession(pyCompute.default_graph, n_workers = 100, pooled = True)

session.setup(op, feeds = inputs)

#run thr session : 

start = time.time()

ops = session.run()

end = time.time() - start

print("Time taken : " , end)

print(ops)

#100 matmuls in 0.11111s

