class Quest:
    """Quests are multi-user interactive stories."""

    def __init__(self):
        """The beginning of the story."""
        self.participants = []

    def list_participants(self):
        """List of participants."""
        return self.participants

    def add_participant(self, character):
        """Add character to the list of participants."""
        self.participants.append(character)
