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


DATADIR = Path("/home/dag/data/osland-ia/output-extracts/last-large-bordeaux-metropole")

OSM_ELEMENT_FILE = DATADIR / 'element-metadata.csv'
OSM_USER_FILE = DATADIR / 'user-metadata-extra.csv'
# luigi process automatically select 5 groups for the cluster
CLUSTER_FILE = DATADIR / "user-metadata-pca-auto-clusters-5-kmeans.h5"
PCA_FILE = DATADIR / 'user-metadata-auto-n_components-min-3-max-12-pca.h5'


def scatter(data, first, second):
    """list of scatter

    users : DataFrame
    first : first component
    second : second component
    """
    cluster_id = data["Xclust"].unique().tolist()
    cluster_id.sort()
    return [
        go.Scatter(
            x=data.query("Xclust == @idc")[first],
            y=data.query("Xclust == @idc")[second],
            text=f"cluster: {idc}",
            mode="markers",
            opacity = 0.7,
            marker={
                'size': 10,
                'line': {'width': 0.25, 'color': 'white'}
            },
            name=str(idc)
        ) for idc in cluster_id]


if __name__ == '__main__':
    print("read files")
    print("  - csv files")
    # element = pd.read_csv(str(OSM_ELEMENT_FILE), index_col=0)
    # users = pd.read_csv(str(OSM_USER_FILE))

    print("  - " + CLUSTER_FILE.name)
    centroid = pd.read_hdf(CLUSTER_FILE, "/centroids")
    cluster = pd.read_hdf(CLUSTER_FILE, "/individuals")
    print("  - " + PCA_FILE.name)
    pcafeatures = pd.read_hdf(PCA_FILE, "/features")
    pcaind = pd.read_hdf(PCA_FILE, "/individuals")


    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    f1 = "n_relation_modif_imp"
    f2 = "n_activity_days"
    f3 = "u_way_modif"

    # print(pcafeatures.loc[f1])
    # print(pcafeatures.loc[f1][["PCA1", "PCA2"]])

    anno1 = dict(x=0, y=0,
                 xref="x", yref="y",
                 showarrow=True,
                 text=f1,
                 arrowhead=2,
                 arrowsize=1,
                 arrowwidth=2,
                 arrowcolor='#636363',
                 ax=pcafeatures.loc[f1]["PC1"]*5,
                 ay=pcafeatures.loc[f1]["PC2"]*5
    )

    anno2 = dict(x=0, y=0,
                 xref="x", yref="y",
                 showarrow=True,
                 text=f2,
                 arrowhead=2,
                 arrowsize=1,
                 arrowwidth=2,
                 arrowcolor='#636363',
                 ax=pcafeatures.loc[f2]["PC1"],
                 ay=pcafeatures.loc[f2]["PC2"]
    )

    app.layout = html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure={
                'data': scatter(cluster, "PC1", "PC2"),
                'layout': go.Layout(
                    xaxis={'title': 'PC1'},
                    yaxis={'title': 'PC2'},
                    width=600,
                    height=500,
                    annotations=[anno1, anno2],
                    margin={'l': 100, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])

    app.run_server(debug=True)
