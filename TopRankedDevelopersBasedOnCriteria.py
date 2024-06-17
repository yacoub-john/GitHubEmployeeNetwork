import pandas as pd
import networkx as nx
import re
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('developers.csv')

# Function to clean and convert yearly contributions to integers
def clean_contributions(value):
    if isinstance(value, str):
        value = re.sub(r'\D', '', value)  # Remove non-numeric characters
    try:
        return int(value)
    except ValueError:
        return 0  # Return 0 if conversion fails

# Apply the cleaning function to the 'yearly_contributions' column
df['yearly_contributions'] = df['yearly_contributions'].apply(clean_contributions)

# Function to calculate the feature vector score based on matching criteria
def calculate_score(bio, target_languages, target_education, experience, yearly_contributions):
    score = 0
    if pd.notna(bio):
        bio = bio.lower()
        # Calculate language similarity using cosine similarity
        lang_similarity = compute_similarity(bio, target_languages)
        score += lang_similarity
        # Calculate education similarity using cosine similarity
        edu_similarity = compute_similarity(bio, [target_education])
        score += edu_similarity
        # Normalize experience score
        normalized_experience = experience / df['yearly_contributions'].max()
        score += normalized_experience  # Add normalized experience
        # Include yearly contributions
        score += yearly_contributions * 0.01  # Adjust the scale if necessary
    return score

# Function to compute cosine similarity between two sets of words
def compute_similarity(bio, target_words):
    # Tokenize the bio and target words
    bio_tokens = set(re.findall(r'\w+', bio))
    target_tokens = set(target_words)
    # Compute cosine similarity
    bio_vector = [1 if word in bio_tokens else 0 for word in target_tokens]
    target_vector = [1] * len(target_tokens)
    similarity = cosine_similarity([bio_vector], [target_vector])[0][0]
    return similarity

# Create graph data structures using NetworkX
G = nx.Graph()

# Add nodes (developers) to the graph
for _, row in df.iterrows():
    username = row['username']
    bio = row['Bio']
    experience = row['yearly_contributions']  # Use yearly contributions as a proxy for experience
    G.add_node(username, bio=bio, company=row['Company'], location=row['Location'], experience=experience,
               yearly_contributions=row['yearly_contributions'])

# Function to set edge weights based on scores
def set_edge_weights(graph, target_languages, target_education):
    for _, row in df.iterrows():
        username = row['username']
        bio = row['Bio']
        experience = row['yearly_contributions']  # Use yearly contributions as a proxy for experience
        yearly_contributions = row['yearly_contributions']
        followers_names = row['collaborators_name'].strip("[]").replace("'", "").split(',')
        for follower_name in followers_names:
            follower_name = follower_name.strip()  # Clean up any extra spaces

            user_score = calculate_score(
                bio, target_languages, target_education, experience, yearly_contributions
            )
            follower_bio = graph.nodes.get(follower_name, {}).get('bio', '')
            follower_experience = graph.nodes.get(follower_name, {}).get('experience', 0)
            follower_contributions = graph.nodes.get(follower_name, {}).get('yearly_contributions', 0)

            follower_score = calculate_score(
                follower_bio, target_languages, target_education, follower_experience, follower_contributions
            )

            weight = (user_score + follower_score) / 2  # Average the scores for the edge weight

            graph.add_edge(follower_name, username, relation='collaborator', weight=weight)

# Function to generate a custom graph based on input criteria
def generate_custom_graph(target_languages, target_education):
    # Create a new graph
    custom_graph = nx.Graph()

    # Add nodes (developers) to the custom graph
    for _, row in df.iterrows():
        username = row['username']
        bio = row['Bio']
        experience = row['yearly_contributions']  # Use yearly contributions as a proxy for experience
        if pd.notna(bio):  # Check if bio is not NaN
            custom_graph.add_node(username, bio=bio, company=row['Company'], location=row['Location'],
                                  experience=experience, yearly_contributions=row['yearly_contributions'])
        else:
            custom_graph.add_node(username, company=row['Company'], location=row['Location'], experience=experience,
                                  yearly_contributions=row['yearly_contributions'])

    # Set edge weights based on scores
    set_edge_weights(custom_graph, target_languages, target_education)

    return custom_graph

# Example usage
target_languages = ['Java']
target_education = 'PhD'

custom_graph = generate_custom_graph(target_languages, target_education)

# Print nodes and edges for the custom graph
print("\nCustom Graph:")
print(f"Number of nodes: {custom_graph.number_of_nodes()}")
print(f"Number of edges: {custom_graph.number_of_edges()}")

# Weighted PageRank for the graph with higher weights for Python users
pr_with_scored_weights = nx.pagerank(custom_graph, weight='weight')

# Get top 50 nodes from each graph based on PageRank scores
top_50_main = sorted(pr_with_scored_weights.items(), key=lambda x: x[1], reverse=True)[:50]

# Save top 50 nodes and their PageRank scores to files
with open('top_50_criteria_graph.txt', 'w') as f:
    f.write("Top 50 nodes in main graph:\n")
    for node, score in top_50_main:
        f.write(f"{node}: {score}\n")
