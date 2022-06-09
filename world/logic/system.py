import icontract
from evennia.utils.search import search_script_tag


class System:
    """Workflow and Business Logic system for Starquest - Infinite Worlds."""

    @icontract.ensure(lambda result: result is True)
    def active(self):
        """System integrity status."""
        return True

    def quests(self):
        """List of available quests."""
        # show list of factions
        quests = search_script_tag("quest")
        return [quest.name for quest in quests]
