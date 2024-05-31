import json
import networkx as nx
import jsonlines


def filter_and_save(input_file, output_file):
    """
    Filter users based on the number of repositories and save the filtered data to a new file.
    Criteria:
    - 'repo_list' is a list
    - Length of 'repo_list' is at least 3
    """
    with open(input_file, encoding='utf-8') as f:
        with jsonlines.open(output_file, mode='w') as out_f:
            for line in f:
                user_data = json.loads(line)
                if isinstance(user_data.get("repo_list"), list) and len(user_data["repo_list"]) >= 3:
                    out_f.write(user_data)


# Filter and save data to a new file
filter_and_save('data.json', 'filtered_data.json')

# Create a NetworkX graph
G = nx.Graph()

# Dictionaries to track users by company, programming languages, and to map user IDs to names
company_dict = {}
language_dict = {}
user_names = {}

# Process filtered JSON file and construct the graph
with jsonlines.open('filtered_data.json', mode='r') as reader:
    for user_data in reader:
        user_id = user_data["id"]
        user_name = user_data.get("name")

        # Only add user if name is known
        if user_name and user_name != "unknown":
            # Add user to the names dictionary
            user_names[user_id] = user_name

            # Add user node to the graph
            G.add_node(user_id, name=user_name)

            # Add users to company dictionary
            company = user_data.get("company")
            if company:
                if company not in company_dict:
                    company_dict[company] = []
                company_dict[company].append(user_id)

            # Extract languages from repo_list and add users to language dictionary
            for repo in user_data.get("repo_list", []):
                language = repo.get("language")
                if language:
                    if language not in language_dict:
                        language_dict[language] = []
                    language_dict[language].append(user_id)

            # # Add follower and following edges
            # for follower_id in user_data.get("follower_list", []):
            #     if follower_id in user_names:
            #         G.add_edge(user_id, follower_id)
            #
            # for following_id in user_data.get("following_list", []):
            #     if following_id in user_names:
            #         G.add_edge(user_id, following_id)

# Add edges for users working in the same company
for company, users in company_dict.items():
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            if users[i] in user_names and users[j] in user_names:
                G.add_edge(users[i], users[j])

# Add edges for users using the same programming languages
for language, users in language_dict.items():
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            if users[i] in user_names and users[j] in user_names:
                G.add_edge(users[i], users[j])

# Export the network as a GraphML file
nx.write_graphml(G, "network.graphml")
print("Network exported as network.graphml")
