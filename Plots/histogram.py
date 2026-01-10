import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("diamonds")

sns.displot(df["price"], bins = [0, 2500, 5000, 7500,10000,12500,15000,17500], kde = True, rug = True, color= "hotpink")
plt.savefig("Hehe.png")
plt.show()