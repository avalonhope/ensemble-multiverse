from enum import IntEnum


class LocationType(IntEnum):
    """System of Room and Object Locations."""

    # Each level is contained with the next level up,
    # for example: a room is inside a building,
    # a command room is a room associated with a Station, and
    # a starship is an object within a Star System, but also has associated rooms
    ROOM = 0  # cannot have any sub-rooms, lowest possible level
    BUILDING = 1  # structure, cavern, vehicle, shuttle
    AREA = 2  # street, village, docking bay, open terrain
    DISTRICT = 3  # major village, town quarter, large ship
    TOWN = 4  # space station, county, shipyard, wilderness, floating city
    REGION = 5  # major city, province, duchy, atmospheric layer
    COUNTRY = 6  # major country or minor planet, atmosphere of major planet, moon
    PLANET = 7  # planets, stars, inner worlds for most species
    SYSTEM = 8  # single star system or a deep space region
    SECTOR = 9  # large group of star systems
    GALAXY = 10  # single galaxy, inner world for some species
    CLUSTER = 11  # galaxy cluster or group
    SUPERCLUSTER = 12  # any large cosmic structure
    UNIVERSE = 13  # physical space-time continuum, inner worlds for advanced species
    MULTIVERSE = 14  # all of creation, visible and invisible, highest possible level
