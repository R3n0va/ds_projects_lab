import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns

data_full = pd.read_csv('/datasets/cars_label.csv')

data = data_full.drop(columns=['brand'])

model = KMeans(n_clusters=3, random_state=12345)
model.fit(data)

centroids = pd.DataFrame(model.cluster_centers_, columns=data.columns)

centroids['brand'] = 4

pairgrid = sns.pairplot(data_full, hue='brand', diag_kind='hist')
pairgrid.data = centroids
pairgrid.map_offdiag(func=sns.scatterplot, s=200, marker='*', palette='flag')
