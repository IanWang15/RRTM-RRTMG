# write data into a hdf5 file
# input files:
# heating rate: heatrate_all.txt
# other input constant gases: intpltgas.txt
# pressure: heatrate_pressure.txt
# filename: inputmlslist.txt
# output file: rrtm_simulation.h5


import numpy as np
import h5py
 
arr0 = np.loadtxt('../dat/heatrate_all.txt')
pressure = np.loadtxt('../dat/heatrate_pressure.txt')
with open('../dat/inputmlslist.txt') as f:
    filelist = f.readlines()

datelist = np.zeros(len(filelist))
for i in range(len(filelist)):
    datelist[i] = int(filelist[i][-7:-1])

datelist = datelist.astype('int')
#print(datelist[0])
gas = np.loadtxt('intpltgas.txt')

#print(np.shape(arr0))
#print(np.shape(pressure))
#print(np.shape(datelist))
#print(np.shape(gas))

#pressure = gas[1:50,0]
#h2o = gas[1:50,1] * 10**-6
co2 = gas[1:50,2]
#o3 = gas[1:50,3] * 10**-6
n2o = gas[1:50,4]
co = gas[1:50,5]
ch4 = gas[1:50,6]
o2 = gas[1:50,7]
density = gas[1:50,8]

#print(np.shape(o2))
 
with h5py.File('../dat/rrtm_simulation.h5', 'w') as f:
    f.create_dataset('heating_rate(K_day-1)', data = arr0)
    f.create_dataset('pressure(mb)', data = pressure)
    f.create_dataset('date', data = datelist)
    f.create_dataset('CO2', data = co2)
    f.create_dataset('N2O', data = n2o)
    f.create_dataset('CO', data = co)
    f.create_dataset('CH4', data = ch4)
    f.create_dataset('O2', data = o2)
    f.create_dataset('number_density', data = density)

