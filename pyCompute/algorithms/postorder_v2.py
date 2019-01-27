from pyCompute.graph import Operation
from pyCompute.graph import *
from pyCompute.text_processing.graph import Operation as TextOp
from pyCompute.text_processing.graph import *


def node_executor_v2(node, feed_dict):

    if type(node) == placeholder:
        node.feed_value(feed_dict[node.name])
        node.output = node.value

    elif type(node) == Variable:

        node.output = node.input_value

    elif type(node) == constant:

        node.output = node.input_value

    else:

        inputs = [input_.output for input_ in node.inputs]

        node.output = node.compute(*inputs)


def string_executor_v2(node):

        if type(node) == string:

            node.output = node.value

        elif type(node) == File:

            node.output = node.value

        elif type(node) == array:

            node.output = output

        else:

            # operation, execute it :

            node_inputs = [input_.output for input_ in node.inputs]

            node.output = node.compute(*node_inputs)



class Postorder2x:

    def __init__(self, operation, feed_dict, is_string=False):

        self.operation = operation
        self.feed_dict = feed_dict
        self.is_string = is_string

    def recursive_traversal(self, node, node_registry, level):

        if isinstance(node, Operation):

            for input_node in node.inputs:
                self.recursive_traversal(input_node, node_registry, level)

        # node.level = level
        # level += 1
        node_executor_v2(node, self.feed_dict)
        node_registry[node.name] = node.output

    def string_recursive_traversal(self, node, node_registry, level):

        if isinstance(node, TextOp):
            for input_node in node.inputs:

                self.string_recursive_traversal(input_node, node_registry, level)

        # node.level = level
        # level += 1
        string_executor_v2(node)
        node_registry[node] = node.output

    def run(self):

        node_registry = {}

        if self.is_string:

            self.string_recursive_traversal(self.operation, node_registry, 0)

            return node_registry[self.operation]

        self.recursive_traversal(self.operation, node_registry, 0)

        return node_registry[self.operation.name]
