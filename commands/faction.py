"""
Faction Commands
Commands for managing factions
"""

from commands.command import Command

class CmdFactionCreate(Command):
    """
    create faction
    Usage:
      +factioncreate <action>
    This creates a new faction
    """
    
    key = "+factioncreate"
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        errmsg = "You must supply a valid string."
        if not self.args:
            self.caller.msg(errmsg)
            return
        try:
            name = str(self.args.strip())
        except ValueError:
            self.caller.msg(errmsg)
            return
        
        caller = self.caller
        if caller.db.faction:
          caller.msg("You already belong to %s." caller.db.faction.name)
          return
        # create a new faction
        pass
        

class CmdFactions(Command):
    """
    show lists of factions
    Usage:
      +history
    This emits a message about the roleplaying history.
    """
    
    key = "+factions"
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        # show list of factions
        pass
        
 
