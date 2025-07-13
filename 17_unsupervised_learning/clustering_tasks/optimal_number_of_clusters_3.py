import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('/datasets/segments.csv')

model_3 = KMeans(n_clusters=3, random_state=12345)
model_3.fit(data)

print("Типичные пользователи сегментов для 3-х кластеров:")
print(model_3.cluster_centers_.round())

model_4 = KMeans(n_clusters=4, random_state=12345)
model_4.fit(data)

print("Типичные пользователи сегментов для 4-х кластеров:")
print(model_4.cluster_centers_.round())
