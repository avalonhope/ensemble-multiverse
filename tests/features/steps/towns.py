from behave import given, when, then

@then(u'a list of zones within the town is shown')
def zones(context):
    context.zones = context.town.zones()

@when(u'the roads command is used')
def roads(context):
    context.roads = context.town.roads()


@then(u'a list of roads out of town is shown')
def show_roads(context):
    if context.roads is None:
        raise AssertionError("Roads not found.")

@given(u'a charcater is located within a town')
def intown(context):
    context.character.town = context.town


@given(u'the charcater is onboard a vehicle')
def invehicle(context):
    


@given(u'the charcater has control of the vehicle')
def driving(context):
    raise NotImplementedError(u'STEP: Given the charcater has control of the vehicle')


@when(u'the travel command is used')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the travel command is used')


@when(u'a road is specified')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a road is specified')


@then(u'the vehicle enters that road')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the vehicle enters that road')
