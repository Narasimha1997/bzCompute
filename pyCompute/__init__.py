from pyCompute.error import Exception
from pyCompute.graph import *
from pyCompute.algorithms import DFS, Postorder
from pyCompute.KernelOperations import *
from pyCompute.runtime.session import SequentialSession
from pyCompute.runtime.domain_decomposition import MasterSession

#string processing modules :


import pyCompute.text_processing.graph  as text 
import pyCompute.text_processing.StringOperations as text_ops 
from pyCompute.runtime.string_session import StringSession


default_graph = Graph()

string_default_graph = text.Graph()

string_default_graph.create_graph()

default_graph.create_graph()

def get_default_graph():

    return default_graph

def get_default_string_graph() :

    return string_default_graph