from evennia import DefaultScript


class Timeline(DefaultScript):
    def __init__(self):
        """Timelines are persistent."""
        super().__init__()
        self.persistent = True
