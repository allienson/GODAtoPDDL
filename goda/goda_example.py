from __future__ import print_function
from pyhop import *

import goda_operators
import goda_methods

print('')
print_operators()

print('')
print_methods()

state = State('Width')
state.objects = { \
'T2:_Task':True, \
'T3:_Task':True, \
'T4:_Task':True, \
'T5:_task':True, \
'T6:_Task':True, \
'T1:_Task':False, \
'G1:_Subgoal':False, \
'G2:_Subgoal':True, \
'T1.1:_task':True, \
'G3:_Subgoal':False, \
'G4:_Subgoal':True, \
'T8:_Task':True, \
'T9:_Task':True, \
'T10:_task':True, \
'T11:_Task':True, \
'T7:_Task':False, \
'G5:_Subgoal':False, \
'G0:_Goal':False}

pyhop(state, [ \
('and_seq', 'T1:_Task', 'T2:_Task', 'T3:_Task', 'T4:_Task', 'T5:_task', 'T6:_Task'), \
('means_end', 'G1:_Subgoal', 'T1:_Task'), \
('opt', 'G3:_Subgoal', 'T1.1:_task'), \
('and_par', 'T7:_Task', 'T8:_Task', 'T9:_Task', 'T10:_task', 'T11:_Task'), \
('means_end', 'G5:_Subgoal', 'T7:_Task'), \
('or_par', 'G0:_Goal', 'G1:_Subgoal', 'G2:_Subgoal', 'G3:_Subgoal', 'G4:_Subgoal', 'G5:_Subgoal'), \
], verbose=1)