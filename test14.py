# -*- coding: utf-8 -*-
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa'],
}
app.layout = html.Div(
    [
        dcc.RadioItems(
            list(all_options.keys()),
            'America',
            id='countries-radio',
        ),
        html.Hr(),
        dcc.RadioItems(id='cities-radio'),
        html.Hr(),
        html.Div(id='display-selected-values'),
    ]
)

#callback 3개
@app.callback(
    Output('cities-radio', 'options'), Input('countries-radio', 'value')
    #값이 아닌 옵션을 바꿈 
)
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(Output('cities-radio', 'value'), Input('cities-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']
#기본 값 설정하는 곳
#ex)미국이나 캐나다를 선택했을 경우 도시는 표시가 안 되어 있음


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'),
)
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city,
        selected_country,
    )


if __name__ == '__main__':
    app.run_server(debug=True)