import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/datasets/sales.csv')

boxplot = plt.boxplot(df['Profit'].values)
outliers = list(boxplot["fliers"][0].get_data()[1])
df_outliers = df[df["Profit"].isin(outliers)]
print("Количество аномалий: ", len(df_outliers))