from hydrogis.core.rendering.maps import BaseMap
from hydrogis.core.hydrology.contour import ContourField
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict
import geopandas as gpd
import folium

filename="data_set.csv"

@dataclass
class MapPlotter:
    """This class use folium to creates maps
    """
    base_map:BaseMap
    location:list[int]
    countour:ContourField

    def plot(self):
        pass
