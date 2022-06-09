import icontract


class System:
    """Workflow and Business Logic system for Starquest - Infinite Worlds."""

    def __init__(self):
        """The Beginning."""
        self.list_of_quests = []

    @icontract.ensure(lambda result: result is True)
    def active(self):
        """System integrity status."""
        return True

    def quests(self):
        """List of available quests."""
        return self.list_of_quests
