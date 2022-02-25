"""
Faction Commands
Commands for managing factions
"""

import evennia

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
          caller.msg("You already belong to %s." % caller.db.faction.name)
          return
        # create a new faction
        # make each part of name always start with capital letter
        name = self.args.strip().title()
        # create faction
        faction = create_object("factions.Faction",
                                key=name,
                                locks="edit:id(%i) and perm(Builders);call:false()" % caller.id)
        faction.db.founder = caller
        faction.db.members = [caller.name]
        faction.db.leadership = [caller.name]
        faction.tags.add("faction")
        caller.msg("You founded the faction called: %s." % faction.name)
        

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
        factions = evennia.search_tag("faction")
        for faction in factions:
            self.caller.msg(faction.name)
        
 
