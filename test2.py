from dash import Dash, dcc, html
import plotly.graph_objs as go

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])

app = Dash(__name__)
app.layout = html.Div(
    dcc.Graph(id='example-graph', figure=fig),
    #어떤 그래프를 그릴 것인지 설정
)

if __name__ == '__main__':
    app.run_server(debug=True)

#상호작용 가능
#일부분만 설정 가능