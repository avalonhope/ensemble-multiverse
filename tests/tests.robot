*** Settings ***
Documentation     Starquest - Infinite Worlds
Library           OperatingSystem

*** Test Cases ***

Directory Structure Test
  Should Be True  True
  Directory Should Exist  world
  Directory Should Exist  world/logic
  Directory Should Exist  commands
  Directory Should Exist  typeclasses
  Directory Should Exist  server
  Directory Should Exist  tests
  Directory Should Exist  tests/features
  Directory Should Exist  tests/features/steps
