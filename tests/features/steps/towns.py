from behave import given, when, then


@then("a list of zones within the town is shown")
def zones(context):
    pass


@when("the roads command is used")
def roads(context):
    pass


@then("a list of roads out of town is shown")
def show_roads(context):
    pass


@given("a charcater is located within a town")
def in_town(context):
    pass


@given("the charcater is onboard a vehicle")
def in_vehicle(context):
    pass


@given("the charcater has control of the vehicle")
def driving_vehice(context):
    pass


@when("the travel command is used")
def travel(context):
    pass


@when("a road is specified")
def choose_road(context):
    pass


@then("the vehicle enters that road")
def check_vehicle_on_road(context):
    pass
