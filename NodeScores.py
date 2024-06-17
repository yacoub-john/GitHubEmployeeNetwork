import matplotlib.pyplot as plt
from pyvis.network import Network
import networkx as nx


# Create a figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Define the graph structure
nodes = range(6)
edges = [(0, 2), (0, 3), (0, 4), (0, 5)]
contact_times = [5, 1, 2, 12, 1]

# Plot 1: Number of contacts (node degree)
G1 = nx.Graph()
G1.add_edges_from(edges)

pos = nx.spring_layout(G1, seed=1)  # positions for all nodes

nx.draw(G1, pos, node_color='black', node_size=700, width=2, ax=axs[0])
nx.draw_networkx_nodes(G1, pos, nodelist=[0], node_color='red', node_size=700, ax=axs[0])
# nx.draw_networkx_labels(G1, pos, font_size=14, font_color="red", ax=axs[0])
net = Network(directed=True, notebook=True)
net.from_nx(G1)
net.show('nodes.html')


axs[0].set_title("(1) # of contacts (node degree)\nIntuitive\nDoesn't consider time spent in contact")
axs[0].axis('off')

# Plot 2: Total contact time
G2 = nx.Graph()
for edge, time in zip(edges, contact_times):
    G2.add_edge(*edge)

nx.draw(G2, pos, with_labels=False, node_color='black', node_size=700, width=2, ax=axs[1])
nx.draw_networkx(G2, pos, nodelist=[0], node_color='red', node_size=700, ax=axs[1])
nx.draw_networkx_labels(G2, pos, font_color="red", ax=axs[1])

axs[1].set_title("(2) Total contact time\nConsiders contact time\nLong contacts skew result")
axs[1].axis('off')

# Plot 3: Sum of contact times in geometric function
beta = 0.1
geometric_sum = 4 - sum(beta**time for time in contact_times)

G3 = nx.Graph()
for edge, time in zip(edges, contact_times):
    G3.add_edge(*edge, weight=time)

nx.draw(G3, pos, with_labels=False, node_color='black', node_size=700, width=2, ax=axs[2])
nx.draw_networkx_nodes(G3, pos, nodelist=[0], node_color='red', node_size=700, ax=axs[2])
# nx.draw_networkx_edge_labels(G3, pos, font_color='red', ax=axs[2])
nx.draw_networkx_labels(G3, pos, font_size=14, font_color="red", ax=axs[2])

axs[2].set_title("(3) Sum of contact times in geometric function\nConsiders contact time\nVery long contacts don't count as much")
axs[2].axis('off')

plt.show()
