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
lineend   = 55
linenum   = lineend - linestart
dat1    = np.zeros(shape=(6,linenum))
dat2    = np.zeros(shape=(6,linenum))
#level    = np.zeros(linenum)
#pressure = np.zeros(linenum)
#upflx    = np.zeros(linenum)
#dwnflx   = np.zeros(linenum)
#netflx   = np.zeros(linenum)
#rate     = np.zeros(linenum)

dat1 = readdat('../dat/tmp1.txt',dat1)
dat2 = readdat('../dat/tmp2.txt',dat2)

#print(upflx)
fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(12, 7))

ax[0].plot(dat1[2,:], dat1[1,:],c='black', linewidth=1.5, label='orig')
ax[0].plot(dat2[2,:], dat2[1,:],c='red', linewidth=1.5, label='added H2O')
ax[0].set_xlabel('upward flux (W/m2)', fontsize=10)
ax[0].set_ylabel('pressure (mb)', fontsize=12)
ax[0].set_ylim(0,121)
ax[0].invert_yaxis()
ax[0].set_xlim(275,285)
ax[0].legend()

ax[1].plot(dat1[3,:], dat1[1,:],c='black', linewidth=1.5)
ax[1].plot(dat2[3,:], dat2[1,:],c='red', linewidth=1.5)
ax[1].set_xlabel('downward flux (W/m2)', fontsize=10)
ax[1].set_ylim(0,121)
ax[1].invert_yaxis()
ax[1].set_xlim(0,20)
ax[1].set_title('                   Wavenumbers: 10.0 - 3250.0/cm; standard mid-latitude summer atmosphere',fontsize=12)

ax[2].plot(dat1[4,:], dat1[1,:],c='black', linewidth=1.5)
ax[2].plot(dat2[4,:], dat2[1,:],c='red', linewidth=1.5)
ax[2].set_xlabel('net flux (W/m2)', fontsize=10)
ax[2].set_ylim(0,121)
ax[2].invert_yaxis()
ax[2].set_xlim(259,281)

ax[3].plot(dat1[5,:], dat1[1,:],c='black', linewidth=1.5)
ax[3].plot(dat2[5,:], dat2[1,:],c='red', linewidth=1.5)
ax[3].set_xlabel('heating rate (degree/day)', fontsize=10)
ax[3].set_ylim(0,121)
ax[3].invert_yaxis()
ax[3].set_xlim(-4,0)

#plt.xscale("log")
#plt.yscale("log")

#plt.xticks(fontsize=14)
#plt.yticks(fontsize=14)

#plt.text(1, 0.000000001, 'alpha = 1.2; beta = 0.06', fontsize=12)

#ax.set_xticks([1,10,100])
#ax.set_yticks([-15,-10,-5,0,5,10,15,20,25])
#plt.colorbar(mm, cax=cbar_ax)
#ax.set_xlim(-0.02,0.1)
#ax.set_ylim(0.0000000001,1)

print('start saving')

pngname = "../fig/"+"fig_outrrtm_watervapor.png"
print("save ", pngname)
plt.savefig(pngname, bbox_inches='tight')
#plt.show()


