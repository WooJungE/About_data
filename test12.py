from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            df['Indicator Name'].unique(),
                            'Fertility rate, total (births per woman)', #기본 값
                            id='xaxis-column',
                        ),
                        dcc.RadioItems( 
                            ['Linear', 'Log'],
                            'Linear', #기본 값
                            id='xaxis-type',
                            inline=True, #생략 가능
                        ),
                    ],
                    style={'width': '48%', 'display': 'inline-block'},
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            df['Indicator Name'].unique(),
                            'Life expectancy at birth, total (years)',
                            id='yaxis-column',
                        ),
                        dcc.RadioItems(
                            ['Linear', 'Log'],
                            'Linear',
                            id='yaxis-type',
                            inline=True,
                        ),
                    ],
                    style={
                        'width': '48%',
                        'float': 'right',
                        'display': 'inline-block',
                    },
                ),
            ]
        ),
        dcc.Graph(id='indicator-graphic'),
        dcc.Slider(
            df['Year'].min(),
            df['Year'].max(),
            step=None, #중간값 선택 불가능
            id='year--slider',
            value=df['Year'].max(),
            marks={str(year): str(year) for year in df['Year'].unique()},
        ),
    ]
)


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'),
)
def update_graph(
    xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value
):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(
        x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'], #line 67과 관련
        y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
        hover_name=dff[dff['Indicator Name'] == yaxis_column_name][
            'Country Name'
        ],
    )

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest'
    )

    fig.update_xaxes(
        title=xaxis_column_name,
        type='linear' if xaxis_type == 'Linear' else 'log',
    )

    fig.update_yaxes(
        title=yaxis_column_name,
        type='linear' if yaxis_type == 'Linear' else 'log', #linear과 Linear의 차이 때문에 if문으로 작성
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)