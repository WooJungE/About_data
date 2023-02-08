import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value='MTL', #기본값 지정 else 아무것도 선택이 되지 않음(line이 없을 시에)
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

#하나만 선택 가능