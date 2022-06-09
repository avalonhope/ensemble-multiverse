from world.logic.system import System as LogicSystem
import icontract


class LeadCharacter:
    """Leading character for a quest party."""

    def __init__(self, name=""):
        """Lead character for a quest party."""
        self.system = LogicSystem()
        self.name = name

    @icontract.require(lambda command_name: command_name is not None)
    def command(self, command_name: str, target=None):
        """Execute a command on this character or party."""
        this_command = command_name.lower()
        if this_command == "quests":
            result = self.system.quests()
        elif this_command == "joinquest" and target is not None:
            result = target.add_participant(self)
        else:
            result = None
        return result
