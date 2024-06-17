import networkx as nx
import json
import random
import itertools

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
G = nx.read_graphml("developer_network_main.graphml")


# Create training and testing sets ensuring the test set is not empty
def split_edges(G, test_ratio=0.2):
    all_edges = list(G.edges())
    random.shuffle(all_edges)

    num_test_edges = int(len(all_edges) * test_ratio)
    test_edges = all_edges[:num_test_edges]
    train_edges = all_edges[num_test_edges:]

    return train_edges, test_edges


train_edges, test_edges = split_edges(G)

# Check if we have test edges
if len(test_edges) == 0:
    raise ValueError("Test set is empty. Adjust the edge splitting strategy.")

print(f"Test edges ({len(test_edges)}): {test_edges[:10]}...")

# Create training graph
G_train = nx.Graph()
G_train.add_nodes_from(G.nodes(data=True))
G_train.add_edges_from(train_edges)


# Function to apply prediction function to a chunk of edges
def apply_prediction_function_chunk(G, edges, prediction_function):
    if prediction_function == common_neighbors:
        return [(u, v, len(list(nx.common_neighbors(G, u, v)))) for u, v in edges]
    else:
        return list(prediction_function(G, edges))


# Apply link prediction algorithms on the training graph
def predict_links(G, train_edges, prediction_function, num_predictions, chunk_size=1000, sample_size=100000):
    # Remove training edges from the graph
    G_pred = nx.Graph(G)
    G_pred.remove_edges_from(train_edges)

    predictions = []

    # Function to chunk potential edges to avoid memory overload
    def chunk_generator(iterable, size):
        iterator = iter(iterable)
        for first in iterator:
            yield itertools.chain([first], itertools.islice(iterator, size - 1))

    # Randomly sample potential edges to limit the scope
    potential_edges = list(itertools.islice(nx.non_edges(G_pred), sample_size))
    total_chunks = (len(potential_edges) // chunk_size) + 1

    print(f"Total potential edges: {len(potential_edges)}")
    print(f"Processing in {total_chunks} chunks of size {chunk_size}...")

    # Process potential edges in chunks
    potential_edges_chunks = chunk_generator(potential_edges, chunk_size)
    for i, chunk in enumerate(potential_edges_chunks):
        chunk = list(chunk)
        predictions.extend(apply_prediction_function_chunk(G_pred, chunk, prediction_function))
        predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:num_predictions]
        print(f"Processed chunk {i + 1}/{total_chunks}")

    # Return the top predicted edges
    return [(u, v) for u, v, _ in predictions]  # Limit to the number of predictions


# Evaluate the predictions
def evaluate_predictions(predicted_edges, test_edges):
    predicted_set = set(predicted_edges)
    test_set = set(test_edges)

    true_positives = len(predicted_set & test_set)
    false_positives = len(predicted_set - test_set)
    false_negatives = len(test_set - predicted_set)

    print(f"True Positives: {true_positives}")
    print(f"False Positives: {false_positives}")
    print(f"False Negatives: {false_negatives}")

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
    "Common Neighbors": common_neighbors,
    "Jaccard Coefficient": jaccard_coefficient,
    "Adamic/Adar Index": adamic_adar_index,
    "Resource Allocation Index": resource_allocation_index
}

results = {}

print("Starting prediction for Common Neighbors...")
predicted_edges_cn = predict_links(G_train, train_edges, common_neighbors, num_predictions)
print(f"Top predicted edges (Common Neighbors): {predicted_edges_cn[:10]}...")
results["Common Neighbors"] = evaluate_predictions(predicted_edges_cn, test_edges)
print("Completed prediction for Common Neighbors.")

for method_name, prediction_function in methods.items():
    print(f"Starting prediction for {method_name}...")
    predicted_edges = predict_links(G_train, train_edges, prediction_function, num_predictions)
    print(f"Top predicted edges ({method_name}): {predicted_edges[:10]}...")
    results[method_name] = evaluate_predictions(predicted_edges, test_edges)
    print(f"Completed prediction for {method_name}.")

# Output the results
write_data_to_json("link_prediction_results.json", results)
print("Link prediction results written to link_prediction_results.json")
