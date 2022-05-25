import icontract

from world import characters, factions

@icontract.require(lambda character: character is not None)
@icontract.require(lambda faction: faction is not None)
def join_faction(character: characters.Character, faction: factions.Faction):
  """A character asks to join a faction."""
  if character.faction() is faction:
    return True
  if character.faction() is None or faction.subfaction(character.faction()):
    character.set_faction(faction)
    return True
  return False
