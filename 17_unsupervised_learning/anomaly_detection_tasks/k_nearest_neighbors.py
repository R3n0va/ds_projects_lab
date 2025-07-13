import pandas as pd
from pyod.models.knn import KNN
from sklearn.ensemble import IsolationForest

RANDOM_STATE = 42

df = pd.read_csv('/datasets/sales.csv')
data = df[['Sales', 'Profit']]

estimation_knn = KNN()
outliers_knn = estimation_knn.fit_predict(data)
print("Количество аномалий (KNN): ", (outliers_knn == 1).sum())

estimation_iforest = IsolationForest(random_state=RANDOM_STATE)
outliers_iforest = estimation_iforest.fit_predict(data)
print("Количество аномалий (изоляционный лес): ", (outliers_iforest == -1).sum())

knn_anomalies = (outliers_knn == 1)
iforest_anomalies = (outliers_iforest == -1)
print("Совпало: ", (knn_anomalies & iforest_anomalies).sum())
