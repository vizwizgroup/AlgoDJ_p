
from pathlib import Path
import pandas as pd
from data.dataset import LoadData
from dash_holoniq_wordcloud import DashWordcloud
from dash import Dash, html
import dash_bootstrap_components as dbc 
from model.model_cosine_similarity import SongRecommender
from model.network import Network


df_raw = pd.read_csv('https://raw.githubusercontent.com/vizwizgroup/small_data/main/music_data_1k.csv')
# df_raw = LoadData("million").get_data()
playlist = SongRecommender(df_raw, 'Gimmie Trouble').recommender()

g = Network(limit=30, num_songs=20, num_related=3).build_network(df_raw, playlist, "artist")
#g.degree
#g.degree['Bob Dylan']


dicttolist = list(g.degree)
artists1 = [list(ele) for ele in dicttolist]
artists = artists1[0:20] #limiting to just ten artists in the word cloud for now for spacing
#artists

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])

# this was the dummy data that I was working with before getting
# the data from Stu's classes
# artists = [
#     ["Taylor Swift", 30],
#     ["The Rolling Stones", 20],
#     ["Red Hot Chili Peppers", 10],
#     ["The Beatles", 40],
#     ["Beyonce", 30],
#     ["Coldplay", 20],
#     ["Maroon 5", 20],
#     ["Foo Fighters", 10],
#     ["Zac Brown Band", 10],
#     ["O.A.R.", 10]
# ]

WordCloud = html.Div([
# app.layout = html.Div([
   
        dbc.Row([
            dbc.Col([
                dbc.Label("Word Cloud:"),
            DashWordcloud(
                id='wordcloud',
                list=artists,
                width=540, height=300,
                gridSize=20,
                color='#f1f1f1',
                backgroundColor='#421331',
                shuffle=False,
                rotateRatio=0.5,
                shrinkToFit=True,
                shape='circle',
                hover=True
            )
                
            ])
        ])
        
    ])

# if __name__ == '__main__':
#     app.run_server('0.0.0.0',debug=True, threaded=True, use_reloader=True, port=8888)


# if __name__ == '__main__':
#     app.run_server("0.0.0.0",debug=True, threaded=False, use_reloader=False, port=8050)