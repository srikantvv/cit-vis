#!/usr/bin/python

import sys,pprint

from _gexf import Gexf, GexfImport

# test helloworld.gexf
class WrapperGexf:

    def __init__(self, ofile="../output/world_map.gexf"):
        self.startID = 0
        self.ofile = ofile

    def setID(self, sID):
        self.startID = sID

    def populate(self):
        gexf = Gexf("Citation Visualizer","An academic paper visualizer")
        graph=gexf.addGraph("directed","static","a citation world map")
        
        graph.addNode("0","hello")
        graph.addNode("1","World")
        graph.addEdge("0","0","1")
        
        output_file=open(self.ofile,"w")
        gexf.write(output_file)
