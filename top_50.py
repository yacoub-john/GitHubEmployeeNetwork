import networkx as nx
import jsonlines

# Import the graph from the GraphML file
G_imported = nx.read_graphml("developer_network.graphml")

# Calculate the number of nodes and edges
num_nodes = G_imported.number_of_nodes()
num_edges = G_imported.number_of_edges()
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

# Run the PageRank algorithm
pagerank = nx.pagerank(G_imported)

# Get the top 50 nodes by PageRank
top_50_nodes = sorted(pagerank, key=pagerank.get, reverse=True)[:50]

# # Load the JSON data and create a mapping from node ID to name
# names = {}
# with jsonlines.open("filtered_data.json", "r") as reader:
#     for user in reader:
#         names[str(user["id"])] = user["login"]
#
# # Add names to the top 50 nodes based on the node ID
# top_50_with_names = {}
# for node in top_50_nodes:
#     top_50_with_names[node] = names.get(node, "Unknown")

# Save the top 50 nodes with their names to a file
with open("top_50_nodes_with_names.txt", "w", encoding="utf-8") as f:
    for name in top_50_nodes:
        f.write(f"Node ID: {name}\n")

print("Top 50 nodes with their names have been saved to top_50_nodes_with_names.txt")
