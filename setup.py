from setuptools import find_packages, setup

setup(
    name='osm-data-bdx-ml',
    packages=find_packages(),
    install_requires=["jupyter", "jupyter_contrib_nbextensions", "pandas", "geopandas", "table",
                      "dash", "plotly", "seaborn", "folium"],
    version='0.1.0',
    description="Bordeaux Machine Learning Meetup with OSM data",
    url="https://github.com/garaud/osm-data-bdx-ml",
    author='Damien Garaud & Armand Gilles',
    license='MIT',
)
