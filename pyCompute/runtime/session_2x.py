from pyCompute.algorithms.postorder_v2 import Postorder2x

class Session2x():

    def __init__(self, graph) :

        self.graph = graph
        self.algorithm = Postorder2x

    
    def run(self, operation, feed_dict = {}) :

        recursive_executor = self.algorithm(operation, feed_dict)

        return recursive_executor.run()


class StringSession2x() :

    def __init__(self, graph) :

        self.graph = graph
        self.algorithm = Postorder2x
    
    def run(self, operation) :

        recursive_executor = self.algorithm(operation, None, is_string = True)

        return recursive_executor.run()
