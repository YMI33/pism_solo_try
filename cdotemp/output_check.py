from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from matplotlib import pyplot as plt

var_name = "thick"
titext = var_name 
offset = 0
clim = [0,4000]
yr     = 249

f = NetCDFFile("../ex_g20km_25ka_paleo_min10.nc")
lat2 = np.squeeze(f.variables["lat"])
lon2 = np.squeeze(f.variables["lon"])
var  = np.squeeze(f.variables[var_name]) - offset)

# projection
map = Basemap(width=3e6,height=3e6,resolution='l',projection='laea',\
        lat_ts=60,lat_0=72,lon_0=-40)
map.drawcoastlines()
map.drawparallels(np.arange(-80.,81.,20.))
map.drawmeridians(np.arange(-180.,181.,20.))
x,y = map(lon,lat)

fig = plt.figure(figsize=[12,4])
# temperature
for t in range(1):
    cs  = map.contourf(x,y,var[yr,:,:],cmap="bwr")
    cbr = map.colorbar(cs)
    plt.title(titext,fontsize=13)
    plt.clim(clim)
#plt.savefig(filename, dpi=300,format="eps")
plt.show()

