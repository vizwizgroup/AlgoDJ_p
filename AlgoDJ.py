from os import path
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc 
import pandas as pd
from viz.ADJ_layout1 import ADJ_Layout, init_input_layout1_callbacks
from app.lib import *
from viz.ADJ_layout1 import user_data

app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])
server = app.server



app.layout = dbc.Container([
    html.Div([ADJ_Layout])
])

init_input_layout1_callbacks(app)

 

if __name__ == '__main__':
    app.run_server(debug=True, threaded=False, use_reloader=False, port=8020)
    print(dict_to_df(user_data))
    # app.run_server(debug=True)
    
    


