import unittest
  
from evennia.commands.default.tests import CommandTest

from commands.faction import CmdFactionClaim
from typeclasses.characters import Character
from typeclasses.rooms import Room

class TestFactionClaim(CommandTest):
  
  character_typeclass = Character
  room_typeclass = Room
  
  def test_unclaimed_room(self):
    # create an empty room
    # create a character
    # create a faction
    # claim the room for that faction
    # self.call(CmdFactionClaim)
    # check that the room is now claimed by this faction
    # check the increase in reputation for this character
    pass
    
 def test_dispute_claim(self)
    # create an empty room
    # create a character and faction
    # claim the room
    # claim another character and faction
    # increase reputation for first character
    # second character claims room unsuccessfully
    # increase reputation for second character
    # second character claims room successfully
    pass
    
