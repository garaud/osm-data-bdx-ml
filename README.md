## Évaluation de la qualité de la donnée OpenStreetMap

Code, data et notebooks.

Bordeaux Machine Learning Meetup
https://www.meetup.com/Bordeaux-Machine-Learning-Meetup/events/257919300/

## how to : 

`
pip install -e .
`

```python
# Load variable in config.py
from explorer.config import *

# read data
centroid = pd.read_hdf(CLUSTER_FILE, "/centroids")

centroid.head()
```

## data

Résultats produits avec l'historique de données OpenStreetMap dans une région donnée
via le code
[osm-data-classification](https://github.com/Oslandia/osm-data-classification/)

Pour les données en base :

* Fichier `pbf` de la région étudiée (données OSM récentes) à mettre en base Postgres
  avec `osm2pgsql`
* Dump de quelques CSV issues de l'analyse en base pour croiser les données,
  i.e. récupérer la géométrie de certaines entités OSM et les visualiser sur une carte
