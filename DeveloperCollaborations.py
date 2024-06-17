import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('developers.csv')

# Filter developers who have 3 or more public repositories
df = df[df['Public Repositories'] >= 3]

# Create graph data structures using NetworkX
G = nx.Graph()
G_with_phd_weights = nx.Graph()
G_with_java_weights = nx.Graph()
G_with_python_weights = nx.Graph()

# Add nodes (developers) to all graphs
for index, row in df.iterrows():
    username = row['username']
    bio = row['Bio']
    if pd.notna(bio):  # Check if bio is not NaN
        G.add_node(username, bio=bio, company=row['Company'], location=row['Location'])
        G_with_phd_weights.add_node(username, bio=bio, company=row['Company'], location=row['Location'])
        G_with_java_weights.add_node(username, bio=bio, company=row['Company'], location=row['Location'])
        G_with_python_weights.add_node(username, bio=bio, company=row['Company'], location=row['Location'])
    else:
        G.add_node(username, company=row['Company'], location=row['Location'])
        G_with_phd_weights.add_node(username, company=row['Company'], location=row['Location'])
        G_with_java_weights.add_node(username, company=row['Company'], location=row['Location'])
        G_with_python_weights.add_node(username, company=row['Company'], location=row['Location'])

# Add edges for following relationships in all graphs
for index, row in df.iterrows():
    username = row['username']
    following_names = row['following_names'].split(',')
    for following_name in following_names:
        if following_name in G.nodes:
            G.add_edge(username, following_name, relation='following')
            weight = 2.0 if 'Phd' in G.nodes.get(username, {}).get('bio', '') or 'Phd' in G.nodes.get(following_name, {}).get('bio', '') else 1.0
            G_with_phd_weights.add_edge(username, following_name, relation='following', weight=weight)
            weight = 2.0 if 'Java' in G.nodes.get(username, {}).get('bio', '') or 'Java' in G.nodes.get(following_name, {}).get('bio', '') else 1.0
            G_with_java_weights.add_edge(username, following_name, relation='following', weight=weight)
            weight = 2.0 if 'Python' in G.nodes.get(username, {}).get('bio', '') or 'Python' in G.nodes.get(following_name, {}).get('bio', '') else 1.0
            G_with_python_weights.add_edge(username, following_name, relation='following', weight=weight)

# Add edges for follower relationships in all graphs
for index, row in df.iterrows():
    username = row['username']
    followers_names = row['followers_name'].split(',')
    for follower_name in followers_names:
        G.add_edge(follower_name, username, relation='collaborator')
        weight = 2.0 if 'Phd' in G.nodes.get(username, {}).get('bio', '') or 'Phd' in G.nodes.get(follower_name, {}).get('bio', '') else 1.0
        G_with_phd_weights.add_edge(follower_name, username, relation='collaborator', weight=weight)
        weight = 2.0 if 'Java' in G.nodes.get(username, {}).get('bio', '') or 'Java' in G.nodes.get(follower_name, {}).get('bio', '') else 1.0
        G_with_java_weights.add_edge(follower_name, username, relation='collaborator', weight=weight)
        weight = 2.0 if 'Python' in G.nodes.get(username, {}).get('bio', '') or 'Python' in G.nodes.get(follower_name, {}).get('bio', '') else 1.0
        G_with_python_weights.add_edge(follower_name, username, relation='collaborator', weight=weight)

# Weighted PageRank for the main graph
pr_main = nx.pagerank(G, weight='weight')

# Weighted PageRank for the graph with higher weights for Phd users
pr_with_phd_weights = nx.pagerank(G_with_phd_weights, weight='weight')

# Weighted PageRank for the graph with higher weights for Java users
pr_with_java_weights = nx.pagerank(G_with_java_weights, weight='weight')

# Weighted PageRank for the graph with higher weights for Python users
pr_with_python_weights = nx.pagerank(G_with_python_weights, weight='weight')

# Get top 50 nodes from each graph based on PageRank scores
top_50_main = sorted(pr_main.items(), key=lambda x: x[1], reverse=True)[:50]
top_50_with_phd_weights = sorted(pr_with_phd_weights.items(), key=lambda x: x[1], reverse=True)[:50]
top_50_with_java_weights = sorted(pr_with_java_weights.items(), key=lambda x: x[1], reverse=True)[:50]
top_50_with_python_weights = sorted(pr_with_python_weights.items(), key=lambda x: x[1], reverse=True)[:50]

# Save top 50 nodes and their PageRank scores to files
with open('top_50_main_graph.txt', 'w') as f:
    f.write("Top 50 nodes in main graph:\n")
    for node, score in top_50_main:
        f.write(f"{node}: {score}\n")

with open('top_50_with_phd_weights_graph.txt', 'w') as f:
    f.write("Top 50 nodes in graph with higher weights for Phd users:\n")
    for node, score in top_50_with_phd_weights:
        f.write(f"{node}: {score}\n")

with open('top_50_with_java_weights_graph.txt', 'w') as f:
    f.write("Top 50 nodes in graph with higher weights for Java users:\n")
    for node, score in top_50_with_java_weights:
        f.write(f"{node}: {score}\n")

with open('top_50_with_python_weights_graph.txt', 'w') as f:
    f.write("Top 50 nodes in graph with higher weights for Python users:\n")
    for node, score in top_50_with_python_weights:
        f.write(f"{node}: {score}\n")

# Print nodes and edges for the main graph
print("\nMain Graph:")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")


# Print nodes and edges for the graph with higher weights for Phd users
print("\nGraph with Higher Weights for Phd Users:")
print(f"Number of nodes: {G_with_phd_weights.number_of_nodes()}")
print(f"Number of edges: {G_with_phd_weights.number_of_edges()}")


# Print nodes and edges for the graph with higher weights for Java users
print("\nGraph with Higher Weights for Java Users:")
print(f"Number of nodes: {G_with_java_weights.number_of_nodes()}")
print(f"Number of edges: {G_with_java_weights.number_of_edges()}")


# Print nodes and edges for the graph with higher weights for Python users
print("\nGraph with Higher Weights for Python Users:")
print(f"Number of nodes: {G_with_python_weights.number_of_nodes()}")
print(f"Number of edges: {G_with_python_weights.number_of_edges()}")

# Visualization function
def draw_graph(graph, title):
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(12, 12))
    nx.draw(graph, pos, with_labels=True, node_size=50, font_size=8)
    plt.title(title)
    plt.show()

# Visualize the graphs
draw_graph(G, "Main Graph")
draw_graph(G_with_phd_weights, "Graph with Higher Weights for PhD Users")
draw_graph(G_with_java_weights, "Graph with Higher Weights for Java Users")
draw_graph(G_with_python_weights, "Graph with Higher Weights for Python Users")

