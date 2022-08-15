import dash  # version 1.13.1
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import pandas as pd
import numpy as np
from numpy import int64

df = pd.read_csv("https://raw.githubusercontent.com/tom6174/tom6174.github.io/main/tmp_data/2021-population.csv", engine='python', encoding='utf-8', dtype={ "총인구": int64 })
df.rename(columns={'광역': '광역시도', '군구': '시군구'}, inplace=True)

print(df['광역시도'].unique())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1("대한민국 인구 분포", style={"textAlign":"center"}),
    html.Hr(),
    html.P("시군구별 인구:"),
    html.Div(html.Div([
        dcc.Dropdown(id='광역시도', clearable=False,
                     value="서울특별시",
                     options=[{'label': x, 'value': x} for x in
                              df["광역시도"].unique()]),
    ],className="two columns"),className="row"),

    html.Div(id="output-div", children=[]),
])

@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="광역시도", component_property="value"),
)
def make_graphs(province_chosen):
    # HISTOGRAM
    df_bar = df[(df["광역시도"]==province_chosen) & ~(df["시군구"]==province_chosen)]
    print(df_bar)
    print(df_bar.dtypes)
    fig_hist = px.line(df_bar, x="시군구", y="총인구")
    # fig_hist.update_xaxes(categoryorder="total descending")

    # # STRIP CHART
    # fig_strip = px.strip(df_hist, x="animal_stay_days", y="intake_type")

    # # SUNBURST
    # df_sburst = df.dropna(subset=['chip_status'])
    # df_sburst = df_sburst[df_sburst["intake_type"].isin(["STRAY", "FOSTER", "OWNER SURRENDER"])]
    # fig_sunburst = px.sunburst(df_sburst, path=["animal_type", "intake_type", "chip_status"])

    # # Empirical Cumulative Distribution
    # df_ecdf = df[df["animal_type"].isin(["DOG","CAT"])]
    # fig_ecdf = px.ecdf(df_ecdf, x="animal_stay_days", color="animal_type")

    # # LINE CHART
    # df_line = df.sort_values(by=["intake_time"], ascending=True)
    # df_line = df_line.groupby(
    #     ["intake_time", "animal_type"]).size().reset_index(name="count")
    # print(df_line.head())
    # fig_line = px.line(df_line, x="intake_time", y="count",
    #                    color="animal_type", markers=True)

    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_hist)], className="twelve columns"),
            # html.Div([dcc.Graph(figure=fig_strip)], className="six columns"),
        ], className="row"),
        # html.H2("All Animals", style={"textAlign":"center"}),
        # html.Hr(),
        # html.Div([
        #     html.Div([dcc.Graph(figure=fig_sunburst)], className="six columns"),
        #     html.Div([dcc.Graph(figure=fig_ecdf)], className="six columns"),
        # ], className="row"),
        # html.Div([
        #     html.Div([dcc.Graph(figure=fig_line)], className="twelve columns"),
        # ], className="row"),
    ]

if __name__ == '__main__':
    app.run_server(debug=True)

    
    
# https://youtu.be/4gDwKYaA6ww