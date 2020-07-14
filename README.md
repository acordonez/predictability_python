# Predictability (Python)  
  
This is a demo of how to recreate some types of plots from my paper on sea ice predictability using Python instead of MATLAB. 

### Installation and running

1. Clone this repo
2. Obtain a sample file. I am using `b.e11.B20TRC5CNBDRD.f09_g16.013.cice.h.aice_nh.192001-200512.nc`, which I downloaded from https://www.earthsystemgrid.org/dataset/ucar.cgd.ccsm4.CESM_CAM5_BGC_LE.ice.proc.monthly_ave.html. Save this file in a subfolder called 'cesm_data'.
3. Generate the region mask by running `make_region_mask.py`
4. Run the jupyter notebook `ice_area_correlation_plots.ipynb`. If you are using a different LENS member, change the variable `cesm_data` to your file name.

### Dependencies

This repo relies on the following packages:
1. numpy
2. matplotlib.pyplot
3. mpt_toolkits.basemap
4. scipy
5. xarray
6. os
7. netCDF4
