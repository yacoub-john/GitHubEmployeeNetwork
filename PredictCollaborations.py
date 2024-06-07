import networkx as nx
import json
import random

from networkx import common_neighbors
from networkx.algorithms.link_prediction import (
    jaccard_coefficient,
    adamic_adar_index,
    resource_allocation_index
)

# Function to write results to a JSON file
def write_data_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Load the bipartite graph from the GraphML file
G = nx.read_graphml("bipartite_graph.graphml")

# Split the edges into training and testing sets
edges = list(G.edges())
random.shuffle(edges)
split_index = int(0.8 * len(edges))
train_edges = edges[:split_index]
test_edges = edges[split_index:]

# Create training graph
G_train = nx.Graph()
G_train.add_nodes_from(G.nodes(data=True))
G_train.add_edges_from(train_edges)

# Apply link prediction algorithms on the training graph
def predict_links(G, train_edges, prediction_function, num_predictions, chunk_size=100000):
    # Remove training edges from the graph
    G_pred = nx.Graph(G)
    G_pred.remove_edges_from(train_edges)

    predictions = []

    # Generate potential edges using a generator
    potential_edges = nx.non_edges(G_pred)

    # Process potential edges in chunks to avoid memory overload
    potential_edges_chunk = []
    for u, v in potential_edges:
        potential_edges_chunk.append((u, v))
        if len(potential_edges_chunk) >= chunk_size:
            predictions.extend(apply_prediction_function(G_pred, potential_edges_chunk, prediction_function))
            predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:num_predictions]
            potential_edges_chunk = []

    # Process remaining potential edges
    if potential_edges_chunk:
        predictions.extend(apply_prediction_function(G_pred, potential_edges_chunk, prediction_function))
        predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:num_predictions]

    # Return the top predicted edges
    return [(u, v) for u, v, _ in predictions]  # Limit to the number of predictions

def apply_prediction_function(G, edges, prediction_function):
    if prediction_function == common_neighbors:
        return [(u, v, len(list(nx.common_neighbors(G, u, v)))) for u, v in edges]
    else:
        return list(prediction_function(G, edges))

# Evaluate the predictions
def evaluate_predictions(predicted_edges, test_edges):
    predicted_set = set(predicted_edges)
    test_set = set(test_edges)

    true_positives = len(predicted_set & test_set)
    false_positives = len(predicted_set - test_set)
    false_negatives = len(test_set - predicted_set)

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }

# Number of predictions should equal the number of removed test edges
num_predictions = len(test_edges)

# Predict and evaluate using different link prediction methods
methods = {
    "Jaccard Coefficient": jaccard_coefficient,
    "Adamic/Adar Index": adamic_adar_index,
    "Resource Allocation Index": resource_allocation_index
}

results = {}

# Special case for common neighbors
predicted_edges_cn = predict_links(G_train, train_edges, common_neighbors, num_predictions)
results["Common Neighbors"] = evaluate_predictions(predicted_edges_cn, test_edges)

for method_name, prediction_function in methods.items():
    predicted_edges = predict_links(G_train, train_edges, prediction_function, num_predictions)
    results[method_name] = evaluate_predictions(predicted_edges, test_edges)

# Output the results
write_data_to_json("link_prediction_results.json", results)
print("Link prediction results written to link_prediction_results.json")
