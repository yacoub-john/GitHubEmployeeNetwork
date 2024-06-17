import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Example feature vector (replace with your actual data)
# Assuming a matrix where rows and columns represent entities (users) and values represent scores
# Example matrix (replace with your actual data)
feature_matrix = np.array([
    [1.0, 0.8, 0.6, 0.3],
    [0.8, 1.0, 0.7, 0.4],
    [0.6, 0.7, 1.0, 0.5],
    [0.3, 0.4, 0.5, 1.0]
])
# Example feature vector (replace with your actual data)
features = ['Programming Languages', 'Education', 'Years of Experience', 'Company Affiliation']
scores = [8, 7, 6, 9]  # Example scores or weights for each feature

# Number of features
num_features = len(features)

# Create a radar chart
angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()

# Repeat the first feature to close the circle
scores += scores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, scores, color='skyblue', alpha=0.4)
ax.plot(angles, scores, color='skyblue', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(features, fontsize=10)
plt.title('Feature Vector Radar Chart')
plt.show()
# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(feature_matrix, annot=True, cmap='Blues', xticklabels=features, yticklabels=features)
plt.title('Feature Vector Heatmap')
plt.show()
