from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from matplotlib import pyplot as plt

f = NetCDFFile("../pism_Greenland_5km_v1.1.nc")
lat = np.squeeze(f.variables["lat"])
lon = np.squeeze(f.variables["lon"])
var = np.squeeze(f.variables["ice_surface_temp"])
map = Basemap(width=3e6,height=3e6,resolution='l',projection='laea',\
        lat_ts=60,lat_0=72,lon_0=-40)
map.drawcoastlines()
map.drawparallels(np.arange(-80.,81.,20.))
map.drawmeridians(np.arange(-180.,181.,20.))
x,y = map(lon,lat)
cs  = map.contourf(x,y,var)
cbr = map.colorbar(cs)
plt.show()

