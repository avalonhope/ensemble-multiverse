"""
Faction Commands
Commands for managing factions
"""
import deal
import evennia

from commands.command import Command
from evennia import create_object, create_script, utils
from world.factions import subfaction

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
        faction.db.leader = caller
        caller.tags.add(faction.name, category="faction")
        faction.tags.add("faction")
        if caller.db.faction:
            faction.db.superfaction = caller.db.faction
        caller.db.faction = faction
        # shared inner world by which faction members may communicate and interact
        faction.db.innerWorld = create_object("typeclasses.innerworld.Home", key = "Inner World of %s" % faction.name)
        faction.db.innerWorld.tags.add("Inner World")
        faction.db.innerWorld.db.faction = faction
        faction.db.innerWorld.tags.add(faction.name, category="faction")
        # announce
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
            if faction.db.leader:
                self.caller.msg(faction.name + " led by " + faction.db.leader.name)
            else:
                self.caller.msg(faction.name)
            if faction.db.superfaction:
                self.caller.msg(" a subfaction of " + faction.db.superfaction.name)
                
        if self.caller.db.faction:
            self.caller.msg("You are a member of " + self.caller.db.faction.name)
        else:
            self.caller.msg("You do not yet belong to any faction.")
        return
        
 
class CmdFactionClaim(Command):
    """
    associates your faction with this location, if not already taken
    Usage:
      +factionclaim
    Associate this location with your faction
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
        faction = caller.db.faction
        location.tags.add(faction.name, category="faction")
        if location.db.level is None:
            caller.db.reputation += 1
        else:
            caller.db.reputation += 2 ** int(location.db.level)
        if faction.db.leader is None or caller.db.reputation > faction.db.leader.db.reputation:
            faction.db.leader = caller
            caller.msg("You are now the faction leader.")
        caller.msg(location.name + " is now claimed by " + location.db.faction.name)
        location.msg("This located is now claimed by " + location.db.faction.name)
        return
 
class CmdFactionJoin(Command):
    """
    Join the local faction or subfaction
    Usage:
      +factionjoin
    This adds you to the local faction
    """
    
    key = "+factionjoin"
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        caller = self.caller
        location = caller.location
        if location.db.faction is None:
            caller.msg("There is no local faction to join. You must find the right location.")
            return
        faction = location.db.faction
        if caller.db.faction is None or subfaction(faction, caller.db.faction):
            caller.db.faction = faction
            caller.tags.add(faction.name, category="faction")
            if faction.db.leader is None or caller.db.reputation > faction.db.leader.db.reputation:
                faction.db.leader = caller
                caller.msg("You are now the leader of " + faction.name)
            else:
                caller.msg("You are now a member of " + faction.name)
        else:
            caller.msg("You already belong to " + caller.db.faction.name)
         
        return
    
class CmdFactionSpace(Command):
    """
    enter shared inner world of faction
    Usage:
      +factionspace
    Moves character into shared inner world of faction
    """
    key = "+factionspace"
    aliases = ["+factionworld"]
    help_category = "inner world"
    
    def func(self):
        "moves to inner world of faction"
        caller = self.caller
        if caller.db.faction is None:
            caller.msg("You do not yet belong to nay faction.")
            return
       faction = caller.db.faction
        # comsume some energy
        if not caller.db.energy or caller.db.energy < MEDITATION_COST or caller.db.resting:
            caller.msg("You are too tired. You need to rest.")
            return
        caller.db.energy -= MEDITATION_COST
        # gain experience and improve mental defenses
        if not caller.db.skills:
            caller.db.skills = {}
            caller.db.skills["mindshield"] = 0
        elif "mindshield" not in caller.db.skills.keys():
            caller.db.skills["mindshield"] = 0
        caller.db.skills["mindshield"] += MINDSHIELD_GAIN
        # create empty inner world if needed
        if not faction.db.innerWorld:
            faction.db.innerWorld = create_object("typeclasses.innerworld.Home", key = "Inner World of %s" % faction.name)
            faction.db.innerWorld.tags.add("Inner World")
            faction.db.innerWorld.tags.add(faction.name, category="faction")
            faction.db.innerWorld.db.faction = faction
        if not caller.location:
            # may not meditate when OOC
            caller.msg("You must have a location to begin meditation.")
            return
        if caller.db.in_medidation:
            caller.msg("You visualize the shared inner world of your faction.")
            caller.move_to(faction.db.innerWorld)
            return
        caller.db.in_meditation = True
        caller.db.outerWorld = caller.location
        caller.move_to(faction.db.innerWorld)
        caller.msg("You close your eyes and visualize the shared inner world of your faction.")

