from rdflib import Literal
from shapely import LineString, Point, Polygon, contains

def contains(a, b) -> Literal:
    # Returns Literal(true) if the first geometry contains the second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b)
    if contains(geoA, geoB):
        return Literal(True)
    return Literal(False)
def within(a, b) -> Literal:
   #  Returns Literal(true) if the first geometry is within the second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b)
    if within(geoA, geoB):
        return Literal(True)
    return Literal(False)
def disjoint(a, b) -> Literal:
    #Returns Literal(true) if the first geometry is disjoint with the second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b))
    if disjoint(geoA, geoB):
        return Literal(True)
    return Literal(False)
def intersects(a, b) -> Literal:
    # Returns Literal(true) if the first geometry intersects (i.e. has any spatial relation other than disjoint) the
    # second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b))
    if intersects(geoA, geoB):
        return Literal(True)
    return Literal(False)
def touches(a, b) -> Literal:
    # Returns Literal(true) if the first geometry touches the second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b))
    if touches(geoA, geoB):
        return Literal(True)
    return Literal(False)
def overlaps(a, b) -> Literal:
    # Returns Literal(true) if the first geometry overlaps the second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b))
    if overlaps(geoA, geoB):
        return Literal(True)
    return Literal(False)
def equals(a, b) -> Literal:
    # Returns Literal(true) if the first geometry is equal to the second geometry.
    geoA= toGeoJason(a)
    geoB= toGeoJason(b))
    if equals(geoA, geoB):
        return Literal(True)
    return Literal(False)
def toGeoJason(geometry:Literal):
    match  geometry.value['type']:
        case 'Point':
            return Point(geometry.value['coordinates'])
        case 'Polygon':
            return Polygon(geometry.value['coordinates'][0])
        case 'LineString':
            return LineString(geometry.value['coordinates'][0])
        case _:
            return None
    