"""Pour lire & préparer la données à visualiser
"""

import math
from pathlib import Path

import numpy as np
import pandas as pd

import plotly.graph_objs as go

from explorer.config import CLUSTER_FILE, PCA_FILE


def read_pca():
    print(" read PCA " + PCA_FILE.name)
    features = pd.read_hdf(PCA_FILE, "/features")
    ind = pd.read_hdf(PCA_FILE, "/individuals")
    return features, ind


def read_cluster():
    print(" read cluster " + CLUSTER_FILE.name)
    centroid = pd.read_hdf(CLUSTER_FILE, "/centroids")
    cluster = pd.read_hdf(CLUSTER_FILE, "/individuals")
    return centroid, cluster


def pca_highest_features(pca_features, first, second, k):
    """Prend les 5 features de PCx, PCy les plus importantes
    """
    df = pca_features[[first, second]]
    # on calcule la norm 2
    norm = df[first]**2 + df[second] ** 2
    norm = norm.sort_values(ascending=False)
    return norm.iloc[:k].index.tolist()


def cluster_scatter(data, first, second):
    """list of scatter

    users : DataFrame
    first : first component
    second : second component
e
    """
    cluster_id = data["Xclust"].unique().tolist()
    cluster_id.sort()
    return [
        go.Scatter(
            x=data.query("Xclust == @idc")[first],
            y=data.query("Xclust == @idc")[second],
            text="cluster: "+str(idc),
            mode="markers",
            opacity = 0.7,
            marker={
                'size': 10,
                'line': {'width': 0.25, 'color': 'white'}
            },
            name=str(idc)
        ) for idc in cluster_id]


def rayon_estimation(cluster, first, second):
    stats = np.sqrt(cluster[first]**2 + cluster[second]**2).describe()
    return stats['75%']
    # return np.sqrt(cluster[first]**2 + cluster[second]**2).mean()


def pca_arrow(pca_features, first="PC1", second="PC2", rayon=1, k=5):
    names = pca_highest_features(pca_features, first, second, k)
    result = [ ]
    for name in names:
        x, y = pca_features.loc[name, [first, second]].tolist()
        r = x**2 + y**2
        x = math.sqrt(rayon**2 / r) * x
        y = math.sqrt(rayon**2 / r) * y
        result.append(
            go.Scatter(
                x=[0, x],
                y=[0, y],
                mode="lines + markers + text",
                text=['', name],
                textposition='top center',
                name=name,
                # marker=dict(symbol=9, size=12)
                marker=dict(symbol=24, size=7, color="#666666")
            )
        )
    return result


if __name__ == '__main__':
    centroid, cluster = read_cluster()
    pcafeatures, pcaind = read_pca()
