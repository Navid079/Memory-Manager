from packages.algorithms.clock import clock
from packages.algorithms.lru import lru
from packages.algorithms.optimized import optimized
from packages.utility.fileParser import parseFile

pages, mem_size = parseFile('sample.txt')
mem_o, flt_o = optimized(pages, mem_size)
mem_l, flt_l = lru(pages, mem_size)
mem_c, flt_c = clock(pages, mem_size)

# print(mem_o)