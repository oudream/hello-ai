# Render our plots inline

import pandas as pd
import matplotlib.pyplot as plt

from fastai.learner import *
from fastai.column_data import *

# pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

path='/eee/ml-latest-small/'

ratings = pd.read_csv(path+'ratings.csv')
ratings.head()

ratings.plot

print(type(ratings))

