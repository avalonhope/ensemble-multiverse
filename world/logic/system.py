import icontract
from server.conf.settings import QUESTS


class System:
    """Workflow and Business Logic system for Starquest - Infinite Worlds."""

    def __init__(self):
        """The Beginning."""
        self.quests = QUESTS

    @icontract.ensure(lambda result: result is True)
    def active(self):
        """System integrity status."""
        return True

    def quests(self):
        """List of available quests."""
        return self.quests
