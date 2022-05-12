from behave import *
from typeclasses import accounts
from commands import quest
from evennia.utils.create import create_object


@given("a new character has been created")
def step_impl(context):
  test_account = accounts.create("username","password")
  test_charcater = test_account.create_character()
  
  
@when("the quest command is used")
def step_impl(context):
   pass
  
  
@then("a list of quests is shown")
def setp_impl(context):
  pass
