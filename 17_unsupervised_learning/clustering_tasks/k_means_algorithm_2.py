import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

data = pd.read_csv('/datasets/segments.csv')
centers = np.array([[20, 80, 8], [50, 20, 5], [20, 30, 10]])

model = KMeans(n_clusters=3, random_state=12345)
model.fit(data)

print("Центроиды кластеров:")
print(model.cluster_centers_)

model_with_centers = KMeans(n_clusters=3, init=centers, n_init=1, random_state=12345)
model_with_centers.fit(data)

print("Центроиды кластеров для модели с начальными центроидами:")
print(model_with_centers.cluster_centers_)