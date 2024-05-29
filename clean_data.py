import json
import networkx as nx
import jsonlines


# Function to filter users based on criteria and save to a new file
def filter_and_save(input_file, output_file):
    with open(input_file, encoding='utf-8') as f:
        with jsonlines.open(output_file, mode='w') as out_f:
            for line in f:
                user_data = json.loads(line)
                if (isinstance(user_data.get("repo_list"), list) and
                        len(user_data.get("repo_list", [])) >= 3 and
                        user_data.get("followers", 0) >= 3 and
                        user_data.get("following", 0) >= 3):
                    out_f.write(user_data)


# Filter and save data to a new file
filter_and_save('data.json', 'filtered_data.json')

# Create a NetworkX graph
G = nx.Graph()

# Process JSON file line by line in chunks
with jsonlines.open('filtered_data.json', mode='r') as reader:
    for user_data in reader:
        # Add nodes to the graph
        user_id = user_data["id"]
        G.add_node(user_id)

        # Add edges (follower/following links)
        for follower_id in user_data.get("follower_list", []):
            if not G.has_node(follower_id):
                G.add_node(follower_id)
            if not G.has_edge(user_id, follower_id):
                G.add_edge(user_id, follower_id)
        for following_id in user_data.get("following_list", []):
            if not G.has_node(following_id):
                G.add_node(following_id)
            if not G.has_edge(user_id, following_id):
                G.add_edge(user_id, following_id)

# Export the network as a GraphML file
nx.write_graphml(G, "network.graphml")
print("Network exported as network.graphml")
