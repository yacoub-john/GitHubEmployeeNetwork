import pandas as pd

# Update file paths based on your actual file names
login_data = pd.read_csv("languages_projects_created_at.csv")
user_info = pd.read_csv("developers.csv")

# Merge on login (languages_projects_created_at) and username (developers)
merged_df = login_data.merge(user_info[['username', 'Followers', 'Following', 'starredRepoCount', 'yearly_contributions', 'followers_name', 'following_names']], left_on='login', right_on='username', how='inner')

print("Merged data created successfully!")

# You can save the merged data to a new CSV file if desired
merged_df.to_csv("merged_data.csv", index=False)
print("Merged data saved to merged_data.csv")
