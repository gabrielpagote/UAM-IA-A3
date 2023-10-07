import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# Posição dos nós
node_positions = {"A": (0, 25), "B": (0.180, 24), "C": (0.160, 20), "D": (0.420, 25), "E": (0.430, 21), "F": (0.450, 19), "G": (0.360, 16), "H": (0.250, 14.5), "I": (0.150, 13), "J": (0.153, 10), "K": (0.470, 11), "L": (0.500, 16), "M": (0.400, 1.8), "N": (0.240, -2), "O": (0.170, 0.4), "P": (0.460, 5.1), "Q": (0.700, 2.38)}

# Função para criar um pop-up
def solicitar_posicao():
    root = tk.Tk()
    root.title("Informe sua posição")
    label = tk.Label(root, text="Onde você se encontra neste exato momento?")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    # Função para obter a entrada 
    def obter_entrada():
        posicao = entry.get().strip().upper() 
        root.destroy() 
        if posicao not in G.nodes():
            mostrar_erro("Posição inválida. Insira um nó válido do grafo.")
        else:
            calcular_caminho(posicao)

    # Criar um botão para confirmar a entrada
    confirm_button = tk.Button(root, text="Confirmar", command=obter_entrada)
    confirm_button.pack()

    root.mainloop()

# Erro
def mostrar_erro(mensagem):
    error_window = tk.Tk()
    error_window.title("Erro")

    error_label = tk.Label(error_window, text=mensagem)
    error_label.pack()

    error_window.mainloop()

# Função para calcular o caminho mais curto
def calcular_caminho(posicao):
    # Dijkstra
    def dijkstra(graph, start, end):
        shortest_path = nx.shortest_path(graph, source=start, target=end, weight='weight')
        shortest_distance = nx.shortest_path_length(graph, source=start, target=end, weight='weight')
        return shortest_path, shortest_distance

    # Função para calcular o caminho mais curto
    def shortest_path(graph, start_node, end_node):
        shortest_path, shortest_distance = dijkstra(graph, start_node, end_node)
        return shortest_path, shortest_distance

    # Calcular o caminho mais curto de posicao para Q
    shortest_path_to_Q, shortest_distance_to_Q = shortest_path(G, posicao, "Q")

    # Calcular o caminho mais curto de posicao para A
    shortest_path_to_A, shortest_distance_to_A = shortest_path(G, posicao, "A")

    # Comparar os resultados
    if shortest_distance_to_Q < shortest_distance_to_A:
        resultado_comparacao = f"O caminho mais curto é de {posicao} para Q."
    elif shortest_distance_to_A < shortest_distance_to_Q:
        resultado_comparacao = f"O caminho mais curto é de {posicao} para A."
    else:
        resultado_comparacao = "Ambos os caminhos têm a mesma distância mais curta."

    # Obter o caminho mais curto
    caminho_vermelho, _ = shortest_path(G, posicao, "Q")
    caminho_roxo, _ = shortest_path(G, posicao, "A")

    # Criar uma janela para exibir informações
    info_window = tk.Tk()
    info_window.title("Informações do Caminho")

    # Exibir informações sobre o caminho mais curto distância etc.....
    info_label = tk.Label(info_window, text=f"Caminho mais curto de {posicao} para Q: {shortest_path_to_Q}")
    info_label.pack()

    info_label = tk.Label(info_window, text=f"Distância mais curta de {posicao} para Q: {shortest_distance_to_Q}")
    info_label.pack()

    info_label = tk.Label(info_window, text=f"Caminho mais curto de {posicao} para A: {shortest_path_to_A}")
    info_label.pack()

    info_label = tk.Label(info_window, text=f"Distância mais curta de {posicao} para A: {shortest_distance_to_A}")
    info_label.pack()
    
    info_label = tk.Label(info_window, text=resultado_comparacao)
    info_label.pack()

    # Exibir o grafo
    plt.figure(figsize=(5, 5))
    nx.draw(G, pos=node_positions, with_labels=True, node_size=500, node_color="skyblue")
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=labels)
    nx.draw_networkx_edges(G, pos=node_positions, edgelist=G.edges(), width=2, edge_color="gray")

    # Exibir o caminho mais curto no gráfico
    path_edges = [(caminho_vermelho[i], caminho_vermelho[i + 1]) for i in range(len(caminho_vermelho) - 1)]
    nx.draw_networkx_edges(G, pos=node_positions, edgelist=path_edges, width=2, edge_color="red")

    path_edges = [(caminho_roxo[i], caminho_roxo[i + 1]) for i in range(len(caminho_roxo) - 1)]
    nx.draw_networkx_edges(G, pos=node_positions, edgelist=path_edges, width=2, edge_color="purple")

    # Do matplotlib para interface gráfica do tkinter
    canvas = FigureCanvasTkAgg(plt.gcf(), master=info_window)
    canvas.get_tk_widget().pack()

    info_window.mainloop()

# Exiba o gráfico e solicite a posição do usuário 
plt.figure(figsize=(5, 5))
nx.draw(G, pos=node_positions, with_labels=True, node_size=500, node_color="skyblue")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=labels)
nx.draw_networkx_edges(G, pos=node_positions, edgelist=G.edges(), width=2, edge_color="gray")

# Crie um botão 
solicitar_posicao_button = tk.Button(plt.gcf().canvas.get_tk_widget(), text="Informe sua posição", command=solicitar_posicao)
solicitar_posicao_button.pack()

plt.show()
