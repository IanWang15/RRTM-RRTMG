# reading the vertical profile from the INPUT file and plot

import math
import numpy as np
import matplotlib.pyplot as plt

linestart = 7
lineend   = 109
linenum   = int((lineend - linestart)/2)
pressure    = np.zeros(linenum)
h2o1    = np.zeros(linenum)
h2o2    = np.zeros(linenum)

with open('../dat/input_rrtm_MLS','r') as f:
#    lines=f.read().splitlines()
#    print(lines)

    lines=f.readlines()
#    print(lines)
#    print(len(lines))
    ii = 0
    for i in range(linestart,lineend,2):
        varstr = lines[i].split()
        var = [i for i in varstr]
#        print(var)
        pressure[ii] = float(var[0])

        varstr = lines[i+1].split()
        var = [float(i) for i in varstr]
#        print(var)
        h2o1[ii] = var[0]
        ii = ii + 1
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4,7))

ax.plot(h2o1, pressure,c='black', linewidth=1.5,label='orig')
ax.set_xlabel('water vapor', fontsize=10)
ax.set_ylabel('pressure (mb)', fontsize=12)
ax.set_ylim(0,121)
ax.invert_yaxis()
ax.set_xlim(0.000001,0.00002)
ax.legend()

print('start saving')

pngname = "../fig/"+"fig_in_h2o.png"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')
#plt.show()


