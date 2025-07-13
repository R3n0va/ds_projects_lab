import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('/datasets/segments.csv')

X = data.select_dtypes(include=['number'])

model = KMeans(n_clusters=3, random_state=12345)
model.fit(X)

print("Центроиды кластеров:")
print(model.cluster_centers_)
