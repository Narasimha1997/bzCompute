import numpy
from pyCompute.error import Exception


class Graph:

    def __init__(self):

        self.constants = []
        self.variables = []
        self.operations = []
        self.placeholders = []

        self.name_registry = {}

    def get_constants(self):

        return {const.name : const.output for const in self.constants}
    
    def get_placeholders(self):

        return {const.name : const.output for const in self.constants}

    def get_operations(self):

        return {op.name : op for op in self.operations} 

    def create_graph(self):

        global _default_graph
        _default_graph = self


class Variable:

    def __init__(self, value, name, dtype='float32'):

        self.parents = []
        self.input_value = numpy.array(value, dtype='float32')

        self.output = []

        self.name = name

        _default_graph.variables.append(self)
        _default_graph.name_registry[name] = {
            "dtype": dtype, "shape": self.input_value.shape, "type": self.__class__}

    def get_value(self):

        return self.input_value

    def get_metadata(self):

        return _default_graph.name_registry[name]

    def get_parents(self):

        return self.get_parents


class constant:

    def __init__(self, value, name, dtype='float32'):

        self.parents = []
        self.input_value = numpy.array(value, dtype='float32')

        self.output = []

        self.name = name

        _default_graph.constants.append(self)
        _default_graph.name_registry[name] = {
            "dtype": dtype, "shape": self.input_value.shape, "type": self.__class__}

    def get_value(self):

        return self.input_value

    def get_metadata(self):

        return _default_graph.name_registry[name]

    def get_parents(self):

        return self.get_parents


class placeholder:

    def __init__(self, shape, name, dtype='float32'):

        self.parents = []

        self.name = name
        self.value = None
        self.dtype = dtype
        self.shape = shape

        _default_graph.placeholders.append(self)
        _default_graph.name_registry[name] = {
            "dtype": dtype, "shape": shape, "type": self.__class__}

    def feed_value(self, value):

        value = numpy.array(value, dtype=self.dtype)

        if value.shape != self.shape:
            Exception("Placeholder "+self.name+" takes tensor of shape : " +
                      str(self.shape)+" but got : "+str(value.shape))
            exit(0)
        else:
            self.value = value
            del value

    def get_value(self):

        return self.input_value

    def get_metadata(self):

        return _default_graph.name_registry[name]

    def get_parents(self):

        return self.get_parents


# defines a base class for all the supported operation
# to implement your own operation, extend this class
class Operation:

    def __init__(self, inputs, name):

        self.parents = []

        self.name = name

        self.inputs = inputs

        for i in range(len(inputs)):

            tensor = inputs[i]

            if type(tensor) == list:

                tensor = constant(
                    tensor, name="tensor:"+str(len(_default_graph.constants)), dtype='float32')
                self.inputs[i] = tensor

            tensor.parents.append(self)

        #self.inputs = inputs

        _default_graph.operations.append(self)
        _default_graph.name_registry[name] = {
            "type": self.__class__, "level": 0}

    def compute(self, *inputs):
        '''implement by KernelOperation that extends this class'''
        pass

    def get_metadata(self):

        return _default_graph.name_registry[name]

    def get_parents(self):

        return self.parents

    def get_inputs(self):

        return self.inputs


# test


'''

graph = Graph()

graph.create_graph()

a = constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], name = "constant_a")
b = constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], name = "constant_b")

c = placeholder(shape = (10, 10), name = "placeholder_c")

d = Variable([[1, 2, 3],[4,5,6]], name = "Variable_d")

e = Operation([a, b, [[1, 2, 3], [4, 5, 6]]], name = "AddOp")

print(_default_graph.constants)
print(_default_graph.variables)
print(_default_graph.placeholders)
print(_default_graph.operations)

print(_default_graph.name_registry) '''
