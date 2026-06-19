#%%
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict
import geopandas as gpd
from shapely.geometry import Point

filename="data_set.csv"
with open(filename,mode="r", encoding="utf-8") as file:
    for line in file:
        print(line)
        



@dataclass
class WellData:
    csv_file:Path
    geoseries_file:gpd.GeoSeries

    def convert(self):
        """This method take a csv file and convert it to geo-series file
        """
        pass

    def load(self):
        """After checking file and converting it,this method load it into MapPlotter class
        """
        pass

    