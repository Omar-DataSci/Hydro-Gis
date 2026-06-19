from dataclasses import dataclass
from pathlib import Path
from typing import Literal

@dataclass
class BaseMap:
    tiles:Literal["osm","satellite"]
    zoom_start:int = 12
   