import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns

data = pd.read_csv('/datasets/cars.csv')

model = KMeans(n_clusters=3, random_state=12345)
model.fit(data)

data['label'] = model.labels_.astype(str)

sns.pairplot(data, hue='label', vars=data.columns[:-1], diag_kind='hist')
