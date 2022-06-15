"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import create_object, utils
from evennia.commands.command import Command as BaseCommand
from world.logic.skills import proficiency  # type: ignore
from server.conf.settings import RECOVERY_RATE, SKILLS  # type: ignore


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


class CmdTrainSkill(Command):
    """
    improve the skill of a character

    Usage:
      +train <skill>

    This trains the skills of the current character. This can only be
    used in a training room.
    """

    key = "+train"
    aliases = ["+learn", "+study", "+improve"]
    help_category = "skills"

    def func(self):
        """This performs the actual command"."""
        if self.caller.db.energy <= 0 or self.caller.db.health <= 0:
            self.caller.msg("You are too tired to train. You need to rest.")
            return
        errmsg = "You must supply a valid skillname."
        if not self.args:
            self.caller.msg(errmsg)
            return
        try:
            skillname = self.args.strip().lower()
            if skillname == "strength":
                if self.caller.db.strength is None:
                    self.caller.db.strength = 0
                self.caller.db.strength += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg(
                    "Your strength level is now %.2f."
                    % proficiency(self.caller.db.strength)
                )
            elif skillname == "agility":
                if self.caller.db.agility is None:
                    self.caller.db.agility = 0
                self.caller.db.agility += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg(
                    "Your agility level is now %.2f."
                    % proficiency(self.caller.db.agility)
                )
            elif skillname == "speed":
                if self.caller.db.speed is None:
                    self.caller.db.speed = 0
                self.caller.db.speed += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg(
                    "Your speed level is now %.2f." % proficiency(self.caller.db.speed)
                )
            elif skillname == "stamina":
                if self.caller.db.stamina is None:
                    self.caller.db.stamina = 0
                self.caller.db.stamina += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg(
                    "Your stamina level is now %.2f."
                    % proficiency(self.caller.db.stamina)
                )
            elif skillname in SKILLS:
                if skillname not in self.caller.db.skills.keys():
                    self.caller.db.skills[skillname] = 0
                self.caller.db.skills[skillname] += self.caller.db.energy
                self.caller.db.energy = 0
                self.caller.msg(
                    "Your skill level is now %.2f."
                    % proficiency(self.caller.db.skills[skillname])
                )
            else:
                self.caller.msg("%s skill cannot be trained (yet)." % self.args)

        except ValueError:
            self.caller.msg(errmsg)
            return

        return


class CmdImagine(Command):
    """
    create a new imaginary companion and add to inner world

    Usage:
        +imagine <name>

    Creates a new, imaginary companion.
    """

    key = "+imagine"
    aliases = ["+thoughtform", "+tulpa"]
    help_category = "inner world"

    def func(self):
        """creates the object and names it"."""
        caller = self.caller
        if not self.args:
            caller.msg("Usage: +imagine <name>")
            return
        if not caller.db.innerWorld:
            # may not create companion without inner world
            caller.msg("You must meditate before creating imaginary companions.")
            return
        # make each part of name always start with capital letter
        name = self.args.strip().title()
        # create companion in Inner World
        companion = create_object(
            "characters.Tulpa",
            key=name,
            location=caller.db.innerWorld,
            locks="edit:id(%i) and perm(Builders);call:false()" % caller.id,
        )

        # add to faction
        if caller.db.faction is not None:
            faction = caller.db.faction
            companion.db.faction = faction
            companion.tags.add(faction.name, category="faction")
        # announce
        message = "%s imagined '%s'."
        caller.msg(message % ("You", name))
        caller.db.innerWorld.msg_contents(message % (caller.key, name), exclude=caller)


class CmdMeditate(Command):
    """
    enter inner world

    Usage:
        +meditate

    Moves character into inner world
    """

    key = "+meditate"
    aliases = ["+meditation"]
    help_category = "inner world"

    def func(self):
        """moves to inner world"."""
        caller = self.caller

        # create empty inner world if needed
        if not caller.db.innerWorld:
            caller.db.innerWorld = create_object(
                "typeclasses.innerworld.Home",
                key="Entrance to Inner World of %s" % caller.name,
            )
            caller.db.innerWorld.tags.add("Inner World")
            # add inner world to faction
            if caller.db.faction is not None:
                faction = caller.db.faction
                caller.db.innerWorld.db.faction = faction
                caller.db.innerWorld.tags.add(faction.name, category="faction")
        # create inner character, if needed
        if not caller.db.innerSelf:
            caller.db.innerSelf = create_object(
                "characters.InnerCharacter",
                key=caller.key,
                location=caller.db.innerWorld,
                locks="edit:id(%i) and perm(Builders);call:false()" % caller.id,
        )
        if not caller.location:
            # may not meditate when OOC
            caller.msg("You must have a location to begin meditation.")
            return
        if caller.db.in_meditation:
            caller.msg("You continue to meditate.")
            return
        caller.db.in_meditation = True
        if caller.location is not caller.db.innerWorld:
            caller.db.outerWorld = caller.location
        caller.msg("You close your eyes and visualize your inner world.")
        caller.move_to(caller.db.innerWorld)
        return


class CmdAwaken(Command):
    """
    leave inner world
    Usage:
        +awaken
    Moves charcater back into outer world
    """

    key = "+awaken"
    aliases = ["+awaken"]
    help_category = "inner world"

    def func(self):
        """moves to outer world."""
        caller = self.caller
        if not caller.db.in_meditation:
            caller.msg("You are not in meditation.")
            return
        caller.msg("You leave your inner world and return to the outer world.")
        caller.move_to(caller.db.outerWorld)
        caller.db.in_meditation = False
        return


class CmdRest(Command):
    """
    restore energy
    Usage:
        +rest
    rest until maximum energy is reached
    """

    key = "+rest"
    aliases = ["+sleep"]
    help_category = "general"

    def func(self):
        """recover energy"""
        caller = self.caller
        if not caller.db.stamina:
            caller.db.stamina = 0
        if not caller.db.health:
            caller.db.health = 100
        stamina_level = proficiency(caller.db.stamina)
        maximum_energy = int(caller.db.health * stamina_level)
        if caller.db.energy is None:
            caller.db.energy = 0
        amount_to_recover = maximum_energy - caller.db.energy
        if amount_to_recover <= 0 and caller.db.health == 100:
            self.caller.db.resting = False
            self.caller.msg("You are already fully rested.")
            return
        time_to_recover = int(RECOVERY_RATE * amount_to_recover / stamina_level)
        utils.delay(time_to_recover, self.recover)
        self.caller.db.resting = True
        hours_to_recovery = time_to_recover / 3600.0
        if hours_to_recovery > 1.0:
            caller.msg(
                "You begin resting. You will be fully rested in %.1f hours."
                % hours_to_recovery
            )
        else:
            minutes_to_recovery = time_to_recover / 60.0
            caller.msg(
                "You begin your nap. You will be fully rested in %.1f minutes."
                % minutes_to_recovery
            )

    def recover(self):
        """This will be called when fully recovered."""
        caller = self.caller
        stamina_level = proficiency(caller.db.stamina)
        # maximum energy level depends on health and stamina
        caller.db.energy = int(caller.db.health * stamina_level)
        # resting also restores some health percentage
        if caller.db.health < 100:
            caller.db.health = min(100, caller.db.health + int(stamina_level))
        caller.msg("You are fully rested now.")


class CmdStats(Command):
    """
    Show the skill levels and stats of a character
    Usage:
      +skills
    This shows the skills and stats of the current character.
    """

    key = "+skills"
    aliases = ["+profile", "+status"]
    help_category = "skills"

    def func(self):
        """Display profile."""
        self.caller.msg("Your health is now %d%%." % self.caller.db.health)
        self.caller.msg("Your energy is now %d." % self.caller.db.energy)
        self.caller.msg(
            "Your reputation level is now %.2f."
            % proficiency(self.caller.db.reputation)
        )
        self.caller.msg(
            "Your strength level is now %.2f." % proficiency(self.caller.db.strength)
        )
        self.caller.msg(
            "Your agility level is now %.2f." % proficiency(self.caller.db.agility)
        )
        self.caller.msg(
            "Your speed level is now %.2f." % proficiency(self.caller.db.speed)
        )
        self.caller.msg(
            "Your stamina level is now %.2f." % proficiency(self.caller.db.stamina)
        )
        for skillname in self.caller.db.skills.keys():
            self.caller.msg(
                f"Your {skillname} skill level is now {round(proficiency(self.caller.db.skills[skillname]), 2)}."
            )


class CmdRace(Command):
    """
    Set or show the the species or race of a character
    Usage:
      +race <name>
    This sets or shows the race of the current character.
    """

    key = "+race"
    aliases = ["+species", "+kind"]
    help_category = "general"

    def func(self):
        """This performs the actual command."""
        caller = self.caller
        if caller.db.race is None or len(caller.db.race) < 2:
            caller.db.race = self.args.strip().title()
            caller.tags.add(caller.db.race, category="race")
        caller.msg("You are a " + caller.db.race)
