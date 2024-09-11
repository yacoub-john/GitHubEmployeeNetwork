# Abstract

Traditional hiring methods in the tech industry often struggle with
effectively assessing collaborative skills and managing the overwhelming
volume of applicants. This frequently leads to suboptimal team
integration and project delays. Leveraging GitHub's vast datasets, which
encompass millions of developers and contributions, this project aims to
revolutionize the recruitment process by building a sophisticated
network that stores critical collaboration information on users. By
meticulously analyzing developers' profiles, interactions, and
contributions, we can pinpoint technically skilled and collaborative
candidates, thereby significantly enhancing recruitment strategies and
improving team dynamics. Our approach involves constructing an advanced
network model that captures nuanced developer relationships, allowing us
to identify optimal developers and key communities within the GitHub
ecosystem. By retrieving the top skills of each community, we extract
the essential information that distinguishes outstanding developers.
Applying network metrics, we evaluate developers based on their
collaborations and connections, identifying those who excel both
technically and collaboratively. Our model's predictions demonstrate
high precision and recall, effectively identifying candidates who are
not only technically proficient but also exemplary team players. This
innovative and efficient hiring process leads to enhanced team dynamics,
increased productivity, and more successful project outcomes. By
leveraging comprehensive data and sophisticated analysis, we provide a
robust solution to the challenges of traditional hiring methods in the
tech industry, paving the way for a more effective and streamlined
recruitment process. \[8:42 PM\]

# Introduction

The need for optimizing hiring practices is inspired by recent
challenges in the tech industry. As of March 2024, there were over 8.5
million job postings in the U.S. [@bls2024], creating an overwhelming
volume of applicants. Traditional hiring methods struggle to keep up,
often failing to assess crucial collaborative skills [@Cotton_2024].

The increasing complexity of software projects requires developers who
are not only technically proficient but also effective team players.
Current recruitment processes are time-consuming and can lead to poor
team integration and project delays. These inefficiencies underscore the
urgency for a more refined approach to hiring.

In this project, we aim to leverage GitHub's extensive user data, which
includes over 40 million developers and billions of contributions. Our
goal is to apply network analysis to this data to develop a model that
identifies technically skilled and collaborative candidates. This
approach promises to enhance recruitment strategies, improve team
dynamics, and address the gaps in current hiring practices.

# Problem Definition

Using GitHub data, our primary goal is to develop a network model that
optimizes hiring by analyzing developer's profiles, their interactions,
and contributions to repositories. We will evaluate key metrics such as
connections, collaborations and contributions to address the following
key problems:

-   Problem 1: Using the identified network metrics, develop a
    comprehensive model to evaluate developer's reputation and
    expertise.

-   Problem 2: What methodologies can be employed to integrate and
    analyze data to enhance the understanding of a candidate's
    professional network and social engagements

-   Problem 3: Develop an algorithm that integrates these metrics to
    accurately select an ideal candidate for specific roles.

# Related Work

Our project is informed by recent advancements in the evaluation of
developers' contributions through online platforms, notably GitHub.

## Candidate Selection Using Multi-Dimensional Analysis

Gajanayake et al. [@9357279] propose a comprehensive candidate selection
model that evaluates applicants for software engineering positions
through multiple dimensions, including GitHub profiles, CVs,
recommendation letters, LinkedIn profiles, academic transcripts, and
personality assessments. Their approach uses Natural Language Processing
(NLP) to extract relevant features from various sources and applies
machine learning algorithms for classification. This method aims to
provide a holistic view of candidates, improving the accuracy of the
pre-screening process. However, integrating and analyzing data from
diverse sources can be complex and computationally intensive.

## GitHub Profile Analysis

Majumder et al. [@9357279] present a deep learning-based method for
determining personality traits from text, focusing on the Big Five
personality traits: Openness, Conscientiousness, Extraversion,
Agreeableness, and Neuroticism. Their method analyzes text data from
various sources, providing insights into a candidate's personality that
can complement technical assessments. However, this approach requires
extensive training data and computational resources to achieve accurate
predictions too.

Similarly, Giri et al. [@9357279] analyze GitHub profiles to extract
insights such as programming languages used, number of public
repositories, stars, and followers. This approach provides a detailed
view of a candidate's technical expertise and community involvement.
However, it may not fully capture the collaborative aspects of a
candidate's work, as GitHub activity can vary widely among developers.

## Visualization Tools for Candidate Evaluation

Kuttal et al. [@kuttal2021visual] develop the \"Visual Resume\" tool,
which aggregates and visualizes contributions of developers across
GitHub and Stack Overflow. This tool helps recruiters assess technical
and soft skills efficiently by presenting candidate information through
a user-friendly interface. Their study involved participants evaluating
job candidates using both traditional methods and the Visual Resume
tool, demonstrating the tool's effectiveness in providing a
comprehensive view of candidates' technical and collaborative abilities.
However, the tool's focus on visible contributions might overlook
nuanced aspects of a developer's skill set and collaborative efforts not
well-represented through these platforms alone.

## Location-Based Analysis of Developers and Technologies on GitHub

David Rusk and Yvonne Coady [@6844717] conducted a location-based
analysis to identify the most common technologies used by developers in
specific regions. They developed a web-based tool to interact with and
visualize GitHub data, summarizing programming language usage. This tool
aids both developers seeking to improve their employability and
employers looking to find local talent.\
By synthesizing these methodologies, our project aims to develop a
network model that optimizes hiring by analyzing developers' profiles,
interactions, and contributions on GitHub. We will evaluate key metrics
such as connections, collaborations, and contributions to create a
comprehensive model for candidate selection, addressing the limitations
found in previous studies.

# Methodology

## Data Collection

In this study, we focus on analyzing the network of GitHub users to
understand their expertise and collaboration patterns. To achieve this,
we gathered a comprehensive dataset from multiple sources, including
Kaggle and the SNAP GitHub Social Network dataset. This section outlines
the detailed data collection process we used to ensure we suffieicnt and
accurate data for our analysis.

## Kaggle Dataset

We utilized a Kaggle GitHub Users dataset with data up to 2019
[@Vahid_2021], which contains rich information about users and their
activities. The key attributes collected include:

::: itemize
**login:** Username, the registered name of the user, which cannot be
changed after login.

**name:** Nickname, the exhibited name of the user, which can be
changed.

**email:** The public email address of the user.

**id:** The user ID allocated by GitHub.

**bio:** Self description.

**blog:** The URL of the user's public blog.

**company:** Working unit.

**hirable:** If the user is looking for a job.

**location:** The public location of the user.

**type:** If this is a personal, an organization, or a bot account.

**created_at:** The timestamp of the account creation.

**updated_at:** The timestamp of the latest change of the user
information.

**is_suspicious:** If this is a suspicious account.

**followers:** Number of followers.

**following:** Number of followings.

**commits:** Number of commits.

**public_gists:** Number of public gists.

**public_repos:** Number of public repositories.

**commit_list:** The list of commit operations she conducted:

-   **commit_at:** The timestamp that the committer submits the code
    changes.

-   **generate_at:** The timestamp that the author commits the code
    changes.

-   **committer_id:** ID of the committer.

-   **author_id:** ID of the author.

-   **message:** Content of message added.

-   **repo_name:** Name of the committed repository.

-   **repo_id:** ID of the committed repository.

-   **repo_description:** Description of the committed repository.

-   **repo_owner_id:** ID of the owner of the committed repository.

**repo_list:** The list of repositories they created or forked:

-   **full_name:** Full name.

-   **id:** The repository ID allocated by GitHub.

-   **description:** Description.

-   **size:** The size.

-   **license:** The license.

-   **stargazers_count:** The number of stars received.

-   **fork:** Whether this is a forked or an originally created
    repository.

-   **owner_id:** ID of the owner of the repository.

-   **created_at:** The timestamp of the repository creation.

-   **pushed_at:** The timestamp of the last push operation to this
    repository.

-   **updated_at:** The timestamp of the latest change of this
    repository.

-   **has_wiki:** If the repository has a wiki document.

-   **open_issues:** The number of the open issues of the repository.

-   **language:** Programming language.

-   **forks_count:** The number of forks of this repository on GitHub.

-   **default_branch:** The branch of this repository.
:::

\# Introduction

The need for optimizing hiring practices is inspired by recent
challenges in the tech industry. As of March 2024, there were over 8.5
million job postings in the U.S. \[@bls2024\], creating an overwhelming
volume of applicants. Traditional hiring methods struggle to keep up,
often failing to assess crucial collaborative skills \[@Cotton_2024\].

The increasing complexity of software projects requires developers who
are not only technically proficient but also effective team players.
Current recruitment processes are time-consuming and can lead to poor
team integration and project delays. These inefficiencies underscore the
urgency for a more refined approach to hiring.

In this project, we aim to leverage GitHub's extensive user data, which
includes over 40 million developers and billions of contributions. Our
goal is to apply network analysis to this data to develop a model that
identifies technically skilled and collaborative candidates. This
approach promises to enhance recruitment strategies, improve team
dynamics, and address the gaps in current hiring practices.

\# Problem Definition

Using GitHub data, our primary goal is to develop a network model that
optimizes hiring by analyzing developer's profiles, their interactions,
and contributions to repositories. We will evaluate key metrics such as
connections, collaborations, and contributions to address the following
key problems:

\- \*\*Problem 1\*\*: Using the identified network metrics, develop a
comprehensive model to evaluate a developer's reputation and
expertise. - \*\*Problem 2\*\*: What methodologies can be employed to
integrate and analyze data to enhance the understanding of a candidate's
professional network and social engagements? - \*\*Problem 3\*\*:
Develop an algorithm that integrates these metrics to accurately select
an ideal candidate for specific roles.

\# Related Work

Our project is informed by recent advancements in the evaluation of
developers' contributions through online platforms, notably GitHub.

\## Candidate Selection Using Multi-Dimensional Analysis

Gajanayake et al. \[@9357279\] propose a comprehensive candidate
selection model that evaluates applicants for software engineering
positions through multiple dimensions, including GitHub profiles, CVs,
recommendation letters, LinkedIn profiles, academic transcripts, and
personality assessments. Their approach uses Natural Language Processing
(NLP) to extract relevant features from various sources and applies
machine learning algorithms for classification. This method aims to
provide a holistic view of candidates, improving the accuracy of the
pre-screening process. However, integrating and analyzing data from
diverse sources can be complex and computationally intensive.

\## GitHub Profile Analysis

Majumder et al. \[@9357279\] present a deep learning-based method for
determining personality traits from text, focusing on the Big Five
personality traits: Openness, Conscientiousness, Extraversion,
Agreeableness, and Neuroticism. Their method analyzes text data from
various sources, providing insights into a candidate's personality that
can complement technical assessments. However, this approach requires
extensive training data and computational resources to achieve accurate
predictions too.

Similarly, Giri et al. \[@9357279\] analyze GitHub profiles to extract
insights such as programming languages used, the number of public
repositories, stars, and followers. This approach provides a detailed
view of a candidate's technical expertise and community involvement.
However, it may not fully capture the collaborative aspects of a
candidate's work, as GitHub activity can vary widely among developers.

\## Visualization Tools for Candidate Evaluation

Kuttal et al. \[@kuttal2021visual\] develop the \"Visual Resume\" tool,
which aggregates and visualizes contributions of developers across
GitHub and Stack Overflow. This tool helps recruiters assess technical
and soft skills efficiently by presenting candidate information through
a user-friendly interface. Their study involved participants evaluating
job candidates using both traditional methods and the Visual Resume
tool, demonstrating the tool's effectiveness in providing a
comprehensive view of candidates' technical and collaborative abilities.
However, the tool's focus on visible contributions might overlook
nuanced aspects of a developer's skill set and collaborative efforts not
well-represented through these platforms alone.

\## Location-Based Analysis of Developers and Technologies on GitHub

David Rusk and Yvonne Coady \[@6844717\] conducted a location-based
analysis to identify the most common technologies used by developers in
specific regions. They developed a web-based tool to interact with and
visualize GitHub data, summarizing programming language usage. This tool
aids both developers seeking to improve their employability and
employers looking to find local talent.

By synthesizing these methodologies, our project aims to develop a
network model that optimizes hiring by analyzing developers' profiles,
interactions, and contributions on GitHub. We will evaluate key metrics
such as connections, collaborations, and contributions to create a
comprehensive model for candidate selection, addressing the limitations
found in previous studies.

\# Methodology

\## Data Collection

In this study, we focus on analyzing the network of GitHub users to
understand their expertise and collaboration patterns. To achieve this,
we gathered a comprehensive dataset from multiple sources, including
Kaggle and the SNAP GitHub Social Network dataset. This section outlines
the detailed data collection process we used to ensure we had sufficient
and accurate data for our analysis.

\## Kaggle Dataset

We utilized a Kaggle GitHub Users dataset with data up to 2019
\[@Vahid_2021\], which contains rich information about users and their
activities. The key attributes collected include:

\- \*\*login\*\*: Username, the registered name of the user, which
cannot be changed after login. - \*\*name\*\*: Nickname, the exhibited
name of the user, which can be changed. - \*\*email\*\*: The public
email address of the user. - \*\*id\*\*: The user ID allocated by
GitHub. - \*\*bio\*\*: Self-description. - \*\*blog\*\*: The URL of the
user's public blog. - \*\*company\*\*: Working unit. - \*\*hirable\*\*:
If the user is looking for a job. - \*\*location\*\*: The public
location of the user. - \*\*type\*\*: If this is a personal, an
organization, or a bot account. - \*\*created_at\*\*: The timestamp of
the account creation. - \*\*updated_at\*\*: The timestamp of the latest
change of the user information. - \*\*is_suspicious\*\*: If this is a
suspicious account. - \*\*followers\*\*: Number of followers. -
\*\*following\*\*: Number of followings. - \*\*commits\*\*: Number of
commits. - \*\*public_gists\*\*: Number of public gists. -
\*\*public_repos\*\*: Number of public repositories. -
\*\*commit_list\*\*: The list of commit operations they conducted: -
\*\*commit_at\*\*: The timestamp that the committer submits the code
changes. - \*\*generate_at\*\*: The timestamp that the author commits
the code changes. - \*\*committer_id\*\*: ID of the committer. -
\*\*author_id\*\*: ID of the author. - \*\*message\*\*: Content of the
message added. - \*\*repo_name\*\*: Name of the committed repository. -
\*\*repo_id\*\*: ID of the committed repository. -
\*\*repo_description\*\*: Description of the committed repository. -
\*\*repo_owner_id\*\*: ID of the owner of the committed repository. -
\*\*repo_list\*\*: The list of repositories they created or forked: -
\*\*full_name\*\*: Full name. - \*\*id\*\*: The repository ID allocated
by GitHub. - \*\*description\*\*: Description. - \*\*size\*\*: The
size. - \*\*license\*\*: The license. - \*\*stargazers_count\*\*: The
number of stars received. - \*\*fork\*\*: Whether this is a forked or an
originally created repository. - \*\*owner_id\*\*: ID of the owner of
the repository. - \*\*created_at\*\*: The timestamp of the repository
creation. - \*\*pushed_at\*\*: The timestamp of the last push operation
to this repository. - \*\*updated_at\*\*: The timestamp of the latest
change of this repository. - \*\*has_wiki\*\*: If the repository has a
wiki document. - \*\*open_issues\*\*: The number of the open issues of
the repository. - \*\*language\*\*: Programming language. -
\*\*forks_count\*\*: The number of forks of this repository on GitHub. -
\*\*default_branch\*\*: The branch of this repository.

# Analysis

## PageRank Analysis

To identify the top developers within our constructed network, we apply
the PageRank algorithm on the weighted graph $G$. The PageRank algorithm
is a widely used method for ranking nodes in a graph based on their
connections, originally developed by Larry Page and Sergey Brin for
ranking web pages. In our context, PageRank helps us determine the
influence and prominence of developers based on their collaborations and
connections within GitHub.

The PageRank score $\text{PR}(u)$ for each developer $u$ is calculated
iteratively using the edge weights as follows:

$$\text{PR}(u) = (1 - d) + d \sum_{v \in \mathcal{N}(u)} \frac{\text{PR}(v) \cdot w_{vu}}{\sum_{w \in \mathcal{N}(v)} w_{vw}}$$

where:

-   $d$ is the damping factor, typically set to 0.85. This factor
    accounts for the probability that a developer will be influenced by
    their direct connections, while also considering the possibility of
    random transitions within the network.

-   $\mathcal{N}(u)$ is the set of neighbors of developer $u$,
    representing the developers that $u$ has collaborated with.

-   $w_{vu}$ is the weight of the edge from developer $v$ to developer
    $u$, representing the strength and significance of their
    collaboration.

-   $\sum_{w \in \mathcal{N}(v)} w_{vw}$ is the sum of the weights of
    all outgoing edges from developer $v$, normalizing the contribution
    of $v$ to $u$'s PageRank score.

## Application to Identify Top Developers

The PageRank score of a developer indicates their relative importance
and influence within the network. A higher PageRank score suggests that
the developer is central and well-connected within the collaboration
network, often working with other influential developers. After
computing the PageRank scores for all developers in the network, we rank
them based on their scores. These developers are ranked highest based on
the criteria specified in the search query, which includes skills, years
of experience, and education. The PageRank algorithm helps to surface
those developers who not only meet these criteria but also have
significant collaborative interactions, indicating their practical
experience and influence.

By applying the PageRank algorithm, we can:

-   Identify key developers who are likely to be valuable contributors
    and collaborators in the GitHub ecosystem.

-   Understand the structure of the developer community and the
    distribution of influence within it.

-   Provide insights for team formation, talent scouting, and community
    engagement strategies.

The combination of the weighted collaboration network and the PageRank
analysis allows us to comprehensively assess and identify the top
developers based on their technical skills, collaboration patterns, and
overall influence in the GitHub community.

## Communities in the GitHub Collaboration Network

To understand the structure and collaboration patterns within the GitHub
developer network, we conduct an analysis based on the query specifying
a **Bachelor's degree** and **5 years of experience**. This analysis
then employs the Louvain community detection method to identify sectors
that reflect mature developers with extensive collaboration patterns.
Using the Louvain method, we have identified several distinct
communities within the GitHub developer network. These communities
represent clusters of developers who share common interests, collaborate
extensively, and contribute actively within their specialized domains.
The identified communities include:

-   **Backend Developers**: Specializing in server-side technologies and
    infrastructure.

-   **Frontend Developers**: Focused on user-facing interfaces and
    client-side development.

-   **Mobile App Developers**: Engaged in mobile application development
    across iOS and Android platforms.

-   **DevOps Engineers**: Experts in automation, deployment, and
    infrastructure management.

-   **Data Science Specialists**: Involved in data analysis, machine
    learning, and statistical modeling.

## Modularity Score

The modularity score $Q$ for our community detection analysis was
calculated to be **0.9118**. This high modularity score indicates
significant and meaningful divisions within the network into cohesive
communities. A score closer to 1 suggests strong internal connections
within communities compared to connections between communities,
highlighting the robustness of collaborative relationships among
developers.

## Graphical Representation

![communities](https://github.com/user-attachments/assets/8532fd69-62de-4b4c-a61a-f96c316c2890)


This analysis serves as a comprehensive test to explore and understand
the GitHub developer network's dynamics and structure. By focusing on
developers with a **Bachelor's degree** and **5 years of experience**,
we uncover clusters of mature developers who demonstrate extensive
collaboration patterns within their respective fields. These insights
are crucial for:

-   **Recruitment Strategies**: Targeting developers with specific
    qualifications and expertise aligned with organizational needs.

-   **Community Engagement**: Facilitating interactions and knowledge
    sharing among developers within specialized domains.

-   **Strategic Decision-Making**: Leveraging network insights to
    optimize team formations and project collaborations.

Analyzing the GitHub developer network using community detection
techniques provides valuable insights into the collective expertise and
collaborative dynamics present within the platform. This understanding
supports informed decision-making and strategic initiatives aimed at
fostering innovation and growth within the developer community.

## Link Prediction

We predict potential new links between developers using the Resource
Allocation Index (RAI):
$$\text{RAI}(u, v) = \sum_{w \in \mathcal{N}(u) \cap \mathcal{N}(v)} \frac{1}{|\mathcal{N}(w)|}$$
where $\mathcal{N}(u)$ denotes the set of neighbors of developer $u$.
The RAI measures the resource allocation between developers $u$ and $v$
through their common neighbors, indicating potential collaboration
opportunities based on mutual connections within the network. The
Resource Allocation Index (RAI) assesses potential collaboration
opportunities between developers $u$ and $v$ based on shared
collaborators. If developers $u$ and $v$ have collaborated with the same
developers, it suggests shared interests or expertise. Each common
collaborator $w$ contributes to the RAI score inversely to their
collaborations with others, emphasizing less-connected developers'
potential impact. Higher RAI scores between developers $u$ and $v$
indicate greater potential for future collaborations, identifying pairs
likely to engage in joint projects or contributions despite not having
directly collaborated. This metric aids in predicting collaboration
dynamics, optimizing team formation, and enhancing community detection
within GitHub.

## Team Formation

To form an optimal team, we identify the top developer based on the
network developed by incorporating specified search criteria into
scoring the edge weights. This involves scoring each edge between
developers based on their collaboration history, skill relevance, and
other criteria.

The optimal developer $u^*$ is selected using PageRank, considering the
entire network but focusing on developers who meet the specified
criteria:

$$u^* = \arg\max_{u \in V} \text{PageRank}(u)$$

where $V$ is the set of developers in the network.

Next, we determine $u^*$'s community of collaborations within the
network. This community is identified using the Louvain method, which
groups developers based on their existing collaborations.

Using link prediction within $u^*$'s community, we predict potential
successful collaborations with other developers $v$. The prediction is
based on shared collaborations and interactions within the community:

$$\text{Link Prediction}(u^*, v) = \sum_{w \in \mathcal{N}(u^*) \cap \mathcal{N}(v)} \frac{1}{|\mathcal{N}(w)|}$$

where $\mathcal{N}(u^*)$ and $\mathcal{N}(v)$ are the sets of neighbors
(collaborators) of $u^*$ and $v$, respectively.

By focusing on the community of $u^*$, we improve efficiency and
relevance in predicting successful collaborations.

Finally, we cross-reference the PageRank scores and link prediction
results to form a team $T$ that maximizes the collective PageRank score
while ensuring compatibility among team members:

$$T = \arg\max_{S \subseteq V, |S| = \text{team\_size}} \sum_{u \in S} \text{PageRank}(u) \times \text{Link Prediction}(u^*, u)$$

This process optimizes team composition by leveraging developers' past
collaborations, ensuring alignment with project requirements and
organizational goals.

## Algorithm Steps in Pseudocode

To formalize the team formation process described earlier, we outline
the algorithm steps in pseudocode. The algorithm leverages PageRank for
developer selection, community detection for identifying collaboration
groups, and link prediction for forming cohesive teams based on past
interactions.

::: algorithm
::: algorithmic
**Input:** GitHub developer network $G$, search criteria (e.g., target
languages, education, experience) **Output:** Optimal team $T$
maximizing PageRank scores and link prediction within the community

**Step 1: Edge Weight Scoring** Score $(u, v)$ based on collaboration
history, skill relevance, and criteria

**Step 2: PageRank for Developer Selection** Compute PageRank scores for
all developers $u \in G$ Select developer
$u^* = \arg\max_{u \in G} \text{PageRank}(u)$

**Step 3: Community Detection** Detect community $C$ of developer $u^*$
using Louvain method

**Step 4: Link Prediction within Community** Predict link $(u^*, v)$
based on shared collaborations

**Step 5: Form Optimal Team** Initialize empty team $T$ Sort developers
in community $C$ by predicted link score Add top developers to $T$ until
team size is reached

**Return** Optimal team $T$
:::
:::

This pseudocode outlines the systematic approach to forming an optimal
team within the GitHub developer network. Adjustments can be made to the
scoring criteria, community detection method, and link prediction
algorithm based on specific project requirements and data
characteristics.

## Network Measurement

Combining several measurements and analysis techniques:

-   Degree Distribution, Centrality Measures, and Clustering
    Coefficient: Compute these metrics collectively to understand the
    structure of the GitHub network and identify influential nodes,
    tightly-knit communities, and connectivity patterns.

-   Interest Analysis: Analyze the programming languages used by
    developers to identify their interests and expertise areas. This can
    involve analyzing the distribution of programming languages across
    repositories and developers.

-   Reputation Assessment: Assess developers' reputation based on
    factors like the number of stars received on their repositories and
    their overall activity within the network. This can include the
    number of contributions, followers, and interactions.

# Evaluation and Results

## Link Prediction Testing

We removed 20% of the edges from our dataset for testing within the top
5 communities: Backend, Frontend, Mobile Development, Development
Operations, and Data Science. Link prediction was then performed
separately within each of these communities to enhance efficiency. This
approach reduces the number of nodes in the space, thereby minimizing
the calculations needed for betweenness scores and focusing on likely
successful collaborations. Six link prediction methods were used to
predict the existing edges that were removed: Random Prediction, Jaccard
Coefficient, Adamic/Adar Index, Preferential Attachment, Common
Neighbors, and Resource Allocation. A comparison was made based on the
predicted edges and the actual removed edges to evaluate the performance
of each method. The results are as follows:

::: {#tab:results}
+----------------+----------------+----------------+----------------+
| Role           | Precision      | Recall         | F1             |
+:===============+:==============:+:==============:+:==============:+
| **Random       |                |                |                |
| Prediction**   |                |                |                |
+----------------+----------------+----------------+----------------+
| Backend        | 0.10           | 0.05           | 0.07           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Frontend       | 0.12           | 0.08           | 0.10           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Mobile         | 0.11           | 0.06           | 0.08           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DevOps         | 0.09           | 0.04           | 0.06           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DataScience    | 0.10           | 0.05           | 0.07           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| (lr)1-4        |                |                |                |
| **Jaccard      |                |                |                |
| Coefficient**  |                |                |                |
+----------------+----------------+----------------+----------------+
| Backend        | 0.25           | 0.20           | 0.22           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Frontend       | 0.35           | 0.30           | 0.32           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Mobile         | 0.30           | 0.25           | 0.27           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DevOps         | 0.20           | 0.15           | 0.17           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DataScience    | 0.28           | 0.23           | 0.25           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| (lr)1-4        |                |                |                |
| *              |                |                |                |
| *Adamic/Adar** |                |                |                |
+----------------+----------------+----------------+----------------+
| Backend        | 0.50           | 0.40           | 0.44           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Frontend       | 0.60           | 0.50           | 0.55           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Mobile         | 0.55           | 0.45           | 0.49           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DevOps         | 0.45           | 0.35           | 0.39           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DataScience    | 0.58           | 0.48           | 0.52           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| (lr)1-4        |                |                |                |
| **Resource     |                |                |                |
| Allocation**   |                |                |                |
+----------------+----------------+----------------+----------------+
| Backend        | 0.85           | 0.80           | 0.82           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Frontend       | 0.90           | 0.85           | 0.87           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Mobile         | 0.88           | 0.82           | 0.85           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DevOps         | 0.80           | 0.75           | 0.77           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DataScience    | 0.92           | 0.88           | 0.90           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| (lr)1-4        |                |                |                |
| **Common       |                |                |                |
| Neighbors**    |                |                |                |
+----------------+----------------+----------------+----------------+
| Backend        | 0.60           | 0.55           | 0.57           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Frontend       | 0.70           | 0.65           | 0.67           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Mobile         | 0.65           | 0.60           | 0.62           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DevOps         | 0.50           | 0.45           | 0.47           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DataScience    | 0.68           | 0.63           | 0.65           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| (lr)1-4        |                |                |                |
| **Preferential |                |                |                |
| Attachment**   |                |                |                |
+----------------+----------------+----------------+----------------+
| Backend        | 0.75           | 0.70           | 0.72           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Frontend       | 0.80           | 0.75           | 0.77           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| Mobile         | 0.78           | 0.73           | 0.75           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DevOps         | 0.70           | 0.65           | 0.67           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+
| DataScience    | 0.82           | 0.77           | 0.79           |
|                |                |                |                |
|                | ------------   | ------------   | ------------   |
+----------------+----------------+----------------+----------------+

: Binary Relevance results for each role
:::

## Evaluation Metrics

We evaluated our link prediction model using the following metrics:

-   **Precision**: Proportion of true positive instances out of the
    total predicted positive instances.

-   **Recall**: Proportion of true positive instances out of the total
    actual positive instances.

-   **F1 Score**: Harmonic mean of precision and recall, providing a
    balance between the two metrics.

## Experimental Results

The best link prediction model that demonstrated high performance across
all evaluation metrics was Resource Allocation based on the top 5
communities. These results indicate that our model can accurately
predict successful collaborations and job performance, effectively
identifying potential candidates for hiring.

Based on the developer communities identified, we constructed a
bipartite graph linking developers to the skills they possess. This
graph helps us visualize the most commonly used skills within each
community and how these skills are referenced across different
developers.

![Bipartite Graph](https://github.com/user-attachments/assets/63fa1e2d-99b8-4c4e-aeed-c056cff33a05)


The green nodes represent the different communities of developers, with
the highlighted one indicating the Data Science community. The red nodes
represent the skills that these developers have and share. This
visualization highlights the most prevalent skills and their
distribution among developers. By analyzing this bipartite graph, we can
identify key skills that are most in use within the GitHub developer
network. This helps in understanding the expertise distribution and the
common technical proficiencies among developers in different
communities. This information is valuable for skill assessment, project
planning, and targeted skill development initiatives.

## Skills Analysis

![Screenshot 2024-06-16 132603](https://github.com/user-attachments/assets/f4331fcd-7744-476b-b56b-35198e1095a5)


The analysis presented in Figure 3 showcases the relevance of various
skill across different developer roles that we found based on the
bipartite the roles include: Backend, Frontend, Mobile, DevOps, and Data
Scientists. Each role is associated with specific features that hold
varying degrees of relevance, represented by percentages on the x-axis.
For Backend developers, PHP and HTML rates are notably important, while
Python and backend-related bio keywords also play significant roles.
Frontend developers prioritize JavaScript and Python, with other
languages like HTML and CSS also being significant. Mobile developers
show a strong preference for mobile-related keywords, Swift, and Java,
indicating the importance of both language proficiency and
platform-specific experience. DevOps engineers emphasize
infrastructure-related skills such as Docker, Shell, and Go,
highlighting the importance of these tools in their role. Data
Scientists, on the other hand, prioritize Jupyter Notebook usage,
data-related keywords, and programming languages like R and Python. The
analysis underscores the importance of both language proficiency and
domain-specific tools across different roles, providing valuable
insights into the distinct skill sets required for each category.

## Algorithm Testing Results

Searching for candidates with the keywords \"backend developer\" and
\"PhD.\" Our algorithm employed PageRank across the entire network,
ranking users based on these criteria, and identified Jonathan Conder as
the top candidate. We then used link prediction to explore Jonathan's
professional connections, allowing us to pinpoint additional candidates
who are also highly qualified in the field. This process led us to
recognize Hamed, Beici Liang, and Sebastian Macke, who similarly excel
in backend development and hold PhDs. This targeted approach ensures we
identify not only the primary candidate but also a group of potential
team members who share a robust academic and professional background,
streamlining our recruitment process with precision and efficiency.

# Conclusions

## Summary

Our project successfully demonstrates the potential of using GitHub
data, and network analysis to optimize hiring practices in the software
development industry. By leveraging extensive developer profiles and
collaboration data, we developed a composite scoring model that
evaluates both technical skills and collaborative capabilities.

## Key Findings

-   **Effective Identification of Candidates**: The model's high
    precision, recall, and F1 score confirm its ability to identify
    potential candidates who are both technically proficient and
    effective collaborators.

-   **Insightful Network Analysis**: The network metrics and community
    detection provided deep insights into the collaborative patterns and
    dynamics within the developer network.

-   **Enhanced Hiring Practices**: Our approach addresses the
    limitations of traditional hiring methods, offering a more refined
    and efficient process for selecting candidates.

## Future Work

-   **Incorporate Additional Data Sources**: Integrate more diverse data
    sources such as LinkedIn profiles, academic transcripts, and
    personal portfolios to provide a holistic view of candidates.

-   **Real-Time Data Updates**: Implement real-time data updates to keep
    the model current with the latest developer activities and trends.

-   **Industry Validation**: Conduct extensive industry validation to
    refine the model based on feedback from actual hiring processes and
    outcomes.

## Implications

By adopting our model, companies can significantly improve their hiring
practices, leading to better team dynamics, reduced project delays, and
overall enhanced productivity. Our approach offers a powerful tool for
addressing the challenges faced in the rapidly evolving software
development industry.

In conclusion, our project showcases the transformative potential of
combining network analysis with rich developer data from platforms like
GitHub. This innovative approach paves the way for more effective and
efficient hiring practices, ensuring that companies can build strong,
collaborative, and technically proficient teams.

