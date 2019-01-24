from pyCompute.graph import Operation

class DFS :

    def __init__(self, operation):

        self.operation = operation


    def recursive_traversal(self, node, dfs_sequence, level):

        node.level = level
        level +=1
        
        dfs_sequence.append(node)

        for input_ in node.inputs : 

            if isinstance(input_, Operation):

                self.recursive_traversal(input_, dfs_sequence, level)


    def depth_traversal(self):

        dfs_sequence = []

        self.recursive_traversal(self.operation, dfs_sequence, 0)

        return dfs_sequence


    