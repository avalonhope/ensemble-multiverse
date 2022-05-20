r"""
Evennia settings file.

The available options are found in the default settings file found
here:

../../evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

MULTISESSION_MODE = 3
MAX_NR_CHARACTERS = 10000000

######################################################################
# Starquest (Infinite Worlds) parameters
######################################################################

RECOVERY_RATE = 300  # five minutes per energy point

SKILLS = ["agriculture", "archery", "ecology", "electronics", 
          "horticulture", "leadership", 
          "medicine", "microbiology", "robotics", "piloting", 
          "building", "discovery", "exploration", "crafting"]


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
    SERVERNAME = "Starquest - Infinite Worlds"
    WEBSERVER_ENABLED = False
    
