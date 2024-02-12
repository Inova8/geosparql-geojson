# RDFLib GeoSPARQ functions for GeoJSON
This library provides support for the GeoSPARQL 1.1 Simple Features Relation Family for geometries expressed as GeoJSON Literals. 
It has drawn heavily on geosparql-dggs (https://github.com/RDFLib/geosparql-dggs).

# Installation

pip install git+https://github.com/inova8/geosparql-geojson.git

This package depends on to support the functions' use against graphs RDFlib. The functions depend on the shapely library

# Use


# Function Definitions


geo:sfEqual: Returns Literal(true) if the first geometry is equal to the second geometry.
dggeogs:sfWithin: Returns Literal(true) if the first geometry is within the second geometry.
geo:sfContains: Returns Literal(true) if the first geometry contains the second geometry.
geo:sfIntersects: Returns Literal(true) if the first geometry intersects (i.e. has any spatial relation other than disjoint) the second geometry.
geo:sfTouches: Returns Literal(true) if the first geometry touches the second geometry.
geo:sfDisjoint: Returns Literal(true) if the first geometry is disjoint with the second geometry.
geo:sfOverlaps: Returns Literal(true) if the first geometry overlaps the second geometry.

# Testing
All tests are in tests/ and implemented using pytest.
