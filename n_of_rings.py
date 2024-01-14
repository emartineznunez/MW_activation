#!/usr/bin/env python3
from networkx import simple_cycles, DiGraph
from sys import argv
from ase.io import read
from param import cov_rad


rmol = read(str(argv[1]))
symb  = rmol.get_chemical_symbols()
G = DiGraph()
for i in range(len(rmol)):
     for j in range(i+1,len(rmol)):
         if rmol.get_distance(i,j) < 1.2 * ( cov_rad[symb[i]] + cov_rad[symb[j]] ):
            G.add_edge(i,j); G.add_edge(j,i)

rings = []
for lista in list(simple_cycles(G)):
    if len(lista) == 5 or len(lista) == 6:
        lista.sort()
        if lista not in rings:
            rings.append(lista)
print('Number of rings >5 = ',len(rings))
