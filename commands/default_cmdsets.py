"""
Command sets

All commands in the game must be grouped in a cmdset.  A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""

from evennia import default_cmds
from commands import command, faction  # type: ignore


class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `AccountCmdSet` when an Account puppets a Character.
    """

    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """Populates the cmdset"""
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        self.add(command.CmdImagine())
        self.add(command.CmdMeditate())
        self.add(command.CmdAwaken())
        self.add(command.CmdRest())
        self.add(command.CmdStats())
        self.add(faction.CmdFactions())
        self.add(faction.CmdFactionCreate())
        self.add(faction.CmdFactionClaim())
        self.add(faction.CmdFactionJoin())
        self.add(faction.CmdFactionSpace())
        self.add(command.CmdTrainSkill())
        self.add(command.CmdRace())
        self.add(faction.CmdQuest())


class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the cmdset available to the Account at all times. It is
    combined with the `CharacterCmdSet` when the Account puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """

    key = "DefaultAccount"


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.  This
    holds commands like creating a new account, logging in, etc.
    """

    key = "DefaultUnloggedin"


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """

    key = "DefaultSession"
