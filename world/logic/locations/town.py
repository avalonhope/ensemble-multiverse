class Road:
    """A transport link that connects two or more locations."""


class Town:
    """A settlement within a region."""
    
    def __init__(self, first_zone):
        """Create a new town."""
        self.zones = [first_zone]

    def search_roads(self):
        """List all the roads connected to this town."""

    def search_zones(self):
        """List all the zones within this town."""
        return self.zones
    
class Zone:
    """A zone within a town."""
