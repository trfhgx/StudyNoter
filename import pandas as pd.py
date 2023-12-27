import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# creating dataframe
df = pd.DataFrame({
    'X': [1, 2, 3],
    'Y': [3, 4, 5],
    'Z': [2, 1, 2]
})
 
# creating subplots
ax = plt.subplots()
 
# plotting columns
ax = sns.barplot(x=df["X"], y=df["Y"], color='b')
ax = sns.barplot(x=df["X"], y=df["Z"], color='r')
 
# renaming the axes
ax.set(xlabel="x-axis", ylabel="y-axis")
 
# visualizing illustration
plt.show()