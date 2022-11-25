

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc




# app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])


Genre = ["Pop", "Classic", "Country", "Jazz"]

# app.layout = dbc.Container([
UserInput1 = html.Div([  
    dbc.Row([
        dbc.Col([
            dbc.Label("Playlist size"),
            dbc.Select(
                options=[{"label": i, "value": i}
                    for i in range(2,37)]),
            ]),
        dbc.Col([
            dbc.Label("From"),
            dbc.Select(
                options=[{"label": x, "value": x}
                    for x in range(1970,2023)]),
        ]),
        dbc.Col([
            dbc.Label("To"),
            dbc.Select(
                options=[{"label": y, "value": y}
                    for y in range(1970,2023)]),
        ]),
        
        dbc.Col([
            dbc.Label("Genre"),
            dbc.Select(
                options=[{"label": i, "value": i}
                    for i in Genre]),
        ]),
        ]),
    html.Br(),
  
])

# if __name__ == '__main__':
    # app.run_server('0.0.0.0',debug=True, threaded=False, use_reloader=False, port=8010)