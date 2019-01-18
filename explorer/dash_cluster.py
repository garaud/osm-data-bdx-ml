"""Scatter plot for user and the related clusters
"""

from pathlib import Path

import pandas as pd

import seaborn as sns

import plotly.plotly as py
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html

from data import read_pca, read_cluster, cluster_scatter, pca_arrow, rayon_estimation


if __name__ == '__main__':
    print("read files")
    centroid, cluster = read_cluster()
    pcafeatures, pcaind = read_pca()

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    # PC1, PC2
    # first, second = 1, 2
    first, second = 1, 3
    rayon = rayon_estimation(cluster, first, second)
    data = cluster_scatter(cluster, first, second)
    data += pca_arrow(pcafeatures, first, second, rayon, k=8)

    app.layout = html.Div([
        dcc.Graph(
            id='cluster-pca',
            figure={
                'data': data,
                'layout': go.Layout(
                    xaxis={'title': first},
                    yaxis={'title': second},
                    width=800,
                    height=500,
                    margin={'l': 100, 'b': 40, 't': 10, 'r': 10},
                    # legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])

    app.run_server(debug=True)
