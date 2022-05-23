import icontract
from typeclasses.factions import Faction
from typeclasses.characters import Character

@icontract.requires(character is not None)
@icontract.requires(faction is not None)
def join_faction(character, faction):
