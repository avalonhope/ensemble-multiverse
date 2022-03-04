"""
Faction Commands
Commands for managing factions
"""
import deal
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
        # create a new faction
        # make each part of name always start with capital letter
        name = self.args.strip().title()
        # search for an existing faction of the same name
        existing = utils.search.search_script(name)
        if len(existing) > 0:
            caller.msg("This faction name is already in use.")
            return
        # create faction
        faction = create_script("typeclasses.factions.Faction",
                                key=name,
                                locks="edit:id(%i) and perm(Builders);call:false()" % caller.id,
                                report_to=caller)
        faction.db.founder = caller
        faction.db.members = [caller.name]
        faction.db.leadership = [caller.name]
        faction.tags.add("faction")
        if caller.db.faction:
            faction.db.superfaction = caller.db.faction
        caller.db.faction = faction
        caller.msg("You founded the faction called: %s." % faction.name)
        

class CmdFactions(Command):
    """
    show lists of factions
    Usage:
      +factions
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
            if faction.db.founder:
                self.caller.msg(faction.name + " founded by " + faction.db.founder.name)
            else:
                self.caller.msg(faction.name)
            if faction.db.superfaction:
                self.caller.msg(" a subfaction of " + faction.db.superfaction.name)
        
 
class CmdFactionClaim(Command):
    """
    associates your faction with this location, if not already taken
    Usage:
      +factionclaim
    This calims this location for your faction
    """
    
    key = "+factionclaim"
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        caller = self.caller
        location = caller.location
        if location.db.faction:
            caller.msg("This location is already claimed by " + location.db.faction.name)
            return
        if caller.db.faction is None:
            caller.msg("You do not belong to a faction yet.")
            return
        location.db.faction = caller.db.faction
        if location.db.level is None:
            caller.db.reputation += 1
        else:
            caller.db.reputation += 2 ** location.db.level
        caller.msg(location.name + " is now claimed by " + location.db.faction.name)
        location.msg("This located is now claimed by " + location.db.faction.name)
        return
    
