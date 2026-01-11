import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

fg = sns.FacetGrid(df, col="day", hue="sex", palette="Accent")
fg.map(plt.bar,"total_bill","tip").add_legend()
plt.show()