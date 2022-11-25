

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc




# app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])


Genre = ["Pop", "Classic", "Country", "Jazz"]

# app.layout = dbc.Container([
UserInput2 = html.Div([  
   
    dbc.Row([
        dbc.Col([
            dbc.Label("Title"),
            dbc.Input(placeholder="Valid input...", valid=True, className="mb-3"),
        ],width={"size":9,"order":1}),
        dbc.Col([
            dbc.Label("Song sample"),
            dbc.Button(
            "Upload",
            href="/static/data_file.txt",
            download="my_data.txt",
            external_link=True,
            color="primary",
        ),
        ],width={"size":3,"order":2})
    ]),
    html.Br(),
  
])

# if __name__ == '__main__':
    # app.run_server('0.0.0.0',debug=True, threaded=False, use_reloader=False, port=8010)