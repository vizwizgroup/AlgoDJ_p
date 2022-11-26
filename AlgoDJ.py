from os import path
from dash import dash, html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc 
import pandas as pd
from viz.ADJ_layout1 import ADJ_Layout 


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])




app.layout = dbc.Container([
    html.Div([ADJ_Layout])
])




if __name__ == '__main__':
    app.run_server(debug=True, threaded=False, use_reloader=False,port=8020)
    # app.run_server(debug=True)