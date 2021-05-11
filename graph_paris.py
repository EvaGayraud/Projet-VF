import plotly.express as px
import data_loader
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df0 = data_loader.get_subsample()
df = data_loader.load_house_attributes(df0)

app.layout = html.Div([

    html.H1("DVF Paris", style={'text-align': 'center'}),

    dcc.Dropdown(id="months",
                 options=[
                     {"label": "Jan", "value": 1},
                     {"label": "Fev", "value": 2},
                     {"label": "Mars", "value": 3},
                     {"label": "Avril", "value": 4},
                     {"label": "Mai", "value": 5},
                     {"label": "Juin", "value": 6},
                     {"label": "Juillet", "value": 7},
                     {"label": "Août", "value": 8},
                     {"label": "Sep", "value": 9},
                     {"label": "Oct", "value": 10},
                     {"label": "Nov", "value": 11},
                     {"label": "Dec", "value": 12}],
                 multi=False,
                 value="Jan",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='dispersion', figure={})

])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='dispersion', component_property='figure')],
    [Input(component_id='months', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The month chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["months"] == option_slctd]

    fig = px.box(dff, x='Commune', y='Valeur fonciere', hover_name='Type local')

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)




