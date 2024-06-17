import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Assuming `G` is your NetworkX graph
# Import the graph from the GraphML file
G = nx.read_graphml("developer_network.graphml")

# Calculate the number of nodes and edges
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

# Calculate the metrics
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G, k=100, weight='weight')
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G, weight='weight')
clustering_coefficient = nx.clustering(G, weight='weight')

# Function to save plot with binned data
def save_plot(data, title, xlabel, ylabel, filename, bins=10):
    values = list(data.values())
    counts, bin_edges = np.histogram(values, bins=bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    proportions = counts / len(values)

    plt.figure(figsize=(10, 6))
    plt.bar(bin_centers, proportions, width=bin_edges[1] - bin_edges[0], color='b')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Function to save binned data to a text file
def save_data(data, filename, bins=10):
    values = list(data.values())
    counts, bin_edges = np.histogram(values, bins=bins)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    proportions = counts / len(values)

    with open(filename, 'w') as f:
        for center, proportion in zip(bin_centers, proportions):
            f.write(f"{center}: {proportion}\n")

# Degree Centrality
save_plot(degree_centrality, 'Degree Centrality Distribution', 'Degree Centrality', 'Proportion of Users', 'degree_centrality.png')
save_data(degree_centrality, 'degree_centrality.txt')

# Betweenness Centrality
save_plot(betweenness_centrality, 'Betweenness Centrality Distribution', 'Betweenness Centrality', 'Proportion of Users', 'betweenness_centrality.png')
save_data(betweenness_centrality, 'betweenness_centrality.txt')

# Closeness Centrality
save_plot(closeness_centrality, 'Closeness Centrality Distribution', 'Closeness Centrality', 'Proportion of Users', 'closeness_centrality.png')
save_data(closeness_centrality, 'closeness_centrality.txt')

# Eigenvector Centrality
save_plot(eigenvector_centrality, 'Eigenvector Centrality Distribution', 'Eigenvector Centrality', 'Proportion of Users', 'eigenvector_centrality.png')
save_data(eigenvector_centrality, 'eigenvector_centrality.txt')

# Clustering Coefficient
save_plot(clustering_coefficient, 'Clustering Coefficient Distribution', 'Clustering Coefficient', 'Proportion of Users', 'clustering_coefficient.png')
save_data(clustering_coefficient, 'clustering_coefficient.txt')

print("Plots and data files have been saved.")
