from nodo import GraphNodo as Nodo, TreeNodo as TNodo, PrioNodo as PNodo
from queue import Queue, LifoQueue, PriorityQueue

def breadth_first(start: Nodo, stop: Nodo):
    fringe = Queue()
    fringe_nodes = Queue()
    expanded = []
    root = TNodo(start.get_name())
    
    current = start
    current_node = root

    while current != stop:
        if current not in expanded:
            for (neig, cost) in current.get_neighbours():
                fringe.put(neig)
                fringe_nodes.put(TNodo(neig.get_name(), current_node, cost))

            expanded.append(current)

        try:
            current = fringe.get_nowait()
            current_node = fringe_nodes.get_nowait()
        except:
            return ([], "...", len(expanded))

    solution_node = current_node
    tot_cost = 0
    path = []

    while solution_node != None:
        tot_cost += solution_node.get_cost_to_par()
        path = [solution_node] + path
        solution_node = solution_node.get_parent()

    return (path, tot_cost, len(expanded))

def dijkstra_algo(start: Nodo, stop: Nodo):
    fringe = PriorityQueue()
    fringe_nodes = PriorityQueue()
    expanded = []
    root = TNodo(start.get_name())
    
    current = start
    current_node = root
    current_cost = 0

    while current != stop:
        if current not in expanded:
            for (neig, cost) in current.get_neighbours():
                fringe.put(PNodo(current_cost + cost, neig))
                fringe_nodes.put(PNodo(current_cost + cost, TNodo(neig.get_name(), current_node, cost)))

            expanded.append(current)

        try:
            it1 = fringe.get_nowait()
            it2 = fringe_nodes.get_nowait()
        except:
            return ([], "...", len(expanded))
        
        current = it1.item
        current_node = it2.item
        current_cost = it2.priority

    solution_node = current_node
    tot_cost = 0
    path = []

    while solution_node != None:
        tot_cost += solution_node.get_cost_to_par()
        path = [solution_node] + path
        solution_node = solution_node.get_parent()

    return (path, tot_cost, len(expanded))

def depth_first(start: Nodo, stop: Nodo):
    fringe = LifoQueue()
    fringe_nodes = LifoQueue()
    expanded = []
    root = TNodo(start.get_name())
    
    current = start
    current_node = root

    while current != stop:
        if current not in expanded:
            for (neig, cost) in current.get_neighbours():
                fringe.put(neig)
                fringe_nodes.put(TNodo(neig.get_name(), current_node, cost))

            expanded.append(current)

        try:
            current = fringe.get_nowait()
            current_node = fringe_nodes.get_nowait()
        except:
            return ([], "...", len(expanded))

    solution_node = current_node
    tot_cost = 0
    path = []

    while solution_node != None:
        tot_cost += solution_node.get_cost_to_par()
        path = [solution_node] + path
        solution_node = solution_node.get_parent()

    return (path, tot_cost, len(expanded))

def depth_limited(start: Nodo, stop: Nodo, limit: int):
    fringe = LifoQueue()
    fringe_nodes = LifoQueue()
    expanded = []
    root = TNodo(start.get_name())
    
    current = start
    current_node = root
    cutoff = False

    while current != stop:
        cutoff = current_node.get_depth() >= limit

        if current not in expanded and not cutoff:
            for (neig, cost) in current.get_neighbours():
                fringe.put(neig)
                fringe_nodes.put(TNodo(neig.get_name(), current_node, cost))

            expanded.append(current)

        try:
            current = fringe.get_nowait()
            current_node = fringe_nodes.get_nowait()
        except:
            return ([], "...", len(expanded))

    solution_node = current_node
    tot_cost = 0
    path = []

    while solution_node != None:
        tot_cost += solution_node.get_cost_to_par()
        path = [solution_node] + path
        solution_node = solution_node.get_parent()

    return (path, tot_cost, len(expanded))