class Quest:
    """Quests are multi-user interactive stories."""

    def __init__(self, name=""):
        """The beginning of the story."""
        self.participants = []
        self.name = name

    def list_participants(self):
        """List of participants."""
        return self.participants

    def add_participant(self, character):
        """Add character to the list of participants."""
        self.participants.append(character)
        return f"{character.name} has joined the {self.name} quest."
