#%%


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



pokemon = pd.read_csv('/Users/demiddemidov/Desktop/D/my projects/Data Visualization/Quizzes/pokemon.csv')
print(pokemon.shape)
print(pokemon.head(10))
base_color = sb.color_palette()[0]

sb.countplot(data = pokemon, x= "generation_id",color = base_color)



# %%
