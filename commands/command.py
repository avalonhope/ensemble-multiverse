"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import create_object
from evennia.commands.command import Command as BaseCommand
from world.skills import proficiency

# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns anything truthy, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """

    pass


# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super().has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None

class CmdSetRace(Command):
    """
    set the race of a character

    Usage:
      +setrace <race>

    This sets the race of the current character. This can only be
    used during character generation.
    """
    
    key = "+setrace"
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        errmsg = "You must supply a valid string."
        if not self.args:
            self.caller.msg(errmsg)
            return
        try:
            race = str(self.args)
        except ValueError:
            self.caller.msg(errmsg)
            return
        
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.race = race
        self.caller.msg("Your Race was set to %s." % race)

class CmdTrainSkill(Command):
    """
    improve the skill of a character

    Usage:
      +trainskill <skill> 

    This trains the skills of the current character. This can only be
    used in a training room.
    """
    
    key = "+trainskill"
    help_category = "skills"

    def func(self):
        "This performs the actual command"
        if self.caller.db.energy <= 0:
            self.caller.msg("You are too tired to train. You need to rest.")
            return
        errmsg = "You must supply a valid skillname."
        if not self.args:
            self.caller.msg(errmsg)
            return
        try:
            if self.args == " strength":
                if self.caller.db.strength is None:
                    self.caller.db.strength = 0
                self.caller.db.strength += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg("Your proficency is now %.2f." % proficiency(self.caller.db.strength))
            elif self.args == " agility":
                if self.caller.db.agility is None:
                    self.caller.db.agility = 0
                self.caller.db.agility += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg("Your proficency is now %.2f." % proficiency(self.caller.db.agility))
            elif self.args == " speed":
                if self.caller.db.speed is None:
                    self.caller.db.speed = 0
                else:
                    self.caller.db.speed += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg("Your proficency is now %.2f." % proficiency(self.caller.db.speed))
           elif self.args == " stamina":
                if self.caller.db.stamina is None:
                    self.caller.db.stamina = 0
                else:
                    self.caller.db.stamina += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg("Your proficency is now %.2f." % proficiency(self.caller.db.speed))
            elif self.args == " mindshield":
                if self.caller.db.mindshield is None:
                    self.caller.db.mindshield = 0
                else:
                    self.caller.db.mindshield += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg("Your proficency is now %.2f." % proficiency(self.caller.db.speed))
            elif self.args == " mindmeld":
                if self.caller.db.mindmeld is None:
                    self.caller.db.mindmeld = 0
                else:
                    self.caller.db.mindmeld += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg("Your proficency is now %.2f." % proficiency(self.caller.db.speed))
            else:
                self.caller.msg("%s skill cannot be trained (yet)." % self.args)

        except ValueError:
            self.caller.msg(errmsg)
            return
        
        return

    
class CmdRecruitCompanion(Command):
    """
    create a new companion and add to party

    Usage:
        +recruitCompanion <name>

    Creates a new, named companion.
    """
    key = "+receruitcompanion"
    aliases = ["+recruitCompanion"]
    locks = "call:not perm(nocompanions)"
    help_category = "party"
    
    def func(self):
        "creates the object and names it"
        caller = self.caller
        if not self.args:
            caller.msg("Usage: +recruitCompanion <name>")
            return
        if not caller.location:
            # may not create companion when OOC
            caller.msg("You must have a location to recruit a companion.")
            return
        # make each part of name always start with capital letter
        name = self.args.strip().title()
        # create companion in caller's location
        companion = create_object("characters.Character",
                      key=name,
                      location=caller.location,
                      locks="edit:id(%i) and perm(Builders);call:false()" % caller.id)
        # add to party
        companion.db.party = caller.id
        # announce
        message = "%s recruited '%s'."
        caller.msg(message % ("You", name))
        caller.location.msg_contents(message % (caller.key, name),
                                                exclude=caller)
        
class CmdMeditate(Command):
    """
    enter inner world

    Usage:
        +meditate

    Moves character into inner world
    """
    key = "+meditate"
    aliases = ["+meditation"]
    locks = "call: perm(innerworld)"
    help_category = "inner world"
    
    def func(self):
        "moves to inner world"
        caller = self.caller
        # comsume some energy
        if caller.db.energy < MEDITATION_COST:
            caller.msg("You are too tired. You need to rest.")
            return
        caller.db.energy -= MEDITATION_COST
        # gain experience and improve mental defenses
        caller.db.mindshield += MINDSHIELD_GAIN
        # create empty inner world if needed
        if not caller.db.innerWorld:
            caller.db.innerWorld = create_object("typeclasses.innerworld.Home", key = "Inner World")
        if not caller.location:
            # may not meditate when OOC
            caller.msg("You must have a location to begin meditation.")
            return
        if caller.db.in_medidation:
            caller.msg("You continue to meditate.")
            return
        caller.db.in_meditation = True
        caller.db.outerWorld = caller.location
        caller.location = caller.db.innerWorld
        caller.msg("You close your eyes and visualize your inner world.")
        
class CmdAwaken(Command):
    """
    leave inner world
    Usage:
        +awaken
    Moves charcater back into outer world
    """
    key = "+awaken"
    aliases = ["+awaken"]
    locks = "call: perm(innerworld)"
    help_category = "inner world"
    
    def func(self):
        "moves to outer world"
        caller = self.caller
        caller.db.in_meditation = false
        caller.location = caller.db.outerWorld
        caller.msg("You leave your inner world and return to the outer world.")
        
class CmdRest(Command):
    """
    restore energy
    Usage:
        +rest
    rest until maximum energy is reached
    """
    key = "+rest"
    aliases = ["+sleep"]
    locks = ""
    help_category = "general"
    
    def func(self):
        "recover energy"
        caller = self.caller
        if caller.db.resting = True:
            caller.msg("You continue resting")
            return
        maximum_energy = int(caller.db.health * proficency(caller.db.stamina))
        amount_to_recover = maximum_energy - self.db.energy
        if amount_to_recover <= 0:
            self.caller.msg("You are fully rested.")
        time_to_recover = RECOVERY_RATE * amount_to_recover
        caller.db.resting = True
        utils.delay(time_to_recover, self.recover)
        caller.msg("You begin resting.")
        
    def recover(self):
        "This will be called when fully recovered"
        caller = self.caller
        caller.db.resting = False
        self.db.energy = int(caller.db.health * proficency(caller.db.stamina))
        self.caller.msg("You are fully rested now.")
        
