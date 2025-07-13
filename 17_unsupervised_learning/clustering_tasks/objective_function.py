import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

data = pd.read_csv('/datasets/segments.csv')
centers = np.array([[20, 80, 8], [50, 20, 5], [20, 30, 10]])

model = KMeans(n_clusters=3, random_state=12345)
model.fit(data)

print("Целевая функция:")
print(model.inertia_)

model_with_centers = KMeans(n_clusters=3, init=centers, n_init=1, random_state=12345)
model_with_centers.fit(data)

print("Целевая функция модели с начальными центроидами:")
print(model_with_centers.inertia_)