from .sf_functions import (
    contains,
    overlaps,
    equals,
    touches,
    within,
    disjoint,
    intersects,
)
from rdflib import Namespace
from rdflib.namespace import GEO
from rdflib.plugins.sparql.operators import register_custom_function

__version__ = "0.1"

register_custom_function(GEO.sfContains, contains)
register_custom_function(GEO.sfEquals, equals)
register_custom_function(GEO.sfOverlaps, overlaps)
register_custom_function(GEO.sfDisjoint, disjoint)
register_custom_function(GEO.sfWithin, within)
register_custom_function(GEO.sfTouches, touches)
register_custom_function(GEO.sfIntersects, intersects)