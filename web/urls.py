# type: ignore
"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = []

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
