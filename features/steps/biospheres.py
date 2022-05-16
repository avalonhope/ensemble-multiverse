from behave import *

from world import biospheres, planets

@given("the planet has an atmosphere")
def step_impl(context):
  context.planet = planets.Planet()
  context.planet.atmosphere = planets.Atmosphere()
  
