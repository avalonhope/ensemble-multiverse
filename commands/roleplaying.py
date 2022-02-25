"""
Roleplaying Commands

Commands for roleplaying actions and events
"""

from commands.command import Command

class CmdDo(Command):
    """
    roleplay an action

    Usage:
      +do <action>

    This emits a message about the roleplaying action.
    """
    
    key = "+do"
    aliases = ["+action", "+roleplay"]
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        errmsg = "You must supply a valid string."
        if not self.args:
            self.caller.msg(errmsg)
            return
        try:
            action = str(self.args.strip())
        except ValueError:
            self.caller.msg(errmsg)
            return
        
        self.caller.msg("You %s." % action)
        self.caller.location.msg(self.caller.name + " " + action)
        self.caller.location.db.events.append(self.caller.name + " " + action)
        

class CmdHistory(Command):
    """
    show lists of roleplaying events

    Usage:
      +history

    This emits a message about the roleplaying history.
    """
    
    key = "+history"
    aliases = ["+events", "+journal"]
    help_category = "roleplaying"

    def func(self):
        "This performs the actual command"
        for event in self.caller.location.db.events:
            self.caller.msg(event)
        
