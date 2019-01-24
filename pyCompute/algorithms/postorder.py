from pyCompute.graph import Operation
from pyCompute.text_processing.graph import Operation as TextOp

class Postorder  :

    def __init__(self, operation):

        self.operation = operation


    def recursive_traversal(self, node, computation_seq, level):

        if isinstance(node, Operation):

            for input_node in node.inputs :
                self.recursive_traversal(input_node, computation_seq, level)

        #node.level = level
        #level += 1
        computation_seq.append(node)
    

    def string_recursive_traversal(self, node, computation_seq, level) :

        if isinstance(node, TextOp):
            for input_node in node.inputs :

                self.string_recursive_traversal(input_node, computation_seq, level)

        #node.level = level
        #level += 1
        computation_seq.append(node)



    def run(self, string_op = False):

        computation_sequence = []

        if string_op :

            self.string_recursive_traversal(self.operation, computation_sequence, 0)
            
            return computation_sequence

        self.recursive_traversal(self.operation, computation_sequence, 0)

        return computation_sequence  

