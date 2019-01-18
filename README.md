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
