from enum import IntEnum


class LocationType(IntEnum):
    """System of Room and Object Locations."""

    # Each level is contained with the next level up,
    # for example: a room is inside a building,
    # a command room is a room associated with a Station, and
    # a starship is an object within a Star System, but also has associated rooms
    ROOM = 0  # cannot have any sub-rooms, lowest possible level
    VEHICLE = 0
    BUILDING = 1  # structure, cavern, vehicle, shuttle
    AREA = 2  # street, village, docking bay, open terrain
    VILLAGE = 2
    DISTRICT = 3  # major village, town quarter, large ship
    SPACECRAFT = 3
    TOWN = 4  # space station, county, shipyard, wilderness, floating city
    SPACE_STATION = 4  # space colony, space dock
    REGION = 5  # major city, province, duchy, atmospheric layer
    STARSHIP = 5
    COUNTRY = 6  # major country or minor planet, atmosphere of major planet, moon
    MOON = 6
    DEEP_SPACE_ZONE = 7
    PLANET = 7  # planets, stars, inner worlds for most species
    STAR = 7
    SYSTEM = 8  # single star system or a deep space region
    SECTOR = 9  # large group of star systems
    GALAXY = 10  # single galaxy, inner world for some species
    INTERGALACTIC_ZONE = 10
    CLUSTER = 11  # galaxy cluster or group
    SUPERCLUSTER = 12  # any large cosmic structure
    COSMIC_VOID = 12
    UNIVERSE = 13  # physical space-time continuum, inner worlds for advanced species
    MULTIVERSE = 14  # all of creation, visible and invisible, highest possible level
