# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id='input-1-state', type='text', value='Montréal'),
        dcc.Input(id='input-2-state', type='text', value='Canada'),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Div(id='output-state'),
    ]
)

#test state는 바뀌지만 결과는 나오지 않음 
#State('id', '')
@app.callback(
    Output('output-state', 'children'),
    Input('submit-button-state', 'n_clicks'), #클릭 횟수
    State('input-1-state', 'value'),
    State('input-2-state', 'value'),
    #State 대신에 input일 경우 입력시 바로 출력되는 형태
)
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(
        n_clicks, input1, input2
    )


if __name__ == '__main__':
    app.run_server(debug=True)