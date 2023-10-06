import networkx as nx
import matplotlib.pyplot as plt

# Cria o grafo não direcionado
G = nx.Graph()

# Adiciona os nós
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")
G.add_node("G")
G.add_node("H")
G.add_node("I")
G.add_node("J")
G.add_node("K")
G.add_node("L")
G.add_node("M")
G.add_node("N")
G.add_node("O")
G.add_node("P")
G.add_node("Q")

# Adiciona valor nas arestas
G.add_edge("A", "B", weight=168)
G.add_edge("B", "C", weight=110)
G.add_edge("B", "D", weight=265)
G.add_edge("C", "E", weight=274)
G.add_edge("C", "I", weight=261)
G.add_edge("D", "E", weight=84)
G.add_edge("E", "F", weight=92)
G.add_edge("I", "J", weight=102)
G.add_edge("F", "G", weight=131)
G.add_edge("F", "L", weight=146)
G.add_edge("G", "H", weight=140)
G.add_edge("H", "I", weight=126)
G.add_edge("J", "K", weight=426)
G.add_edge("K", "L", weight=149)
G.add_edge("J", "O", weight=398)
G.add_edge("K", "P", weight=228)
G.add_edge("O", "N", weight=99)
G.add_edge("N", "M", weight=300)
G.add_edge("M", "P", weight=235)
G.add_edge("P", "Q", weight=435)

# Acesso dos nós e das arestas
nodes = G.nodes()
edges = G.edges(data=True)

# Aqui que eu tenho que aprender 100% (POSIÇÃO DOS NÓS NO GRAFO)
node_positions = {"A": (0, 25), "B": (0.180, 24), "C": (0.160, 20), "D": (0.420, 25), "E": (0.430, 21), "F": (0.450, 19), "G": (0.360, 16), "H": (0.250, 14.5), "I": (0.150, 13), "J": (0.153, 10), "K": (0.470, 11), "L": (0.500, 16), "M": (0.400, 1.8), "N": (0.240, -2), "O": (0.170, 0.4), "P": (0.460, 5.1), "Q": (0.700, 2.38)}

# Implementação do algoritmo de Dijkstra
def dijkstra(graph, start, end):
    shortest_path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    shortest_distance = nx.shortest_path_length(graph, source=start, target=end, weight='weight')
    return shortest_path, shortest_distance

start_node = input("Onde você se encontra neste exato momento ? ")

# Função para calcular o caminho mais curto
def shortest_path(graph, start_node, end_node):
    shortest_path, shortest_distance = dijkstra(graph, start_node, end_node)
    return shortest_path, shortest_distance

# Calcular o caminho mais curto de I para Q
shortest_path_to_Q, shortest_distance_to_Q = shortest_path(G, start_node, "Q")
print(f"Caminho mais curto de {start_node} para Q: {shortest_path_to_Q}")
print(f"Distância mais curta de {start_node} para Q: {shortest_distance_to_Q}")

# Calcular o caminho mais curto de I para A
shortest_path_to_A, shortest_distance_to_A = shortest_path(G, start_node, "A")
print(f"Caminho mais curto de {start_node} para A: {shortest_path_to_A}")
print(f"Distância mais curta de {start_node} para A: {shortest_distance_to_A}")

# Comparar os resultados
if shortest_distance_to_Q < shortest_distance_to_A:
    print(f"O caminho mais curto é de {start_node} para Q.")
elif shortest_distance_to_A < shortest_distance_to_Q:
    print(f"O caminho mais curto é de {start_node} para A.")
else:
    print("Ambos os caminhos têm a mesma distância mais curta.")

# Obter o caminho mais curto
caminho_vermelho, _ = shortest_path(G, start_node, "Q")
caminho_roxo, _ = shortest_path(G, start_node, "A")

# Nós
nx.draw(G, pos=node_positions, with_labels=True, node_size=500, node_color="skyblue")

# Arestas
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=labels)
nx.draw_networkx_edges(G, pos=node_positions, edgelist=G.edges(), width=2, edge_color="gray")

# Caminho mais curto no gráfico
path_edges = [(caminho_vermelho[i], caminho_vermelho[i + 1]) for i in range(len(caminho_vermelho) - 1)]
nx.draw_networkx_edges(G, pos=node_positions, edgelist=path_edges, width=2, edge_color="red")

path_edges = [(caminho_roxo[i], caminho_roxo[i + 1]) for i in range(len(caminho_roxo) - 1)]
nx.draw_networkx_edges(G, pos=node_positions, edgelist=path_edges, width=2, edge_color="purple")

# Mostra o Grafo
plt.show()