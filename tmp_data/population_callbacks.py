import dash  # version 1.13.1
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER

import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/tom6174/tom6174.github.io/main/tmp_data/2021-population.csv", engine='python', encoding='utf-8')
df.rename(columns={'광역': '광역시도', '군구': '시군구'}, inplace=True)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("대한민국 인구 분포", style={"textAlign":"center"}),
    html.Hr(),
    html.Div(html.Div([
        dcc.Dropdown(id='광역시도', clearable=False,
                     value="서울특별시",
                     options=[{'label': x, 'value': x} for x in df["광역시도"].unique()]),
    ],className="two columns")),
    html.Div([html.H4("의 인구: "), html.H4(html.Div(id="result-num", children=[]))]),
    html.Div(id="output-div", children=[]),
])

@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="광역시도", component_property="value"),
)
def make_graphs(province_chosen):
    # HISTOGRAM
    df_bar = df[(df["광역시도"]==province_chosen) & ~(df["시군구"]==province_chosen)]
    # print(df_bar)
    fig_hist = px.bar(df_bar, x="시군구", y="총인구")

    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_hist)], className="twelve columns"),
            # html.Div([dcc.Graph(figure=fig_strip)], className="six columns"),
        ], className="row"),
    ]

@app.callback(Output(component_id="result-num", component_property="children"),
              Input(component_id="광역시도", component_property="value"),
)
def return_sum(province_chosen):
    df_and = df[(df["광역시도"]==province_chosen) & (df["시군구"]==province_chosen)]

    return df_and["총인구"].iloc[0]

if __name__ == '__main__':
    app.run_server(debug=True)