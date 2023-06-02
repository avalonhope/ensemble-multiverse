"""
Timelines
"""

from evennia import DefaultScript


class Timeline(DefaultScript):
    """Timelines"""

    def __init__(self):
        """Timelines are persistent."""
        super().__init__()
        self.persistent = True
