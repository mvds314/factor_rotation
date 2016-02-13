# -*- coding: utf-8 -*-
"""
Example illustrating usage.
Other examples are contained in the unittests.
"""

from __future__ import division
from __future__ import print_function

import numpy as np
import factor_rotation as fr

#rotate M towards target with orthogonal matrix T
M = np.array([[ 1.10061095,  0.47713676],
              [ 1.30095568, -0.16730989],
              [ 1.6787652 , -1.234039  ],
              [ 0.42456929, -1.28744732],
              [ 0.47105995,  0.85757736],
              [-0.05816789,  0.31683709],
              [-1.3511985 , -0.11610641],
              [ 1.80523345, -0.14549883]])
M_target = np.array([[ 1.15424697,  0.2724154 ],
                     [ 0.7893224 ,  0.66576866],
                     [-0.71227541,  0.55254571],
                     [-0.84737515,  0.41528169],
                     [-0.12133101, -1.28176304],
                     [-0.60248373, -0.5405648 ],
                     [ 0.45355659,  0.54495004],
                     [ 0.62044144, -1.83902599]])
#analytic method
T_analytic= fr.target_rotation(M,M_target)
#numerical method using a gradient projection algorithm (GPA)
L,T = fr.rotate_factors(M,'target',M_target,'orthogonal')
print(np.allclose(T,T_analytic,atol=1e-4))
#numerical method using a gradient projection algorithm (GPA) with lower level functions
#define objective function
vgQ = lambda L=None, A=None, T=None: fr._gpa_rotation.vgQ_target(M_target,L=L,A=A,T=T)
#define starting point
T_start = T_analytic
#solve
L, phi, T, table = fr._gpa_rotation.GPA(M, T=T_analytic, vgQ=vgQ, rotation_method='orthogonal')
#comparison
if np.allclose(T,T_analytic):
    print(True)
else:
    it_optim = vgQ(A=M, T=T)[0]
    an_optim = vgQ(A=M, T=T_analytic)[0]
    #print('Iterative algorithm optim: %f' % it_optim)
    #print('Analytic optim: %f' % an_optim)
    if it_optim<an_optim:
        print('Iterative algorithm is better.')
    else:
        print('Analytic result is better.')

#varimax rotation
L1,T= fr.rotate_factors(M,'varimax')
#varimax rotation using oblimin family instead of the orthomax family
L2,T= fr.rotate_factors(M,'oblimin',1,'orthogonal')
print(np.allclose(L1,L2,atol=1e-4))