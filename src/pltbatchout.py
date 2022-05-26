# data is from RRTM output file over multiple days
# plot a figure: x: date; y: pressure; colorbar: heating rate
# also save all data to a single file

import matplotlib as mpl
mpl.use('Agg')
import math
import numpy as np
import matplotlib.pyplot as plt

def readdat(filepath, dat):
    with open(filepath,'r') as f:
#    lines=f.read().splitlines()
#    print(lines)

        lines=f.readlines()
#    print(lines)
#    print(len(lines))
        for i in range(linestart,lineend):
            varstr = lines[i].split()
            var = [float(i) for i in varstr]
#        print(var)
            for j in range(6):
                dat[j,i-linestart]    = var[j]
    return dat

linestart = 3
lineend   = 52
linenum   = lineend - linestart
arr    = np.zeros(shape=(489,linenum))
tmp    = np.zeros(shape=(6,linenum))
#level    = np.zeros(linenum)
#pressure = np.zeros(linenum)
#upflx    = np.zeros(linenum)
#dwnflx   = np.zeros(linenum)
#netflx   = np.zeros(linenum)
#rate     = np.zeros(linenum)

f = open('./inputmlslist.txt', "r")
filelist = f.readlines()

print(len(filelist))
#print(filelist[0])

for i in range(489):
    tmp = readdat('../dat/output/'+filelist[i][:-1],tmp)
    arr[i,:] = tmp[5,:]

#print(arr[1,:])
np.savetxt('../dat/heatrate_all.txt', arr)
np.savetxt('../dat/heatrate_pressure.txt', tmp[1,:])

fig, ax = plt.subplots(figsize=(5, 5))

#im = ax.imshow(arr[:100,30:40])
im = ax.imshow(arr[366:466,30:40])
print(tmp[1,30:40])

# Show all ticks and label them with the respective list entries
#ax.set_xticks(np.arange(len(bands)))
#ax.set_xticklabels(labels=bands)
#ax.set_yticks(np.arange(len(bands)))
#ax.set_yticklabels(labels=bands)

# Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.

#ax.set_title("heating rate 202101 - 202103")
ax.set_title("heating rate 202201 - 202203")

# Create colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('heating rate', rotation=-90, va="bottom")

#pngname = "../fig/"+"heatrate_2021.png"
pngname = "../fig/"+"heatrate_2022.png"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')
