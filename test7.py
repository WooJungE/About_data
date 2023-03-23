import dash
from dash import html, dcc

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.Div(dcc.Input(type='text')),
        #'제출'
        html.Button('Submit'),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
