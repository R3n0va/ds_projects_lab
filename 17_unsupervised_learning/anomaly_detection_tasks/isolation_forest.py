import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('/datasets/sales.csv')
data = df[['Sales', 'Profit']]

isolation_forest = IsolationForest(n_estimators=100, random_state=12345)

predictions = isolation_forest.fit_predict(data)

outliers = predictions[predictions == -1].tolist()

print("Количество аномалий: ", len(outliers))
