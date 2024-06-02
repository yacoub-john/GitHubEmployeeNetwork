import json
import csv
import time
import requests

from github import Github


def fetch_repo_details(owner, repo_name):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo_name}"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 403:
            print("Rate limit exceeded. Retrying in a moment...")
            time.sleep(60)
            return fetch_repo_details(owner, repo_name)
        elif response.status_code == 404:
            print(f"Repository {owner}/{repo_name} not found.")
            return None
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None
    except Exception as e:
        print(f"Error fetching repository details for {owner}/{repo_name}: {e}")
        return None


def fetch_repo_and_contributors(owner, repo_name):
    try:
        repo_details = fetch_repo_details(owner, repo_name)
        if repo_details:
            repo_id = repo_details['id']
            repo_owner = repo_details['owner']['login']
            contributors_url = repo_details['contributors_url']
            contributors_response = requests.get(contributors_url)
            if contributors_response.status_code == 200:
                contributors = contributors_response.json()
                return repo_id, repo_owner, contributors, repo_details['html_url']
            elif contributors_response.status_code == 204:
                print(f"No contributors found for repository {owner}/{repo_name}")
                return repo_id, repo_owner, [], repo_details['html_url']
            elif contributors_response.status_code == 403:
                print("Rate limit exceeded. Pausing for a while before retrying...")
                time.sleep(60)
                return fetch_repo_and_contributors(owner, repo_name)
            else:
                print(f"Error fetching contributors for repository {owner}/{repo_name}: {contributors_response.reason}")
                return None, None, [], None
        else:
            print(f"Repository {owner}/{repo_name} not found.")
            return None, None, [], None
    except Exception as e:
        print(f"Error fetching data for repository {owner}/{repo_name}: {e}")
        return None, None, [], None


def process_json(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        for line in file:
            user = json.loads(line.strip())
            if user.get('repo_list'):
                for repo_data in user['repo_list']:
                    full_name = repo_data.get('full_name')
                    if full_name:
                        repo_name = full_name.split('/')[-1]
                        repo_id, repo_owner, contributors, repo_url = fetch_repo_and_contributors(user['login'],
                                                                                                  repo_name)
                        if repo_id and repo_owner:
                            for contributor in contributors:
                                row = [repo_id, repo_owner, user['login'], contributor['login'],
                                       contributor['contributions'], contributor['html_url'], repo_name, repo_url]
                                save_to_csv([row], output_file)

    print(f"Data successfully written to {output_file}")


def save_to_csv(data, output_file):
    with open(output_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


#g = Github("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")

json_file = "filtered_data.json"  # Replace with your JSON file path
output_file = "contributors.csv"  # Replace with your desired output file name

process_json(json_file, output_file, chunk_size=100)
