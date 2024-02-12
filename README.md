# RDFLib GeoSPARQ functions for GeoJSON
This library provides support for the GeoSPARQL 1.1 Simple Features Relation Family for geometries expressed as GeoJSON Literals. 
It has drawn heavily on geosparql-dggs (https://github.com/RDFLib/geosparql-dggs).

# Installation

```
!pip install rdflib
!pip install git+https://github.com/inova8/geosparql-geojson.git
```

This package depends on to support the functions' use against graphs RDFlib. The functions depend on the shapely library

# Use

```
from rdflib import Literal, Graph, Namespace, URIRef
from rdflib.namespace import GEO
import geojson
imprt json

g = Graph()
g.add((URIRef('https://geom-a'), GEO.hasGeometry, Literal('''{"coordinates":[[[ 0,1],[4,1],[4,5],[0,5],[0,1]]],"type": "Polygon"}''',datatype=GEO.geoJSONLiteral)))
g.add((URIRef('https://geom-b'), GEO.hasGeometry, Literal(json.loads('''{"coordinates": [[[ 0,1],[2,1],[2,3],[0,3],[0,1]]],"type": "Polygon"}'''))))
g.add((URIRef('https://geom-c'), GEO.hasGeometry, Literal(json.loads('''{"coordinates": [[[ 4,3],[6,3],[6,5],[4,5],[4,3]]],"type": "Polygon"}'''),datatype=GEO.geoJSONLiteral)))
g.add((URIRef('https://geom-e'), GEO.hasGeometry, Literal('''{"coordinates": [[2,0],[3,3]],"type": "LineString"}''')))
g.add((URIRef('https://geom-f'), GEO.hasGeometry, Literal('''{"coordinates": [ 2,4],"type": "Point"}''')))
```
Note that the literal value for the GEO.hasGeometry can be any of the following

- string of json
- typed datatype=GEO.geoJSONLiteral or untyped

We can now query the graph g, invoking geojson functions as follows:
```
# Query the in-memory graph
q = """
    PREFIX geo: <http://www.opengis.net/ont/geosparql#>

    SELECT ?a ?b
    WHERE {
        ?a geo:hasGeometry ?a_geom .
        ?b geo:hasGeometry ?b_geom .

        FILTER geo:sfWithin(?a_geom, ?b_geom)
    }"""
# Interate through and print results
for r in g.query(q):
  print(f"{r['a']} is within {r['b']}")
```

The results should be:

```
https://geom-a is within https://geom-a
https://geom-b is within https://geom-a
https://geom-b is within https://geom-b
https://geom-c is within https://geom-c
https://geom-f is within https://geom-a
https://geom-f is within https://geom-f
```

The geojson functions can also be used directly with RDFLib as follows:

```
geojson.contains(Literal('''{"coordinates":[[[ 0,1],[4,1],[4,5],[0,5],[0,1]]],"type": "Polygon"}'''),
                 Literal('''{"coordinates": [ 2,4],"type": "Point"}''')).value
```

which returns
```
True
```

# Function Definitions

- geo:sfEqual: Returns Literal(true) if the first geometry is equal to the second geometry.
- geo:sfWithin: Returns Literal(true) if the first geometry is within the second geometry.
- geo:sfContains: Returns Literal(true) if the first geometry contains the second geometry.
- geo:sfIntersects: Returns Literal(true) if the first geometry intersects (i.e. has any spatial relation other than disjoint) the second geometry.
- geo:sfTouches: Returns Literal(true) if the first geometry touches the second geometry.
- geo:sfDisjoint: Returns Literal(true) if the first geometry is disjoint with the second geometry.
- geo:sfOverlaps: Returns Literal(true) if the first geometry overlaps the second geometry.

# Testing
All tests are in tests/ and implemented using pytest.

# Contributing
Via GitHub, Issues & Pull Requests:

https://github.com/Inova8/geosparql-geojson

# License
This code is licensed with the BSD 3-clause license as per LICENSE which is the same license as used for rdflib.

# Citation
@software{https://github.com/Inova8/geosparql-geojson,
  author = {{Peter lawrence}},
  title = {RDFlib GeoSPARQL Functions for GeoJSON},
  version = {0.1.0},
  date = {2024},
  url = {https://github.com/Inova8/geosparql-geojson}
}
Contact
Creator & maintainer:
Peter Lawrence
Application Architect
inova8 plc
peter.lawrence@inova8.com
