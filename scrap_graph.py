import seaborn as sns; sns.set(style="ticks", color_codes=True)
from Parts_Final import *
pd.set_option('display.max_columns',50)
pd.set_option('display.width',150)

# iris = sns.load_dataset("iris")
# g = sns.pairplot(iris)
# print(iris.head())

final, num, percent = get_final('USP')

df = final[2]

print(df.head())
