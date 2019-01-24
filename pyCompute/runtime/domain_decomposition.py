from pyCompute.runtime.session import SequentialSession
from pyCompute.graph import *
from threading import Thread
import copy
from pyCompute.error import Exception
from pyCompute.algorithms.postorder import Postorder

from multiprocessing.dummy import Pool as ThreadPool


def check_hyperthreading(cpu_info='/proc/cpuinfo'):

    with open(cpu_info) as file_handler:
        cpuinfo = dict(map(
            lambda line: map(str.strip, line.split(':', 1)),
            filter(lambda line: ':' in line, file_handler)
        ))

    return int(cpuinfo['siblings'])


def pooled_executor(data):

    graph = data['graph']
    operation = data['operation']
    sequence = data['sequence']
    feed = data['feed']
    name = data['name']

    return {name: SequentialSession().run(graph, operation, feed)}


class __Worker__(Thread):

    def __init__(self, operation, feed_dict, graph, seq, name="worker"):

        Thread.__init__(self)

        self.operation = operation
        self.feed_dict = feed_dict
        self.graph = graph
        self._node_output = None
        self.name = name
        self.seq = seq

    def run(self):

        # create a new sequential session :
        session = SequentialSession()

        self._node_output = session.execute_graph(
            self.seq,
            self.operation,
            self.feed_dict
        )

        del session

    def join(self):

        # returns output back to master upon join :
        return self._node_output


class MasterSession():

    def __init__(self, graph, n_workers=1, pooled=False):

        self.graph = graph
        self.n_workers = n_workers
        self.__workers__ = []

        # Parameters for thread pooling :
        self.pooled = pooled
        self.pool = None
        self.pooled_data = []

    def __create_pool__(self):

        cores = check_hyperthreading()
        return ThreadPool(cores)

    def get_replica_graphs(self, n_workers, operation):

        # returns multiple copies of post order graph sequence :
        postoder = Postorder(operation).run()
        copies = []
        for i in range(n_workers):
            copies.append(copy.deepcopy(postoder))
        return copies

    def get_replicated_op(self, sequence, operation):

        for node in sequence:
            if node.name == operation.name:
                return node

    def setup(self, operation, feeds):

        __workers__ = []

        __replicated_graphs__ = self.get_replica_graphs(
            self.n_workers, operation)

        # for pooled worker mode :
        if self.pooled:
            data = []
            count = 0
            for replica in __replicated_graphs__:

                op = self.get_replicated_op(replica, operation)
                name = "Worker"+str(count)
                feed = feeds[count]

                data.append({
                    "name": name, "feed": feed, "sequence": replica, "graph": self.graph, "operation": op
                })

                count += 1

            self.pooled_data = data
            self.pool = self.__create_pool__()

            return

        # for normal master-slave mode :
        count = 0

        for feed in feeds:
            nodes = feed.keys()

            op = self.get_replicated_op(
                __replicated_graphs__[count], operation)

            worker = __Worker__(op, feed, self.graph, __replicated_graphs__[
                                count], name="worker" + str(count))
            count += 1
            __workers__.append(worker)

        self.__workers__ = __workers__

    def run(self):

        # for pooled workers :

        if self.pooled:

            results = self.pool.map(pooled_executor, self.pooled_data)
            self.pool.close()

            self.pool.join()
            # grabage collection :
            del self.pool
            del self.pooled_data

            return results

        # for non-pooled worker mode :

        for worker in self.__workers__:

            worker.start()
        results = {}

        for worker in self.__workers__:
            results[worker.name] = worker.join()

        del self.__workers__

        return results
