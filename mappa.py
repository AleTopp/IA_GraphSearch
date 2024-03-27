import random
import networkx as nx
import matplotlib.pyplot as plt

nodes10 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
edges = [('A', 'C', {'cost': 8}), ('A', 'B', {'cost': 8}), ('B', 'E', {'cost': 10}), ('C', 'D', {'cost': 18}), ('C', 'F', {'cost': 3}), ('D', 'A', {'cost': 8}), ('E', 'I', {'cost': 4}), ('F', 'G', {'cost': 16}), ('F', 'D', {'cost': 5}), ('G', 'H', {'cost': 13}), ('G', 'I', {'cost': 5}), ('H', 'D', {'cost': 9}), ('I', 'H', {'cost': 3}), ('J', 'I', {'cost': 3}), ('J', 'B', {'cost': 14})]
weighted_edges = [(edge[0], edge[1], edge[2]['cost']) for edge in edges]
edge_labels = {(edge[0], edge[1]): edge[2]['cost'] for edge in edges}

def rand_edges_1(nodes = nodes10):
    edges = []
    for i in range(20):
        x = random.randrange(0, len(nodes))
        y = random.randrange(0, len(nodes))
        z = random.randrange(1, 20)
        if x == y:
            z = 0
        edges.append((nodes[x], nodes[y], {'cost': z}))

    edge_labels = {(edge[0], edge[1]): edge[2]['cost'] for edge in edges}
    return edges, edge_labels

def rand_edges_2(nodes = nodes10, num_edges = 20):
    edges = []
    num_edges = max(num_edges, len(nodes))

    for n in nodes:
        for i in range(num_edges//len(nodes)):
            x = random.randrange(0, len(nodes))
            z = random.randrange(1, 20)

            if n == nodes[x]:
                continue

            isIn = False
            for e in edges:
                if (e[0] == n and e[1] == nodes[x]) or (e[0] == nodes[x] and e[1] == n):
                    isIn = True
                    break

            if not isIn:
                edges.append((n, nodes[x], {'cost': z}))

    edge_labels = {(edge[0], edge[1]): edge[2]['cost'] for edge in edges}
    return edges, edge_labels

def rand_edges_3(nodes = nodes10, num_edges = 15):
    edges = []

    for i in range(num_edges):
        n1 = nodes[i % len(nodes)]
        n2 = nodes[random.randrange(0, len(nodes))]
        z = random.randrange(1, 20)

        if n1 == n2:
            continue

        isIn = False
        for e in edges:
            if (e[0] == n1 and e[1] == n2) or (e[0] == n2 and e[1] == n1):
                isIn = True
                break

        if not isIn:
            edges.append((n1, n2, {'cost': z}))

    edge_labels = {(edge[0], edge[1]): edge[2]['cost'] for edge in edges}
    return edges, edge_labels

def show_map(nodes, edges, edge_labels):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    #G.add_weighted_edges_from(weighted_edges)

    pos = nx.kamada_kawai_layout(G)

    nx.draw_networkx_nodes(G, pos, node_size = 300)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=edges, arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()