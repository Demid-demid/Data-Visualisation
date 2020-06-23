#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



pokemon = pd.read_csv('/Users/demiddemidov/Desktop/D/my projects/Data Visualization/Quizzes/pokemon.csv')
print(pokemon.shape)
print(pokemon.head(10))
base_color = sb.color_palette()[0] #<--- will make the color Blue 
get_order= pokemon["generation_id"].value_counts().index

sb.countplot(data = pokemon, x= "generation_id", color = base_color, order=get_order)

type_order= pokemon["type_1"].value_counts().index
sb.countplot(data=pokemon, y= "type_1", color=base_color, order=type_order)

#plt.xticks(rotation=90) #to rotate a by 90 


# %%
