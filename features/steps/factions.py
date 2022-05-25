from behave import given, when, then
from world import actions, characters, factions


@given(u'we have a faction A')
def step_impl(context):
    context.faction_A = factions.Faction()


@given(u'we have a character C')
def step_impl(context):
    context.character_C = characters.Character()


@given(u'C is a member of faction A')
def step_impl(context):
    context.character_C.faction = context.faction_A


@given(u'we have another faction B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have another faction B')
    conext.faction_B = factions.Faction()


@given(u'faction B is not a subfaction of A')
def step_impl(context):
    context.faction_B.superfactions = None


@given(u'faction A is not a subfaction of B')
def step_impl(context):
    context.faction_B.superfactions = None


@when(u'C asks to join faction B')
def step_impl(context):
    context.result = actions.join_faction(context.character_C, context.faction_B)


@then(u'C is not allowed to join faction B')
def step_impl(context):
    if not context.result:
        raise AssertionError

