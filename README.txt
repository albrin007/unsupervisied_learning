Clustering on the Iris Dataset
This project demonstrates the use of two clustering algorithms—KMeans and Hierarchical Clustering—on the Iris dataset. The goal is to group the data into clusters based on features, without using the species labels.

Project Overview
KMeans Clustering: A centroid-based algorithm that groups data into clusters.
Hierarchical Clustering: A tree-based algorithm that builds clusters step by step.
Requirements
You need to install the following libraries:

numpy
pandas
scikit-learn
matplotlib
scipy
To install them, run:

bash
Copy code
pip install numpy pandas scikit-learn matplotlib scipy
Project Structure
clustering_on_iris.py: The main Python script with the clustering code.
README.md: This file explaining the project.
Visualizations: Scatter plots showing the clustering results.
How the Code Works
Loading and Preprocessing:

Load the Iris dataset and exclude the species column (since it's unsupervised learning).
KMeans Clustering:

Apply KMeans clustering to group the data into 3 clusters.
Visualize the clusters in a 2D scatter plot.
Hierarchical Clustering:

Apply Agglomerative Hierarchical clustering.
Generate a dendrogram and visualize the clusters in a scatter plot.
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/clustering-on-iris.git
Navigate to the project directory:

bash
Copy code
cd clustering-on-iris
Run the script:

bash
Copy code
python clustering_on_iris.py
The script will:

Load the Iris dataset.
Apply KMeans and Hierarchical clustering.
Show visualizations of the clusters.
Conclusion
This project demonstrates how to apply KMeans and Hierarchical clustering to the Iris dataset and visualize the results.

License
This project is licensed under the MIT License.