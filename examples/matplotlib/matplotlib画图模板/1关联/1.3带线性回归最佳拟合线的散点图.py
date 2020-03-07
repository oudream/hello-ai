# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings('ignore')
"""
如果你想了解两个变量如何相互改变，那么最合适的线就是要走的路。
下图显示了数据中各组之间最佳拟合线的差异。要禁用分组并仅为整个数据集绘制一条最佳拟合线，请从下面的调用中删除该参数。
"""
# # Import Data
# df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
# df_select = df.loc[df.cyl.isin([4, 8]), :]
#
# # Plot
# sns.set_style("white")
# gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select,
#                      height=7, aspect=1.6, robust=True, palette='tab10',
#                      scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))
#
# # Decorations
# gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
# plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=10)
# plt.show()


"""

或者，您可以在其自己的列中显示每个组的最佳拟合线。你可以通过在里面设置参数来实现这一点。"""

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4,8]), :]

# Each line in its own column
sns.set_style("white")
# set_style( )是用来设置主题的，Seaborn有五个预设好的主题： darkgrid , whitegrid , dark , white ,和 ticks  默认： darkgrid
# set( )通过设置参数可以用来设置背景，调色板等，更加常用。

gridobj = sns.lmplot(x="displ", y="hwy",
                     data=df_select,
                     height=7,
                     robust=True,
                     palette='Set1',
                     col="cyl",
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))

plt.title("Scatterplot with line of best fit grouped by number of cylinders",  fontsize=10)
plt.show()


