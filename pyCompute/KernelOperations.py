from pyCompute.graph import Operation
import pyCompute.graph
import numpy

class add(Operation):

    def __init__(self, tensor_x, tensor_y, name):

        super().__init__(inputs = [tensor_x, tensor_y], name = name)

    
    def compute(self, x, y):
        self.input_tensors = [x, y]
        return x + y

class matmul(Operation):

    def __init__(self, tensor_x, tensor_y, name):

        super().__init__(inputs = [tensor_x, tensor_y], name = name)

    
    def compute(self, x, y):

        self.input_tensors = [x, y]

        return numpy.matmul(x, y)

class sigmoid(Operation):

    def __init__(self, val_y, name):

        super().__init__(inputs = [val_y], name = name)

    
    def compute(self, x):

        #self.input_tensors = [x]

        return 1. / (1 + numpy.exp(-x))



class dot(Operation):

    def __init__(self, tensor_x, tensor_y, name):

        super().__init__(inputs = [tensor_x, tensor_y], name = name)
    
    def compute(self, x, y):

        #self.input_tensors = [x, y]

        return numpy.dot(x, y)


class mse(Operation):

    def __init__(self, tensor_x, val_y, name):

        super().__init__(inputs = [tensor_x, val_y], name = name)
    
    def compute(self, tensor_x, y):

        self.input_tensors = [tensor_x, y]

        return numpy.sum(numpy.square(tensor_x - y)) / 2

class relu(Operation):

    def __init__(self, x, name):

        super().__init__(inputs = [x], name = name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return x if x > 0 else 0

class tensor_sum(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)

    def compute(self, x):

        self.input_tensors = [x]

        return numpy.sum(x, axis = 1)

class difference(Operation):

    def __init__(self, tensor_x, tensor_y, name):

        super().__init__(inputs = [tensor_x, tensor_y], name = name)

    def compute(self, x, y):

        self.input_tensors = [x, y]

        return x - y

class mean(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)

    def compute(self, x):

        self.input_tensors = [x]

        return numpy.mean(x)

class median(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)

    def compute(self, x):

        self.input_tensors = [x]

        return numpy.median(x)

class median(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)

    def compute(self, x):

        self.input_tensors = [x]

        return numpy.median(x)

class median(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)

    def compute(self, x):

        self.input_tensors = [x]

        return numpy.median(x)

class log(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return numpy.log(x)

class argmin(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return numpy.argmin(x)

class argmin(Operation):

    def __init__(self, tensor_x, sum):

        super().__init__(inputs = [tensor_x], name = name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return numpy.argmin(x)
        

class argmax(Operation):

    def __init__(self, tensor_x, sum):

        super().__init__(inputs = [tensor_x], name = name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return numpy.argmax(x)

class argsort(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name =  name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return numpy.argsort(x)


class average(Operation):

    def __init__(self, tensor_x, name):

        super().__init__(inputs = [tensor_x], name = name)
    
    def compute(self, x):

        self.input_tensors = [x]

        return numpy.average(x)


class custom_op(Operation):

    def __init__(self, op_func, name , *args, **kwargs):

        super().__init__(inputs = [*args], name = name)

        self.kwargs = kwargs
        self.op_func = op_func

    
    def compute(self, *args):

        self.input_tensors = [*args]
        return self.op_func(*args, self.kwargs)



