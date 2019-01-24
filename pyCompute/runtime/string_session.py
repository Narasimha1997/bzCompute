from pyCompute.algorithms.postorder import Postorder
from pyCompute.text_processing.graph import Operation
from pyCompute.text_processing.graph import File
from pyCompute.text_processing.graph import array
from pyCompute.text_processing.graph import string

from pyCompute.graph import Graph

import numpy


class StringSession:

    def __init__(self):

        self.algorithm = Postorder

    def execute_graph(self, sequence, operation):

        executed = [False] * len(sequence)

        for i in range(len(sequence)):

            if executed[i]:
                continue
            

            node = sequence[i]

            if type(node) == string: 

                node.output = node.value
            
            elif type(node) == File :

                node.output = node.value

            elif type(node) == array :

                node.output = output

            else : 

                #operation, execute it : 
                
                node_inputs = [input_.output for input_ in node.inputs]

                node.output = node.compute(*node_inputs)
                 
            executed[i] = True

        return operation.output

    def run(self, graph, operation):

        traversal_seq = self.algorithm(operation).run(string_op = True)

        #print(traversal_seq)
        return self.execute_graph(traversal_seq, operation)
