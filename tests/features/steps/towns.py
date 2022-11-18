from behave import given, when, then
from world.logic.locations.town import Road, Town, Zone  # type: ignore
from world.logic.characters import Character  # type: ignore
from world.logic.mobile import Vehicle  # type: ignore
from world.logic.commands import TravelCommand  # type: ignore


@when("the zones command is used")
def get_zones(context):
    """Get list of zones for this town."""
    context.town_zones = context.town.search_zones()


@then("a list of zones within the town is shown")
def list_zones(context):
    """Check list of zones for this town."""
    if context.town_zones is None:
        raise AssertionError("No town zones found; there should be at least one.")


@when("the roads command is used")
def roads(context):
    """Get list of roads leading to or from this town."""
    context.town_roads = context.town.search_roads()


@then("a list of roads out of town is shown")
def show_roads(context):
    """Check list of roads for this town."""
    if context.town_roads is None:
        raise AssertionError("No roads are connected with this town.")


@given("a character is located within a town")
def in_town(context):
    """Create a test town."""
    context.town = Town(Zone())
    context.character = Character()


@given("the character is onboard a vehicle")
def in_vehicle(context):
    """Create a test vehicle."""
    context.vehicle = Vehicle()


@given("the character has control of the vehicle")
def driving_vehice(context):
    """Set the driver of the vehicle."""
    context.vehicle.set_driver(context.character)


@when("the travel command is used")
def travel(context):
    """Set the command context."""
    context.command = TravelCommand


@when("a road is specified")
def choose_road(context):
    """Create a test road."""
    context.road = Road()


@then("the vehicle enters that road")
def check_vehicle_on_road(context):
    """Check vehicle is on the road."""
    if context.vehicle.road_location != context.road:
        raise AssertionError("Vehicle is not on the expected road.")
