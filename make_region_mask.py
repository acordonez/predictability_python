'''
make_region_mask.py

Creates a regional mask for the arctic based on the
geometry from a CESM run. Saves the mask as a numpy
file called ice_region_mask.npy

Regions:
1. GIN Seas
2. Barents/Kara
3. Bering & Sea of Okhotsk
4. Hudson Bay
5. Baffin
6. Central Arctic
'''

import numpy as np
from netCDF4 import Dataset

# load example ice file
cesm_data = '../cesm_data/b.e11.B20TRC5CNBDRD.f09_g16.013.cice.h.aice_nh.192001-200512.nc'
aice = Dataset(cesm_data)

lat = aice.variables['TLAT'][:]
lon = aice.variables['TLON'][:]

greenland = np.where(((lon >= 315) | (lon < 20)) & (lat < 80),1,0)
kara = np.where((lon >= 20) & (lon < 100) & (lat < 80),2,0)
seamask = np.maximum(greenland, kara)
bering = np.where((lon >= 90) & (lon < 225) & (lat < 65),3,0)
seamask = np.maximum(seamask, bering)
hudson = np.where((lon < 295) & (lon >= 260) & (lat < 70),4,0)
seamask = np.maximum(seamask, hudson)
baffin = np.where((hudson == 0) & (lat < 80) & (lat > 40) & (lon < 315) & (lon > 270),5,0)
seamask = np.maximum(seamask, baffin)
arctic = np.where((seamask == 0) & (((lat > 65) & (lon > 90)) | ((lat > 65) & (lon > 270)) | ((lat > 70) & (lon <=90) & (lon >= -90))), 6, 0)
seamask = np.maximum(seamask, arctic)

np.save('ice_region_mask.npy', seamask)