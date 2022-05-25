import icontract

import world.characters
import world.factions

@icontract.requires(character is not None)
@icontract.requires(faction is not None)
def join_faction(character, faction):
  """A character asks to join a faction."""
  if character.faction() is faction:
    return True
  if character.faction() is None or faction.subfaction(character.faction()):
    character.set_faction(faction)
    return True
  return False
