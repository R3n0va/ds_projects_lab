import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

data = pd.read_csv('https://code.s3.yandex.net/datasets/segments.csv')
centers = np.array([[20, 80, 8], [50, 20, 5], [20, 30, 10]])

model = KMeans(n_clusters=3, init=centers, random_state=12345)
model.fit(data)

centroids = pd.DataFrame(model.cluster_centers_, columns=data.columns)
data['label'] = model.labels_.astype(str)
centroids['label'] = ['0 centroid', '1 centroid', '2 centroid']
data_all = pd.concat([data, centroids], ignore_index=True)

pairgrid = sns.pairplot(data_all, hue='label', diag_kind='hist')
pairgrid.map_offdiag(sns.scatterplot, s=200, marker='*', palette='flag')


centroids_init = pd.DataFrame(centers, columns=data.columns[:-1])
centroids_init['label'] = 4  


pairgrid.data = centroids_init


for i, var_x in enumerate(pairgrid.x_vars):
    for j, var_y in enumerate(pairgrid.y_vars):
        if i != j:
            ax = pairgrid.axes[j, i]
            ax.scatter(centroids_init[var_x], centroids_init[var_y],
                       s=250, c='red', marker='X', label='init centroid')


handles, labels = pairgrid.axes[0, 0].get_legend_handles_labels()
by_label = dict(zip(labels, handles))
pairgrid.axes[0, 0].legend(by_label.values(), by_label.keys(), loc='upper right')

pairgrid.fig.suptitle('KMeans Clustering with Centroids and Initial Centers', y=1.02)
pairgrid.fig.tight_layout()
pairgrid.fig.subplots_adjust(top=0.95)
pairgrid.fig.show()
