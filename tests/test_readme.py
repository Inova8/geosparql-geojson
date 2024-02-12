from rdflib import Literal, Graph, Namespace, URIRef
from rdflib.namespace import GEO
import geojson

g = Graph()
g.add((URIRef('https://geom-a'), GEO.hasGeometry, Literal('''{"coordinates":[[[ 0,1],[4,1],[4,5],[0,5],[0,1]]],"type": "Polygon"}''')))
g.add((URIRef('https://geom-b'), GEO.hasGeometry, Literal('''{"coordinates": [[[ 0,1],[2,1],[2,3],[0,3],[0,1]]],"type": "Polygon"}''')))
g.add((URIRef('https://geom-c'), GEO.hasGeometry, Literal('''{"coordinates": [[[ 4,3],[6,3],[6,5],[4,5],[4,3]]], "type": "Polygon"}''')))
g.add((URIRef('https://geom-e'), GEO.hasGeometry, Literal('''{"coordinates": [[2,0],[3,3]],"type": "LineString"}''')))
g.add((URIRef('https://geom-f'), GEO.hasGeometry, Literal('''{"coordinates": [ 2,4],"type": "Point"}''')))

def test_contains():
    assert geojson.contains(g.value(URIRef('https://geom-a'), GEO.hasGeometry), g.value(URIRef('https://geom-b'), GEO.hasGeometry))
def test_query():
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
        print (r)
        print(f"{r['a']} is within {r['b']}")