import numpy as np
import pandas as pd

life = pd.read_csv('life_expectancy.csv', index_col=0)
print(life.head(5))

# find by label
life.loc[:, '1800'].describe()
life.loc[:, '2013'].describe()

# find by index
life.iloc[:, [0,-1]].describe() 
