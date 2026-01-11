import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

sns.set_style("darkgrid")
sns.despine() # Remove axis line
plt.figure(figsize=(12,8))
sns.set_context("notebook",font_scale=2)
sns.barplot(x="day", y="total_bill", data= df, palette="Accent")
plt.show()