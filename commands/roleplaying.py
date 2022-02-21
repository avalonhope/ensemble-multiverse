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
        self.caller.location.msg("%s %s" % self.caller.name, action)
        self.caller.location.events.append("%s %s" % self.caller.name, action)
        
