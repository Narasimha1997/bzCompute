import pyCompute

#Placeholders : 

#define a shape for placeholder

inputs = pyCompute.placeholder(shape = (1,5), name = 'pl_1')

weights = pyCompute.constant([[1],[1],[1],[1],[1]], name = "weights")

mul = pyCompute.matmul(inputs, weights, name = "mul_1")

sigmoid = pyCompute.sigmoid(mul, name = "sig_1")

session = pyCompute.SequentialSession()

#feed value to placeholder , providing its name : 

input_ = {"pl_1" : [[1,2,3,4,5]]}

result = session.run(pyCompute.default_graph, sigmoid, feed_dict = input_)

print(result)