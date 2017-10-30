from __future__ import print_function
from pyhop import *

import goda_operators
print('')
print_operators()

import goda_methods
print('')
print_methods()

# Definicao do Estado inicial
state1 = State('state1')
state1.objects = {'T0': False, 'T1': False, 'T2': False, 'T3': False, 'T4': False, \
				  'G0': False, 'G1': False, 'G2': False, 'G3': False, 'G4': False}


pyhop(state1, [('k_times', 'T0', 2)], verbose=1)

# pyhop(state1, [('completed', 'T3'), ('try_op', 'T0', 'T3', 'T4'), ('completed', 'G2'), \
# 			   ('completed', 'T1'), ('completed', 'T2'), ('completed', 'G3'), ('completed', 'G4'), \
# 			   ('and_par', 'G0', 'G3', 'G4')], verbose=1)