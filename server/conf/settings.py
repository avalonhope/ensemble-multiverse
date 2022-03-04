r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/avalon/starquest/evennia/evennia/settings_default.py

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

MEDITATION_COST = 10
MINDSHIELD_GAIN = 5
RECOVERY_RATE = 300  # five minutes per energy point

BUILDING_COST = 10
BUILDING_RATE = 30

OPTIONAL_SKILLS = ["archery", "leadership", "medicine", "mindmeld", "mindshield", "piloting", "building"]

DEFAULT_BUILDING = "Town Hall"
DEFAULT_AREA = "Main Street"
DEFAULT_DISTRICT = "Central District"
DEFAULT_TOWN = "Difenland City"
DEFAULT_REGION = "Capital Region" 
DEFALT_COUNTRY = "Difenland"  
DEFAULT_PLANET = "Fleador Prime"
DEFAULT_SYSTEM = "Fleador System"
DEFAULT_SECTOR = "Fleador Sector"
DEFAULT_GALAXY = "Milky Way Galaxy"
DEFAULT_CLUSTER = "Virgo Cluster"
DEFAULT_SUPERCLUSTER = "Virgo Supercluster"  
DEFAULT_UNIVERSE = "The Known Universe"

DEFAULT_LEVEL_0_TITLE = "Agent"
DEFAULT_LEVEL_1_TITLE = "Sergeant"
DEFAULT_LEVEL_2_TITLE = "Lieutenant"
DEFAULT_LEVEL_3_TITLE = "Captain"
DEFAULT_LEVEL_4_TITLE = "Inspector"
DEFAULT_LEVEL_5_TITLE = "Deputy Chief Inspector"
DEFAULT_LEVEL_6_TITLE = "Chief Inspector"
DEFAULT_LEVEL_7_TITLE = "Superintendant"
DEFAULT_LEVEL_8_TITLE = "Deputy Chief Superintendant"
DEFAULT_LEVEL_9_TITLE = "Chief Superintendant"
DEFAULT_LEVEL_10_TITLE = "Superintendant General"
DEFAULT_LEVEL_11_TITLE = "Deputy Assistant Leader"
DEFAULT_LEVEL_12_TITLE = "Assistant Leader"
DEFAULT_LEVEL_13_TITLE = "Deputy Leader"
DEFAULT_LEVEL_14_TITLE = "Faction Leader"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
