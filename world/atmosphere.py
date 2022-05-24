from enum import Enum


class Layers(Enum):
    """Athmospheric Layers (Regions)."""
    # https://www.nasa.gov/mission_pages/sunearth/science/atmosphere-layers2.html
    TROPOSPHERE = 0
    STRATOSPHERE = 1
    MESOSPHERE = 2
    THERMOSPHERE = 3
    EXOSPHERE = 5
