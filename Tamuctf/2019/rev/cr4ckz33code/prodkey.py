#!/usr/bin/python3


import angr
import claripy

#M4119-81178-11191-61BB2-11188

p = angr.Project("./prodkey")

#addr=,add_options={angr.options.LAZY_SOLVES}
st = p.factory.blank_state(addr=0x0000000000400DFC,add_options={angr.options.LAZY_SOLVES})
x = claripy.BVS('input', 8*29)

"""
return a1[5] == 0x2D && a1[11] == 0x2D && a1[17] == 0x2D && a1[23] == 0x2D;
"""

st.solver.add(x[5] ==  0x2D)
st.solver.add(x[11] == 0x2D)
st.solver.add(x[17] == 0x2D)
st.solver.add(x[23] == 0x2D)

"""
return (unsigned int)(a1[1] - 48) <= 9
      && (unsigned int)(a1[4] - 48) <= 9
      && (unsigned int)(a1[6] - 48) <= 9
      && (unsigned int)(a1[9] - 48) <= 9
      && (unsigned int)(a1[15] - 48) <= 9
      && (unsigned int)(a1[18] - 48) <= 9
      && (unsigned int)(a1[22] - 48) <= 9
      && (unsigned int)(a1[27] - 48) <= 9
      && (unsigned int)(a1[28] - 48) <= 9;
"""


st.solver.add(x[1]-48 <= 9)
st.solver.add(x[4]-48 <= 9)
st.solver.add(x[6]-48 <= 9)
st.solver.add(x[9]-48 <= 9)
st.solver.add(x[15]-48 <= 9)
st.solver.add(x[18]-48 <= 9)
st.solver.add(x[22]-48 <= 9)
st.solver.add(x[27]-48 <= 9)
st.solver.add(x[28]-48 <= 9)


st.solver.add(x[20] == 66)
st.solver.add(x[21] == 66)
st.solver.add(x[27] == ord('8'))
st.solver.add(x[28] == ord('8'))

st.solver.add(x[0] == 0x4D)

sm = p.factory.simulation_manager(st)

sm.explore(find=0x0000000000400DEB,avoid=0x0000000000400DF2)

found = sm.found[0]


if found:
    print (found.posix.dumps(0))
