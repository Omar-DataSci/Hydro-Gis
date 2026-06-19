from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict
import geopandas as gpd
from typing import Literal
from shapely.geometry import LineString

@dataclass
class ContourField:
    """ContourField class have field method to choose the type and interval
    """
    field:Literal["conductivity","piezo","elevation"]
    interval: int

    def plot(self)-> LineString:
        """This method plot the countour lines for the field

        Returns:
            _type_: LineString
        """
        pass
