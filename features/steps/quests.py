# type: ignore
from behave import given, when, then
from world.characters import Character


@given("a character exists")
def step_create_character(context):
    """Create a test character."""
    context.character = Character()


@when("the quests command is used")
def step_call_quests_commands(context):
    """Run the quests command."""


@then("a list of available quests is shown")
def step_list_of_quests(context):
    """Check that a list of quests is shown."""
