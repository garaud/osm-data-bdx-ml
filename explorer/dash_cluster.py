"""Scatter plot for user and the related clusters
"""

from pathlib import Path

import pandas as pd

import seaborn as sns

import plotly.plotly as py
import plotly.graph_objs as go

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from data import read_pca, read_cluster, cluster_scatter, pca_arrow, rayon_estimation

print("read files")
centroid, cluster = read_cluster()
pcafeatures, pcaind = read_pca()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

app.layout = html.Div([
    html.H2("Cluster / PCA"),
    dcc.Dropdown(
        id='pca-dropdown',
        options=[
            {'label': 'PC1 / PC2', 'value': 'PC1,PC2'},
            {'label': 'PC1 / PC3', 'value': 'PC1,PC3'},
            {'label': 'PC2 / PC3', 'value': 'PC2,PC3'},
            {'label': 'PC1 / PC4', 'value': 'PC1,PC4'},
            {'label': 'PC2 / PC4', 'value': 'PC2,PC4'},
            {'label': 'PC3 / PC4', 'value': 'PC3,PC4'}
        ],
        value='PC1,PC2'
    ),
    dcc.Graph(
        id='cluster-pca'
    )
])


@app.callback(Output('cluster-pca', 'figure'),
              [Input('pca-dropdown', 'value')])
def update_cluster_graph(dropdown_value):
    first, second = dropdown_value.split(",")
    rayon = rayon_estimation(cluster, first, second)
    data = cluster_scatter(cluster, first, second)
    data += pca_arrow(pcafeatures, first, second, rayon, k=6)
    return {
        'data': data,
        'layout': go.Layout(
            xaxis={'title': "PC{}".format(first)},
            yaxis={'title': "PC{}".format(second)},
            width=800,
            height=500,
            # margin={'l': 100, 'b': 40, 't': 10, 'r': 10},
                    margin={'l': 30, 'b': 20, 't': 30, 'r': 20},
            # legend={'x': 0, 'y': 1},
                    hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
