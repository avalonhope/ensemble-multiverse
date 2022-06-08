def subfaction(child, parent):
    """Check if one faction is a subfaction of another."""
    if child is parent:
        return True
    if child.db.superfaction is None:
        return False
    if child.db.superfaction is parent:
        return True
    faction = child.db.superfaction
    found = False
    while faction.db.superfaction is not None:
        if faction.db.superfaction is parent:
            found = True
            break
        faction = faction.db.superfaction
    return found
