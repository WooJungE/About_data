import plotly.express as px
iris = px.data.iris()

fig = px.scatter(
    iris,
    x="petal_length",
    y="petal_width",
    color="species",
    size="sepal_length",
    hover_data=["sepal_width"],
    height=400,
    width=800,
)
fig.show()