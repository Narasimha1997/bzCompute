import pyCompute

#define constants mat_1 and mat_2
mat_1 = pyCompute.constant([[1,2,3],[1,2,3],[1,2,3]], name = "mat_1")
mat_2 = pyCompute.constant([[1,2,3],[1,2,3],[1,2,3]], name = "mat_2")

#multiply them by calling matmul()
op1 = pyCompute.matmul(mat_1, mat_2, name = "op1")

#create a SequentialSession for executing the op : 

session = pyCompute.SequentialSession()

#run the session : 

op = session.run(pyCompute.get_default_graph(), op1)

print(op)
