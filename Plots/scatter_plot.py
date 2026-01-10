import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("penguins").head(50)

m = {
    "Male" : "o",
    "Female" : ">"
}
sns.scatterplot(x= "bill_length_mm", y= "bill_depth_mm", data= df, hue= "sex", style= "sex", size= "sex", sizes = (100,40), palette="gist_ncar", markers= m)
plt.show()