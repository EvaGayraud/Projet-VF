import plotly.express as px
import data_loader
import matplotlib.pyplot as plt

df_paris = data_loader.load_house_attributes('https://www.data.gouv.fr/fr/datasets/r/90a98de0-f562-4328-aa16-fe0dd1dca60f')

fig = px.box(df_paris, x='Code postal', y='Valeur fonciere', hover_name='Type local')
fig.show()


