#%%
from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from shapely.geometry import Point
import geopandas as gpd
import pandas as pd


base_dir = Path(__file__).resolve().parent.parent.parent
raw_data_path = base_dir/"data"/"data_set.csv"
gdf_data_path = base_dir/"data"/"data_set.gpkg"


# df_data = pd.read_csv(raw_data_path)

# gdf_data = gpd.GeoDataFrame(
#     data =      df_data,
#     geometry = gpd.points_from_xy(df_data['x'],df_data["y"]),
#     crs =     "EPSG:4326"
# )

# gdf_data.to_file(filename= gdf_data_path, driver= "GPKG")

# gpd.read_file(filename=gdf_data_path)

@dataclass
class WellData:
    raw_data:Path # Optional: if they want to save a .gpkg cache)
    cache_path: Path | None = None  # Optional: if they want to save a .gpkg cache
    gdf_data:gpd.GeoDataFrame | None = None # This will hold the data in memory after conversion

    def load_and_convert(self):
        """This method take a CSV file and convert it to GeoDataFrame file
            After checking file and converting it,this method load it into MapPlotter class
        """
        # Reading the raw csv data
        if not self.raw_data.exists():
            raise FileNotFoundError(f"CSV file not found: {self.raw_data}")
        
        try:
            df_data = pd.read_csv(self.raw_data)
        except pd.errors.EmptyDataError:
                raise ValueError("CSV file is empty")
        
        if not {'x', 'y'}.issubset(df_data.columns):
            raise ValueError(f"CSV must contain 'x' and 'y' columns. Found: {df_data.columns.tolist()}")
            
        # Adding the geometry and crs
        gdf_data = gpd.GeoDataFrame(
            data =      df_data,
            geometry = gpd.points_from_xy(df_data['x'],df_data["y"]),
            crs =     "EPSG:4326"
        )

        # Updating the class variables
        self.gdf_data = gdf_data
        
        # If he want to save
        if self.cache_path is not None:
            gdf_data.to_file(filename= self.cache_path, driver= "GPKG")

        return self.gdf_data
                
    def load_from_cache(self) -> gpd.GeoDataFrame:
        """method to read the .gpkg if it already exists, so we don't have to re-convert the CSV every time
        Returns:
            gpd.GeoDataFrame: _description_
        """
        if self.cache_path is None:
            raise ValueError("No cache_path provided")
        if not self.cache_path.exists():
            raise FileNotFoundError(f"Cache file not found: {self.cache_path}")
        
        self.gdf_data = gpd.read_file(filename=self.cache_path)
        return self.gdf_data







    