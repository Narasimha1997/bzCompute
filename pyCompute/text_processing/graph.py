
class Graph : 

    def __init__(self) :

        self.files = []
        self.strings = []
        self.arrays = []
        self.operations = []
        self.name_registry = {}
    
    def get_files(self):

        return {file_.name : file_.value for file_ in self.files}

    def get_strings(self):

        return {string.name : string.value for string in self.strings}
    
    def get_arrays(self):

        return {array_.name : array_.value for array_ in self.arrays}

    def get_operations(self):

        return {op.name : op for op in self.operations}
    
    def create_graph(self) :
        global _string_default_graph
        _string_default_graph = self



class File : 

    def __init__(self, value , name, read_lines = False):

        self.name = name
        self.value = open(value, 'r').read() if not read_lines else open(value, 'r').readlines()

        self.parents = []

        self.output = []

        _string_default_graph.files.append(self)

        _string_default_graph.name_registry[name] = {"file" : value, "size" : len(self.value)}

    
    def get_value(self):

        return self.value

    def get_metadata(self):

        return _string_default_graph.name_registry[self.name]

class string : 

    def __init__(self, value, name) :

        self.name = name
        self.value = value
        self.parents = []

        self.output = []

        _string_default_graph.strings.append(self)
        _string_default_graph.name_registry[name] = {"size" : len(self.value)}
    
    def get_value(self):

        return self.value
    
    def get_metadata(self):

        return _string_default_graph.name_registry[name]


class array : 

    def __init__(self, value, name) :

        self.name = name
        self.value = value
        self.parents = []

        self.output = []

        _string_default_graph.arrays.append(self)
        _string_default_graph.name_registry[name] = {"size" : len(array)}
    

    def get_value(self):

        return self.value

    def get_metadata(self) :

        return _string_default_graph.name_registry[name]


class Operation : 


    def __init__(self, inputs = [], name = ""):

        self.parents = []
        self.inputs = inputs

        self.output = []

        for i in range(len(self.inputs)) :

            tensor = self.inputs[i]

            if type(tensor) == str : 

                tensor = string(tensor, name = "string"+str(i))

                self.inputs[i] = tensor
            
            if type(tensor) == list : 

                tensor = array(tensor, name = "array"+str(i))

                self.inputs[i] = tensor
        
        #assign this op as parents of all inputs : 

        for node in self.inputs : 

            node.parents.append(self)
        
        #register the node : 
        _string_default_graph.operations.append(self)
        _string_default_graph.name_registry[name] = {}


    def compute(self, *args) :
        #empty method, operations will implement it
        pass


