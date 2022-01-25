from packages.algorithms.clock import clock
from packages.algorithms.lru import lru
from packages.algorithms.optimized import optimized
from packages.algorithms.fifo import fifo
from packages.utility.fileParser import parseFile

pages, mem_size = parseFile('sample.txt')
mem_o, flt_o = optimized(pages, mem_size)
mem_l, flt_l = lru(pages, mem_size)
mem_f, flt_f = fifo(pages, mem_size)
mem_c, flt_c = clock(pages, mem_size)

print('Optimized:')
print(mem_o)
print(f'Page Faults: {flt_o}')
print('==================')
print()
print('Least Recently Used:')
print(mem_l)
print(f'Page Faults: {flt_l}')
print('==================')
print()
print('First-In-First-Out:')
print(mem_f)
print(f'Page Faults: {flt_f}')
print('==================')
print()
print('Clock:')
print(mem_c)
print(f'Page Faults: {flt_c}')
print('==================')