import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

# By direct data --> 

"""var = [1,2,3,4,5,6,7]
var1 = [2,3,4,5,5,6,7]

sns.lineplot(x=var, y=var1)

plt.show()"""

# By dataset --> 

"""var = [1,2,3,4,5,6,7]
var1 = [2,3,4,5,5,6,7]

df = pd.DataFrame({"var" : var, "var1" : var1})

sns.lineplot(x="var", y="var1", data= df)

plt.show()"""

#_____________________________________________________________________________________________________________

# Loading datasets --> 

data = sns.load_dataset("penguins").head(20)
print(data.head())

sns.lineplot(x="bill_length_mm", y="bill_depth_mm", data=data , hue="sex", style="sex", palette="Accent", markers=['o','>'],legend=False)

plt.grid() # we can also use matplotlib functions with seaborn
plt.title("Matplotlib and seaborn") 
plt.show()

# hue --> plotting of popular data
# palette --> for changing color by using color bar