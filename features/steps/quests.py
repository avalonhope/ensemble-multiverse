# type: ignore
from behave import *
from typeclasses.characters import Character

@given("a character exists")
def step_impl(context):
    """Create a test character."""
    context.character = Character()


@when("the quest command is used")
def step_impl(context):
    """Run the quest command."""


@then("a list of available quests is shown")
def setp_impl(context):
    """Check that a list of quests is shown."""
