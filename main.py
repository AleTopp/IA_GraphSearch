import string
from uninfo_algorithms import *
from nodo import GraphNodo as Nodo
from mappa import edges, edge_labels
from mappa import show_map, rand_edges_3 as rand_edges

def main():
    N = 10
    E = 20
    nodes = [ letter for letter in string.ascii_uppercase[0:N]]
    #edges, edge_labels = rand_edges(nodes, E)

    nodi = Nodo.get_nodes_from_edges(edges, nodes)

    # --- INIZIO RICERCA ---
    start = nodi['B'] #[nodes[random.randrange(0, len(nodes))]]
    stop = nodi['F'] #[nodes[random.randrange(0, len(nodes))]]
    
    print(f"Ciao, mi trovo in {start.get_name()} e devo arrivare in {stop.get_name()}")

    res = []

    path, cost, exp = breadth_first(start, stop)
    res.append(["Breadth-First", str(path), str(cost), str(exp)])
    
    path, cost, exp = dijkstra_algo(start, stop)
    res.append(["Uniform-Cost", str(path), str(cost), str(exp)])

    path, cost, exp = depth_first(start, stop)
    res.append(["Depth-First", str(path), str(cost), str(exp)])

    for i in range(5):
        path, cost, exp = depth_limited(start, stop, i)
        res.append([f"Depth-Lim ({i})", str(path), str(cost), str(exp)])

    


    print(f'{"Algo":<15}|{"Path":<25}|{"Cost":>5}|{"N.Exp":>7}')
    print("-------------------------------------------------------")
    for row in res:
        print(f'{row[0]:<15}|{row[1]:<25}|{row[2]:>5}|{row[3]:>5}')

    show_map(nodes, edges, edge_labels)


if __name__ == "__main__":
    main()