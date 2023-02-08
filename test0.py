#필요한 패키지 불러오기
from dash import dcc, html, Dash
import plotly.express as px
import pandas as pd

app = Dash(__name__) # "__main__"

#샘플 데이터셋 만들기
df = pd.DataFrame(
    {
        "Fruit": [
            "Apples",
            "Oranges",
            "Bananas",
            "Apples",
            "Oranges",
            "Bananas",
        ],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

#plotly express의 바 그래프
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

#dcc.Graph 클래스
#dash는 HTML 요소들을 app.layout에 넣어 화면 배치 구성
app.layout = html.Div(
    children=[
        html.H1(children='Hello Dash'),
        html.Div(
            children='''
        Dash: A web application framework for your data.
    '''
        ),
        dcc.Graph(id='example-graph', figure=fig),
    ]
)

#서버를 실행하는 코드
if __name__ == '__main__':
    app.run_server(debug=True) #디버그 모드로 서버 실행
    #서버 성능이 떨어지고 보안에 취약하지만 자동 업데이트 됨

#app.py 실행