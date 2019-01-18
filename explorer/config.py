import os
from pathlib import Path

# Paths
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATADIR = Path(ROOT_DIR + '/data/')

OSM_ELEMENT_FILE = DATADIR / 'element-metadata.csv'
OSM_USER_FILE = DATADIR / 'user-metadata-extra.csv'
# luigi process automatically select 5 groups for the cluster
CLUSTER_FILE = DATADIR / "user-metadata-pca-auto-clusters-5-kmeans.h5"
PCA_FILE = DATADIR / 'user-metadata-auto-n_components-min-3-max-12-pca.h5'
