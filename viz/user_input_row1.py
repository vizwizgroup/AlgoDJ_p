from dash import Dash, html, dcc
from dash.exceptions import PreventUpdate
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from app.classes import User

global data1 




app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], meta_tags=[{'name': 'viewport', 'content': 'width=device-width,initial-scale=1.0'}])



Genre = ["Pop", "Classic", "Country", "Jazz", "Rock", "Hard Rock", "Post-rock", "Metal", "Heavy metal", "Flamenco"]

# app.layout = dbc.Container([
UserInput1 = html.Div([  
    dbc.Row([
        dbc.Col([
            dbc.Label("Playlist size"),
            dbc.Select( id = "playlist-size",
                options=[{"label": i, "value": i}
                    for i in range(2,37)]),
            ]),
        dbc.Col([
            dbc.Label("From"),
            dbc.Select( id = "from", 
                options=[{"label": x, "value": x, "type":"number"}
                    for x in range(1950,2023)]),
        ]),
        dbc.Col([
            dbc.Label("To"),
            dbc.Select( id = "to",
                options=[{"label": y,"value": y, "type":"number",}
                    for y in range(1950,2023)]),
        ]),
        
        dbc.Col([
            dbc.Label("Genre"),
            dbc.Select( id = "genre",
                options=[{"label": i, "value": i}
                    for i in Genre]),
        ]),
        ]),
    html.Div(id="row1_validation"),
    html.Br(),
    dcc.Store(id="store-data1", data=[], storage_type="memory")
  
])

if __name__ == '__main__':
    app.run_server('0.0.0.0',debug=True, threaded=False, use_reloader=False, port=8010)
    
# def init_input_row1_callbacks(app):
    
    
#     @app.callback(
#         Output( component_id="first-row-output", component_property="children"),
#         Input(component_id= "from",              component_property="value"),
#         Input(component_id= "to",                component_property="value"),
#         Input(component_id= "playlist-size",     component_property="value")
#     )
#     def validate_values(year_from, year_to, playlist_size):

#         if (year_from is None) or (year_to is None):
#             raise PreventUpdate
#         elif int(year_from) >= int(year_to):
#             # return 'Alert: Start year must be smaller than end year!'
#             return dbc.Alert("Alert: Start year must be smaller than end year!", color="warning")
#         elif playlist_size is None:
#             # return 'Alert: Please select playlist size!'
#             return dbc.Alert("Please select playlist size!", color="warning")
        
        
#     @app.callback(
#         [Output(component_id="store-data1",  component_property="data")],
#         [Input(component_id="playlist-size", component_property="value"),
#          Input(component_id="from",          component_property="value"),
#          Input(component_id="to",            component_property="value"),
#          Input(component_id="genre",         component_property="value")],
#         [State(component_id="store-data1",   component_property="data")],
#         prevent_initial_call = True
#     )
#     def extract_row1_data(playlist_size, yr_from, yr_to, genre, store_data1):
    
#         data1 = {"playlist_size": playlist_size, 
#                 "yr_from"      : yr_from,
#                 "yr_to"        : yr_to,
#                 "genre"        : genre}
#         return [data1]
    