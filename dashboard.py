import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import datetime as dt

filename = str(input('Digite o nome do arquivo, pô:'))

app = dash.Dash(__name__)

app.layout = html.Div(children=[
                                html.H1(children='ETILICOS Internet Velocity'),
                                dcc.Graph(
                                            id='live-update-graph',
                                        ),
                                dcc.Interval(
                                                id='interval-component',
                                                interval=5*60*1000, # in milliseconds
                                                n_intervals=0
                                            )
                                ]
                        )

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    df = pd.read_csv('{}.csv'.format(filename)).drop('Unnamed: 0', axis=1)
    df.time = pd.to_datetime(df.time)

    data = [
                {
                    'x': df.time, 'y': df.fast, 
                    'type': 'line', 'name': 'fast'
                },
                {
                    'x': df.time, 'y': df.velocidadeideal, 
                    'type': 'line', 'name': 'velocidadeideal'
                },
                {
                    'x': df.time, 'y': df.brasilBandaLarga, 
                    'type': 'line', 'name': 'brasilBandaLarga'
                },
                {
                    'x': df.time, 'y': df.set_index('time').mean(axis=1), 
                    'type': 'line', 'name': 'mean', 
                    'line':{'dash': 'dash', 'color': 'red', 'width':5},
                }
            ]

    figure={
        'data': data,
        'layout': 
                    {
                        'title': 'Download velocity. Last reload at: {}'.format(dt.datetime.now())
                    }
        }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)