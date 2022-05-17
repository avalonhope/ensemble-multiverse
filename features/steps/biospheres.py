from behave import *

from world import biospheres, planets

@given("there is a planet")
def step_impl(context):
    context.planet = planets.Planet()

@given("the planet has an atmosphere")
def step_impl(context):
  context.planet.atmosphere = planets.Atmosphere()
  
