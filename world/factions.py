def subfaction(child, parent):
  """Check if one faction is a subfaction of another."""
  if child.name == parent.name:
    return true
  elif child.db.superfaction is None:
    return False
  elif child.db.superfaction.name == parent.name:
    return True
  else:
    subfaction = child.db.superfaction
    found = False
    while subfaction.db.superfaction is not None:
      if subfaction.db.superfaction.name == parent.name:
        found = True
        break
      subfaction = subfaction.db.superfaction
    return found
