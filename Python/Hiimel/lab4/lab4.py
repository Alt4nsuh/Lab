from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import time

def generate_word_graph(words):
    graph = {}
    for word in words:
        graph[word] = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in words:
                        graph[word].append(new_word)
    return graph

def shortest_path(start_word, target_word, graph):
    queue = deque([(start_word, [start_word])])
    visited = set([start_word])
    
    while queue:
        current_word, path = queue.popleft()
        if current_word == target_word:
            return path
        for neighbor in graph[current_word]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

def draw_word_graph(word_graph, shortest_path):
    G = nx.Graph(word_graph)
    pos = nx.spring_layout(G) 
    

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

    if shortest_path:
        edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=3.0, alpha=0.5, edge_color='r')

    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    word_list = ["fool", "cool", "pool", "poll", "pole", "pall", "fall", "fail", "foil", "foul", "pope", "pale", "sale", "sage", "page"]
    word_graph = generate_word_graph(word_list)

    start_word = 'cool'
    target_word = 'sage'

    shortest_path_list = shortest_path(start_word, target_word, word_graph)

    if shortest_path_list:
        print("Shortest path from", start_word, "to", target_word, ":", shortest_path_list)
    else:
        print("No path found from", start_word, "to", target_word)

    draw_word_graph(word_graph, shortest_path_list)
