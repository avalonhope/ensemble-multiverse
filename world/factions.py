def subfaction(child, parent):
  """Check if one faction is a subfaction of another."""
  if child.db.superfaction is None:
    return False
  elif child.db.superfaction.name == parent.name:
    return True
  else:
    superfaction = child.db.superfaction
    found = False
    while superfaction.db.superfaction is not None:
      if superfaction.db.superfaction.name == parent.name:
        found = True
        break
      superfaction = superfaction.db.superfaction
    return found
