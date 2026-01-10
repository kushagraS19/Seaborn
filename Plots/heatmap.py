import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = sns.load_dataset("anagrams").head(10)
x = df.drop(columns = "attnr", axis = 1)

sns.heatmap(x, vmin = 0, vmax  = 12, cmap = "gnuplot", annot=True)
plt.show()

y = {
    "fontsize" : 20,
    "color" : "Pink"
}
var = np.linspace(1,10,10).reshape(2,5)
var1 = np.array([["a0","a1","a2","a3","a4"],
                 ["b0","b1","b2","b3","b4"]])
k = sns.heatmap(var, cmap= "PuOr", annot=var1, fmt="s", annot_kws= y, linewidth=5, linecolor="maroon", cbar = False , xticklabels=False, yticklabels= False)
k.set(xlabel="Python", ylabel = "Seaborn")
sns.set(font_scale=50)

plt.show()

# annot --> we can put our own values for display
# fmt --> We have to tell which type of data are we putting in annot
# annot_kws --> can change size and color of the displayed text.
# linewidth --> use to give spacing between the boxes.
# linecolor --> use to give color to the spacing between boxes.
# cbar = False --> Remove the color bar showing in the map.
# xticklables and yticklabels = False --> Remove the lables from x-axis and y-axis.