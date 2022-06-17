# the H2O and O3 are from MLS data in a IDL save file
# CO2, N2O, CO, CH4, O2, and number density are from
# summer mid-latitude atmosphere with iterpolation

from os.path import dirname, join as pjoin
import scipy.io as sio
from scipy.io import readsav
import numpy as np
import csv
import sys

if sys.argv[1]:
    filename = sys.argv[1]
else:
    print('no input file, enter debug mode')
    import pdb
    pdb.set_trace()
    print('stop here')

writelist = np.loadtxt('../dat/intpltgas.txt')
# pressure, h2o, co2, o3, n2o, co, ch4, o2, density
print(np.shape(writelist))
#print(writelist[0,:])
#print(writelist[-1,:])
#print(len(writelist))

#data_dir = pjoin(dirname(sio.__file__), 'tests', 'data')
data_dir = '/mnt/bigdrive/ywang0/dat/MLS/H2ON2OSO2/MLS_H2ON2OSO2idlsavefile/'

sav_fname = pjoin(data_dir, filename)

sav_data = readsav(sav_fname)
#print(sav_data['latgrid'][:])


pressure = 1000.*np.exp(-1.*sav_data['zmls'][:]/7.)
temp = sav_data['temp'][:]
h2o = sav_data['ztr1'][:] * 10**-6
o3 = sav_data['ztr5'][:] * 10**-6

f = open("tmpinputfile", "w")
# header
f.write('0        1         2         3         4         5         6         7         8         9 \n')
f.write('123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789- \n')
f.write('$ STANDARD MID-LATITUDE SUMMER ATMOSPHERE \n')
f.write('                                                 0                   0              3    0 \n')

t00 =("%.1f" % temp[0][13])

f.write(' '+str(t00)+' \n')
f.write(' 1 49    7  1.000000MIDLATITUDE SUMM H1=    0.00 H2=   70.00 ANG=   0.000 LEN= 0 \n')

# first line
p1 = ("%.4f" % pressure[1])
t1 =("%.2f" % temp[1][13])
p0 = ("%.4f" % pressure[0])
t0 =("%.2f" % temp[0][13])

f.write('   '+str(p1)+'        '+str(t1)+'                      '+str(p0)+' '+str(t0)+'        ')
p2 = ("%.3f" % ((pressure[1]+pressure[2])/2.))
t2 =("%.2f" % ((temp[1][13]+temp[2][13])/2.))
f.write(str(p2)+' '+str(t2)+'\n')

h5 = ("%.7E" % h2o[1][13])
h6 = ("%.7E" % o3[1][13])
f.write('  '+str(h5)+'  '+str("%.7E" % writelist[0,2])+'  '+str(h6))
for i in range(4,9):
    f.write('  '+str("%.7E" % writelist[0,i]))
f.write('\n')
# other lines
for i in range(2,50):
    var1 = ("%.4f" % pressure[i])
    var2 = ("%.2f" % temp[i][13])
    if pressure[i] > 99.99999:
        f.write('   '+str(var1)+'        '+str(var2)+'                                              ')
    elif  pressure[i] >= 9.9999:
        f.write('    '+str(var1)+'        '+str(var2)+'                                               ')
    elif  pressure[i] >= 0.:
        f.write('     '+str(var1)+'        '+str(var2)+'                                                ')
    var3 = ("%.3f" % ((pressure[i]+pressure[i+1])/2.))
    var4 = ("%.2f" % ((temp[i][13]+temp[i+1][13])/2.))
    f.write(str(var3)+' ' +str(var4)+'\n')

    var5 = ("%.7E" % h2o[i][13])
    var6 = ("%.7E" % o3[i][13])
    f.write('  '+str(var5)+'  '+str("%.7E" % writelist[i-1,2])+'  '+str(var6))
    for j in range(4,9):
        f.write('  '+str("%.7E" % writelist[i-1,j]))
    f.write('\n')

f.write('%%%%% \n')
f.write('123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789- \n')
f.close()
