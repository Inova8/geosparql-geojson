from rdflib import Literal
import shapely
import json
#from shapely import LineString, Point, Polygon, contains

def contains(a, b) -> Literal:
    # Returns Literal(true) if the first geometry contains the second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.contains(geoA, geoB):
        return Literal(True)
    return Literal(False)
def within(a, b) -> Literal:
   #  Returns Literal(true) if the first geometry is within the second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.within(geoA, geoB):
        return Literal(True)
    return Literal(False)
def disjoint(a, b) -> Literal:
    # Returns Literal(true) if the first geometry is disjoint with the second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.disjoint(geoA, geoB):
        return Literal(True)
    return Literal(False)
def intersects(a, b) -> Literal:
    # Returns Literal(true) if the first geometry intersects (i.e. has any spatial relation other than disjoint) the
    # second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.intersects(geoA, geoB):
        return Literal(True)
    return Literal(False)
def touches(a, b) -> Literal:
    # Returns Literal(true) if the first geometry touches the second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.touches(geoA, geoB):
        return Literal(True)
    return Literal(False)
def overlaps(a, b) -> Literal:
    # Returns Literal(true) if the first geometry overlaps the second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.overlaps(geoA, geoB):
        return Literal(True)
    return Literal(False)
def equals(a, b) -> Literal:
    # Returns Literal(true) if the first geometry is equal to the second geometry.
    geoA= toGeoJSON(a)
    geoB= toGeoJSON(b)
    if shapely.equals(geoA, geoB):
        return Literal(True)
    return Literal(False)
def toGeoJSON(geometry:Literal):
    if(isinstance(geometry.value,str)):
        value= json.loads(geometry.value)
    else:
        value = geometry.value
    match  value['type']:
        case 'Point':
            return shapely.Point(value['coordinates'])
        case 'Polygon':
            return shapely.Polygon(value['coordinates'][0])
        case 'LineString':
            return shapely.LineString(value['coordinates'][0])
        case _:
            return None
    