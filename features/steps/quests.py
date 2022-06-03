# type: ignore
from behave import given, when, then
from world.characters import LeadCharacter
from world.quests import Quest


@given("a character exists")
def step_create_character(context):
    """Create a test character."""
    context.character = LeadCharacter()


@given("a quest exists")
def step_create_quest(context):
    """Create a quest."""
    context.quest = Quest()


@when("the {command_name} command is used")
def step_call_commands(context):
    """Run the command."""
    context.list_of_quests = context.character.command(command_name)


@then("a list of available quests is shown")
def step_check_list_of_quests(context):
    """Check that a list of quests is shown."""
    if context.list_of_quests is None:
        raise AssertionError
