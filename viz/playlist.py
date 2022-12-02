
import numpy as np
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from model.model_cosine_similarity import SongRecommender


df_raw = pd.read_csv('https://raw.githubusercontent.com/vizwizgroup/small_data/main/music_data_1k.csv')
# df_raw = LoadData("million").get_data()
playlist = SongRecommender(df_raw, 'Gimmie Trouble').recommender(20)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# df = df.sample(50)
# add an id column and set it as the index
# in this case the unique ID is just the country name, so we could have just
# renamed 'country' to 'id' (but given it the display name 'country'), but
# here it's duplicated just to show the more general pattern.
# df['id'] = df['country']
# df_raw.set_index('id', inplace=True, drop=False)
playlist.index = np.arange(1, len(playlist)+1)
# playlist.set_index('index', inplace=True, drop=False)
playlist = playlist[['id','name', 'album', 'artists', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'liveness', 'valence', 'tempo']]
# display(playlist)
pl = playlist[['name', 'album', 'artists']]
# display(pl)

app = Dash(__name__, meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])


app.layout = html.Div([
# Playlist = html.Div([
    dbc.Label("Playlist: "),
    dash_table.DataTable(
        id='playlist',
        columns=[
            {'name': i, 'id': i, 'deletable': True} for i in pl.columns
            # omit the id column
            if i != 'id'
        ],
        # data= pl.to_dict('records'),
        data= pl.to_dict('dicts'),
        editable=True,
        # filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=True,
        selected_rows=[],
        page_action='native',
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='playlist_div')
])


@app.callback(
    Output('playlist_div', 'children'),
    Input('playlist', 'derived_virtual_row_ids'),
    Input('playlist', 'selected_row_ids'),
    Input('playlist', 'active_cell'),
    prevent_initial_call = True
    )
def update_graphs(row_ids, selected_row_ids, active_cell):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = playlist
        # pandas Series works enough like a list for this to be OK
        row_ids = playlist['id']
    else:
        dff = playlist.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['#FF69B4' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else '#0074D9'
              for id in row_ids]

    return [
        dcc.Graph(
            id=column + '--row-ids',
            figure={
                'data': [
                    {
                        'x': dff['name'],
                        'y': dff[column],
                        'type': 'bar',
                        'marker': {'color': colors},
                    }
                ],
                'layout': {
                    'xaxis': {'automargin': True},
                    'yaxis': {
                        'automargin': True,
                        'title': {'text': column}
                    },
                    'height': 250,
                    'margin': {'t': 10, 'l': 10, 'r': 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ['danceability', 'energy', 'loudness', 'speechiness'] if column in dff
        # for column in [ 'acousticness', 'liveness'] if column in dff
        # for column in ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'liveness'] if column in dff
    ]


if __name__ == '__main__':
    app.run_server(debug=True, threaded=False, use_reloader=False, port=8090)
    
