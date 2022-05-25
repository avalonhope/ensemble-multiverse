def subfaction(child, parent):
  """Check if one faction is a subfaction (or nested subfaction) of another."""
  if child is parent:
    return True
  if child.db.superfaction is None:
    return False
  return subfaction(child.db.superfaction, parent)
