from system import System as LogicSystem
import icontract

class LeadCharacter:
    """Leading character for a quest party."""
    
    def __init__(self):
        """Lead character for a quest party."""
        self.system = LogicSystem()

    @icontract.require(lambda command_name: command_name is not None)
    def command(self, command_name: str):
        """Execute a command on this character or party."""
        this_command = command_name.lower()
        if this_command == "quests":
            result = self.system.quests()
        else:
            result = None
        return result
