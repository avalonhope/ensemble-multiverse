class Vehicle:
    """An entity that may move between locations and may contain passengers and cargo."""

    self.road_location = None
    self.driver = None

    def set_driver(self, driver):
        """Assign a character as driver of this vehicle."""
        self.driver = driver

    def select_road(self, road):
        """Move the vehicle onto a road."""
        self.road_location = road
