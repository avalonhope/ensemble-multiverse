def subfaction(child, parent):
  """Check if one faction is a subfaction of another."""
  if child.db.superfaction is None:
    return false
  elif child.db.superfaction.name == parent.name:
    return true
  else:
    superfaction = child.db.superfaction
    found = false
    while superfaction.db.superfaction is not None:
      if superfaction.db.superfaction.name == parent.name:
        found = true
        break
      superfaction = superfaction.db.superfaction
    return found
