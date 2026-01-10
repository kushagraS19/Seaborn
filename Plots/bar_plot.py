import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

df = sns.load_dataset("Penguins").head(50)
sns.set(style="darkgrid")
sns.barplot(x= df.island , y= df.bill_depth_mm,data=df ,hue="sex", palette="Accent", legend="auto", order= ["Dream", "Torgersen", "Biscoe"], hue_order= ["FEMALE", "MALE"], ci= 20, n_boot= 3, capsize=1, saturation=100)
# ci = For intervals
# n_boot = For gaping 
plt.show()
print(df.head())

# In horizontal bar graph only numerical values or data is allowed. No names or string data is allowed.

sns.barplot(x="bill_length_mm", y= "bill_depth_mm", data = df, hue = "sex", palette="Accent", ci= 20, n_boot= 3, orient= "h", saturation=0.5, errcolor="g" )
plt.show()