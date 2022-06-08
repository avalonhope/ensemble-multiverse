import icontract


class System:
    """Workflow and Business Logic system for Starquest - Infinite Worlds."""

    @icontract.ensure(lambda result: result is True)
    def active(self):
        """System integrity status."""
        return True
