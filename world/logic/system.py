import icontract


class System:
    """Workflow and Business Logic system for Starquest - Infinite Worlds."""

    @icontract.ensures(lambda result: result is True)
    def active(self):
        """System integrity status."""
        return True
