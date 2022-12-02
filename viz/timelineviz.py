
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, dcc, html
import plotly.graph_objects as go
from model.model_cosine_similarity import SongRecommender
from model.network import Network
from data.dataset import LoadData
import dash_bootstrap_components as dbc

df_raw = pd.read_csv('https://raw.githubusercontent.com/vizwizgroup/small_data/main/music_data_1k.csv')
# df_raw = LoadData("million").get_data()
# df_raw = pd.read_csv("../data/music_data_1k.csv")
# df_raw = pd.read_csv("./tracks_features.csv")


playlist = SongRecommender(df_raw, 'Gimmie Trouble').recommender()



fig = go.Figure(px.histogram(playlist, x = 'release_date', color = 'explicit', title = 'Date Distribution of Songs in Playlist'))
fig.update_layout(bargap = 0.2)


app = Dash(__name__ ,external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])

# app.layout = html.Div([
TimeLine = html.Div([
    dbc.Label("Date Distribution of Songs in Playlist:"),
    dcc.Graph(figure = fig)
])


if __name__ == '__main__':
    app.run_server(debug=True, threaded=False, use_reloader=False,port=8070)
# app.run_server(debug = True, use_reloader = False)