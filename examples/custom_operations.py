import pyCompute

import numpy

#custom operation 

def custom_op(a, kwargs) :
    #simply increments each operant by value 10  
    return a + 10

#custom op can use passed kwargs
def custom_op2(a, kwargs) :

    if kwargs["increment"] : 

        return a + 20
    else : 

        return a

a = pyCompute.constant([1,2,3,4,5,6,7,8], name = "const_1")

#call the custom op, pass the function, name and operand
op = pyCompute.custom_op(custom_op, "op1", a)

#call 2nd op with kwargs :

op2 = pyCompute.custom_op(custom_op, "op2", op, increment = True)

session = pyCompute.SequentialSession()

op = session.run(pyCompute.default_graph, op2)

print(op)
