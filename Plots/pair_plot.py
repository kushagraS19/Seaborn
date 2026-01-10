import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips").head(20)

sns.pairplot(df,vars=["total_bill","tip"], hue="sex", hue_order=["Female","Male"], palette="PuOr")
plt.show()

sns.pairplot(df, hue="sex", hue_order=["Female","Male"], palette="PuOr",kind="scatter",markers=["o","<"])
plt.show()