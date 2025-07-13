import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans

data = pd.read_csv('/datasets/segments.csv')

model = KMeans(n_clusters=4, random_state=12345)
model.fit(data)

centroids = pd.DataFrame(model.cluster_centers_, columns=data.columns)
data['label'] = model.labels_.astype(str)
centroids['label'] = ['0 centroid', '1 centroid', '2 centroid', '3 centroid']
data_all = pd.concat([data, centroids], ignore_index=True)

sns.pairplot(data_all, hue='label', diag_kind='hist')