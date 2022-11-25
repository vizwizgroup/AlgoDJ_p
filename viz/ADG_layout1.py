from os import path
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc 
import pandas as pd
import pandas_datareader.data as web 
import datetime
from header import Header
from user_input_row1 import UserInput1
from user_input_row2 import UserInput2
from user_input_row3 import UserInput3
from wordcloudviz import WordCloud
# from playlist1 import Playlist


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])




app.layout = dbc.Container([
    dbc.Row([Header]),
    dbc.Row([
        dbc.Col([
            dbc.Row([UserInput1, UserInput2, UserInput3]),
            dbc.Row([]),
            ]),
        dbc.Col([WordCloud]),
        ]),
])




if __name__ == '__main__':
    app.run_server(debug=True, threaded=False, use_reloader=False,port=8020)
    # app.run_server(debug=True)