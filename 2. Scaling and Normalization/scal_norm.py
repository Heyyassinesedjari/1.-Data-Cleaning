#In scaling, you're changing the range of your data, while
#In normalization, you're changing the shape of the distribution of your data.
#The point of normalization is to change your observations so that they can be described as a normal distribution.
#Transforming your data so that it fits within a specific scale, like 0-100 or 0-1
#Scale data when you're using methods based on measures of how far apart data points are SVMs KNN
#Linear discriminant analysis (LDA) and Gaussian naive Bayes. (Pro tip: any method with "Gaussian" in the name probably assumes normality.)


import pandas as pd
import numpy as np

#for plotting
import seaborn as sns
import matplotlib.pyplot as plt

#for min-max scaling
from mlxtend.preprocessing import minmax_scaling

#for box-cox transformation
from scipy import stats

#reading all our data
kickstarters_2018 = pd.read_csv("ks-projects-201801.csv")

#set seed for reproducibility
np.random.seed(0)

#selecting the goal column
original_data = pd.DataFrame(kickstarters_2018["goal"])

#Practicing normalization
#min-max scaling
scaled_data = minmax_scaling(original_data, columns=["goal"])

print("Original data:")
print(original_data.tail())
print("="*50)
print("Scaled data:")
print(scaled_data.tail())

#Practicing normalization
#Getting the index of all positive pledges (Box-Cox only takes positive values)
index_of_positive_pledges = kickstarters_2018["pledged"] > 0

#Getting the positive pledges values
positive_pledges = kickstarters_2018["pledged"].loc[index_of_positive_pledges]

#normalizing data
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], name= "pledged", index=positive_pledges.index)

#plotting
ax = sns.histplot(normalized_pledges, kde=True)
ax.set_title("normalized pledges")
plt.show()









