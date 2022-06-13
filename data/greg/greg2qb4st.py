from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, XSD
from rdflib.namespace import DC, DCTERMS, SKOS, RDF, RDFS, OWL
import geopandas as gpd
import pandas as pd
import numpy as np

QB = Namespace('http://purl.org/linked-data/cube#')
GEO = Namespace('http://www.opengis.net/ont/geosparql#')
GREG_DIM = Namespace('http://ios-regensburg.de/greg/def/dimension/')
GREG_MEA = Namespace('http://ios-regensburg.de/greg/def/measure/')

g = Graph()
g.bind('qb', QB)
g.bind('geo', GEO)
g.bind('greg-dimension', GREG_DIM)
g.bind('greg_measure', GREG_MEA)

greg = gpd.read_file("GREG.shp")

ds_uri = "http://ios-regensburg.de/greg/data/greg-ld/"
ds = URIRef(ds_uri)

for index, row in greg.iterrows():
  greg_id = row['FeatureID']
  obs_uri = "http://ios-regensburg.de/greg-ld/data/greg-ld/%s" % greg_id
  obs = URIRef(obs_uri)

  g.add( (obs, RDF.type, QB.Observation) )
  g.add( (obs, QB.dataSet, ds) )

  g.add( (obs, GREG_DIM.group, 
    URIRef('http://ios-regensburg.de/greg/def/concept/group/%s' % row['GROUP1'])) )


  g.add( (obs, GREG_MEA.geom, Literal(row['geometry'], datatype=GEO.wktLiteral)) )

g.serialize(destination='greg_qb.ttl', format='turtle')
