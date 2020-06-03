import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('bojack/bojack_ratingsedit.csv')

#dots of all the ratings
#sns.swarmplot(x="Number", y="Rating", data=df)
#bar graph 
#sns.catplot("Season", "Rating", "Episode", data=df, kind="bar", palette="muted", legend=False)
#sns.violinplot(x = "Rating", data=df)
#sns.boxplot(x="Rating", data=df)
#sns.relplot(x="Number", y="Rating", kind="line", data=df)
#sns.relplot(x="Episode", y="Rating", hue="Season", kind="line", legend="full", data=df)
#sns.relplot(x="Episode", y="Rating", col="Season", kind="line", legend="full", data=df)

plt.show()

