import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

sns.catplot(x = "size", y = "tip", data = df,kind="point", hue="sex", palette="PuOr", height=20, )
plt.show()