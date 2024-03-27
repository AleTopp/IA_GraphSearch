class GraphNodo():
    def __init__(self, name, neig = None):
        self.name = name

        if isinstance(neig, type(None)):
            self.neig = []
        else:
            self.neig = neig

    def get_name(self):
        return self.name
    
    def get_neighbours(self):
        return self.neig
    
    def get_neig_names(self):
        names = [neig[0].get_name() for neig in self.get_neighbours()]
        str = ", ".join(names)
        return f"[{str}]"
    
    def add_neighbour(self, node, cost: int):
        self.neig.append((node, cost))

    def __str__(self):
        return f"<{self.get_name()}, {self.get_neig_names()}>"
    
    def __repr__(self):
        return self.get_name()
    
    def __eq__(self, other):
        if isinstance(other, GraphNodo):
            return self.get_name() == other.get_name()
        
    def __ne__(self, other):
        return not self == other
    
    @staticmethod
    def get_nodes_from_edges(edges, nodes):
        nodi = {n: GraphNodo(n) for n in nodes}

        for e in edges:
            n1 = e[0]
            n2 = e[1]
            cost = e[2]['cost']
            nodi[n1].add_neighbour(nodi[n2], cost)
            nodi[n2].add_neighbour(nodi[n1], cost)

        return nodi
    

class TreeNodo():
    def __init__(self, name, parent = None, cost = 0):
        self.name = name
        self.parent = parent
        self.cost_to_parent = cost

        if parent != None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def get_depth(self):
        return self.depth
    
    def get_cost_to_par(self):
        return self.cost_to_parent
    
    def __str__(self):
        return f"<{self.get_name()} <-< {self.get_parent()}>"
    
    def __repr__(self):
        return self.get_name()
    
# --- Comparable Prio Item ---
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioNodo:
    priority: int
    item: Any=field(compare=False)
    
# --- Printable Queue ---
from queue import Queue
class MyQueue(Queue):
    def __str__(self) -> str:
        return f"<<{str(list(self.queue))}<<"
    
    def __repr__(self) -> str:
        return self.__str__()