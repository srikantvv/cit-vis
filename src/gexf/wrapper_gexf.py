#!/usr/bin/python

import sys,pprint

from _gexf import Gexf, GexfImport

# test helloworld.gexf
gexf = Gexf("Paul Girard","A hello world! file")
graph=gexf.addGraph("directed","static","a hello world graph")

graph.addNode("0","hello")
graph.addNode("1","World")
graph.addEdge("0","0","1")

output_file=open("../output/world_map.gexf","w")
gexf.write(output_file)
