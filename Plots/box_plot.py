import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set(style="whitegrid")

sns.boxplot(x="day", y="total_bill", data = df, hue="sex", order= ["Fri", "Sat", "Sun", "Thur"], showmeans = True, meanprops = {
    "marker" : "+", "markeredgecolor" : "white"
}, linewidth=3, linecolor="maroon", palette="PuOr", orient="v")
plt.show()

# single box plot -->

sns.boxplot(x= df["total_bill"], data = df, linewidth=3, linecolor="maroon", palette="PuOr")

plt.show()