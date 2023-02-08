import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            children=[
                html.Label('Checkboxes'),
                dcc.Checklist(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],
                    value=['MTL', 'SF'],
                ),
                html.Br(),
                html.Label('Text Input'),
                dcc.Input(value='MTL', type='text'), #value가 없어도 됨 #placeholder="" 값을 입력하면 사라짐, 어떤 값을 입력해야 하는 지 알려줌
                html.Br(),
                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={
                        i: f'Label {i}' if i == 1 else str(i)
                        for i in range(1, 6)
                    },
                    value=5,
                ),
            ],
            style={'padding': 10, 'flex': 1},
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'row'},
)

if __name__ == '__main__':
    app.run_server(debug=True)