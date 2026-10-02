import requests, time
import json, rdflib, csv
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS, XSD

# schema
uriMap = {
        "hasType" : URIRef('http://hasType'),
        "hasLabel" : URIRef('http://hasLabel'),
        }

# crawling clinvar API given a list of variant identifiers
def parse_API(inputfile, start, end):
    data = []
    with open(inputfile, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='')
        for row in spamreader:
            data.append(row)
    filename = "clinvar" + str(start) + "_" + str(end) + ".ttl"

parse_API("clinvar_id_partial.csv", 100, 500)
