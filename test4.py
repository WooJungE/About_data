import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div( #2개의 드롭다운을 담고 있음
            [
                html.Label('Dropdown'),
                dcc.Dropdown(
                    options=[ #딕셔너리를 리스트로 받음 
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],
                    value='MTL', #드럽다운에 표시되는 값
                ),
                html.Br(),
                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],
                    value=['MTL', 'SF'],
                    multi=True,
                ),
            ],
            style={'padding': 10, 'flex': 1},
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'row'},
)

if __name__ == '__main__':
    app.run_server(debug=True)