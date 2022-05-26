lines (27 sloc) 1.03 KB
import behave
from world import actions, characters, factions


@behave.given(u'we have a faction A')
def step_impl(context):
    context.faction_A = factions.Faction()


@behave.given(u'we have a character C')
def step_impl(context):
    context.character_C = characters.Character()


@behave.given(u'C is a member of faction A')
def step_impl(context):
    context.character_C.faction = context.faction_A


@behave.given(u'we have another faction B')
def step_impl(context):
    context.faction_B = factions.Faction()


@behave.given(u'faction B is not a subfaction of A')
def step_impl(context):
    context.faction_B.superfactions = None


@behave.given(u'faction A is not a subfaction of B')
def step_impl(context):
    context.faction_B.superfactions = None


@behave.when(u'C asks to join faction B')
def step_impl(context):
    context.result = actions.join_faction(context.character_C, context.faction_B)


@behave.then(u'C is not allowed to join faction B')
def step_impl(context):
    if context.result is True:
        raise AssertionError
