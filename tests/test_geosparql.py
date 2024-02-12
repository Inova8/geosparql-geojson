from rdflib import Literal, Graph,  URIRef
from rdflib.namespace import GEO
from geojson.sf_functions import(    contains,
    overlaps,
    equals,
    touches,
    within,
    disjoint,
    intersects,
)
import json

# image showing cells is in tests folder
g = Graph()
geom_a = URIRef("https://geom-a") # POLYGON
geom_b = URIRef("https://geom-b") # POLYGON
geom_c = URIRef("https://geom-c") # POLYGON
geom_d = URIRef("https://geom-d") # POLYGON
geom_e = URIRef("https://geom-e") # POLYGON
geom_f = URIRef("https://geom-f") # POINT
geom_g = URIRef("https://geom-g") # LINESTRING

geojsonFile= open("./tests/sf_relationships_geojson.json")
geojson= json.load(geojsonFile)
geojsonFile.close()
 
get_element_by_key = lambda array,key,value: next(filter(lambda x: x[key] == value, array), {})
 

g.add((geom_a, GEO.hasGeometry, Literal(get_element_by_key(geojson['features'],'id','geom_a')['geometry'],datatype=GEO.geoJSONLiteral)))
g.add((geom_b, GEO.hasGeometry, Literal(get_element_by_key(geojson['features'],'id','geom_b')['geometry'])))
g.add((geom_c, GEO.hasGeometry, Literal(get_element_by_key(geojson['features'],'id','geom_c')['geometry'])))
g.add((geom_d, GEO.hasGeometry, Literal(get_element_by_key(geojson['features'],'id','geom_d')['geometry'])))
g.add((geom_e, GEO.hasGeometry, Literal('''{"coordinates": [[2,0],[3,3]],"type": "LineString"}''')))
g.add((geom_f, GEO.hasGeometry, Literal('''{"coordinates": [ 2,4],"type": "Point"}''',datatype=GEO.geoJSONLiteral)))
g.add((geom_g, GEO.hasGeometry, Literal(get_element_by_key(geojson['features'],'id','geom_g')['geometry'])))

# The test SPARQL creates the cartesian product of each test, 49 in total

def test_direct():
    geom_a_value= g.value(geom_a, GEO.hasGeometry)
    geom_b_value = g.value(geom_b, GEO.hasGeometry)
    a_contains_b= contains(geom_a_value, geom_b_value)
    assert a_contains_b == Literal(True)

def test_contains():
    # A contains B
    # A contains F
    # D contains G
    # G contains D  
    # x contains x for A, B, C, D, G, F
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfContains(?a_geom, ?b_geom) }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 8
    #assert result[0]["a"] == geom_a and result[0]["b"] == geom_b

def test_within():
    # B is within A
    # F is within A
    # D is within G
    # G is within D  
    # x is within x for A, B, C, D, G, F
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfWithin(?a_geom, ?b_geom) }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 8
    #assert result[0]["a"] == geom_b and result[0]["b"] == geom_a

def test_intersects():
    # A intersects B
    # A intersects C
    # A intersects D
    # A intersects G
    # B intersects A
    # C intersects A
    # D intersects A
    # D intersects G
    # G intersects A
    # G intersects D
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfIntersects(?a_geom, ?b_geom)
                FILTER (?a!=?b)
                }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 10
    assert {"a": geom_a, "b": geom_b} in result
    assert {"a": geom_a, "b": geom_c} in result
    assert {"a": geom_a, "b": geom_d} in result
    assert {"a": geom_a, "b": geom_g} in result
    assert {"a": geom_b, "b": geom_a} in result
    assert {"a": geom_c, "b": geom_a} in result
    assert {"a": geom_d, "b": geom_a} in result
    assert {"a": geom_d, "b": geom_g} in result
    assert {"a": geom_g, "b": geom_a} in result
    assert {"a": geom_g, "b": geom_d} in result

def test_touches():
    # A touches C
    # C touches A
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfTouches(?a_geom, ?b_geom)
                }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 2
    assert {"a": geom_a, "b": geom_c} in result
    assert {"a": geom_c, "b": geom_a} in result

def test_equals():
    # D equals G
    # G equals D
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfEquals(?a_geom, ?b_geom)
                FILTER(?a!=?b)
                }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 2
    assert {"a": geom_d, "b": geom_g} in result
    assert {"a": geom_g, "b": geom_d} in result

def test_overlaps():
    # D overlaps A
    # A overlaps D
    # G overlaps A
    # A overlaps G
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfOverlaps(?a_geom, ?b_geom) }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 4
    assert {"a": geom_a, "b": geom_d} in result
    assert {"a": geom_d, "b": geom_a} in result
    assert {"a": geom_a, "b": geom_g} in result
    assert {"a": geom_g, "b": geom_a} in result

def test_disjoint():
    # B disjoint C
    # C disjoint B
    # B disjoint D
    # D disjoint B
    # B disjoint G
    # G disjoint B
    # D disjoint C
    # C disjoint D
    # G disjoint C
    # C disjoint G
    result = g.query(
        """PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    SELECT ?a ?b {?a geo:hasGeometry ?a_geom .
                ?b geo:hasGeometry ?b_geom .
                FILTER geo:sfDisjoint(?a_geom, ?b_geom) }"""
    )
    result = [{str(k): v for k, v in i.items()} for i in result.bindings]
    assert len(result) == 10
    assert {"a": geom_b, "b": geom_c} in result
    assert {"a": geom_c, "b": geom_b} in result
    assert {"a": geom_b, "b": geom_d} in result
    assert {"a": geom_d, "b": geom_b} in result
    assert {"a": geom_b, "b": geom_g} in result
    assert {"a": geom_g, "b": geom_b} in result
    assert {"a": geom_d, "b": geom_c} in result
    assert {"a": geom_c, "b": geom_d} in result
    assert {"a": geom_g, "b": geom_c} in result
    assert {"a": geom_c, "b": geom_g} in result