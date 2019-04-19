from sklearn import cluster, datasets

iris = datasets.load_iris()
iris_X = iris.data

kmeans_fit = cluster.KMeans(n_clusters = 3).fit(iris_X)

cluster_labels = kmeans_fit.labels_
print('ffffffffffffff')
print(cluster_labels)
print('=========')

iris_y = iris.target
print('ttttttttttttttt')
print(iris_y)


