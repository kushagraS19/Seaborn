import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")

sns.violinplot(x= "time", y="total_bill", data= df, linewidth=2, palette="PuOr", order= ["Dinner", "Lunch"], saturation=9, inner="quart" )
plt.show()

sns.violinplot(x = "day", y = "total_bill", data= df, linewidth=2, hue = "sex", split=True)
plt.show()

# Single violin plot -->

sns.violinplot(df["total_bill"])
plt.show()