import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

sns.stripplot(x="day", y="total_bill", data=df, hue="sex", palette="rocket_r", size=5, marker= "o", alpha = 1)
plt.show()

# single plot --> 

sns.stripplot(y = df["total_bill"])
plt.show()