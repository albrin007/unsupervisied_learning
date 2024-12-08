from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df)

# Visualizing the clusters
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=kmeans.labels_, cmap='viridis')
plt.title('KMeans Clustering (2D Visualization)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

# Applying Hierarchical clustering
agg_clust = AgglomerativeClustering(n_clusters=3)
agg_clust.fit(df)

# Plotting the Dendrogram
plt.figure(figsize=(10, 7))
sch.dendrogram(sch.linkage(df, method='ward'))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()

# Visualizing the clusters 
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=agg_clust.labels_, cmap='viridis')
plt.title('Hierarchical Clustering (2D Visualization)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
