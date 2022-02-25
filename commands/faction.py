"""
Faction Commands
Commands for managing factions
"""

import evennia

from commands.command import Command
from evennia import create_object, create_script, utils

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
        faction = create_script("typeclasses.factions.Faction",
                                key=name,
                                locks="edit:id(%i) and perm(Builders);call:false()" % caller.id,
                                report_to=caller)
        faction.db.founder = caller
        faction.db.members = [caller.name]
        faction.db.leadership = [caller.name]
        faction.tags.add("faction")
        caller.db.faction = faction
        caller.msg("You founded the faction called: %s." % faction.name)
        

class CmdFactions(Command):
    """
    show lists of factions
    Usage:
      +history
    This shows a list of faction names
    """
    
    key = "+factions"
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        # show list of factions
        factions = utils.search.search_script_tag("faction")
        self.caller.msg("There are %d factions:" % len(factions))
        for faction in factions:
            self.caller.msg(faction.name + " founded by " + faction.db.founder.name)
        
 
