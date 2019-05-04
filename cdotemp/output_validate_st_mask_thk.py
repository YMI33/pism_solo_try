from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from matplotlib import pyplot as plt

var_name = "usurf"
titext = ["Control run","10K down Exp.","Exp.-Ctr."]
offset = 0
clim = [[0,4000],[0,4000],[-300,300]]
filename = "./ex_comp/Comparison_add10exp_ctrrun_"+var_name+".eps"
yr     = 249

var = []
f = NetCDFFile("../ex_g20km_25ka_paleo.nc")
lat = np.squeeze(f.variables["lat"])
lon = np.squeeze(f.variables["lon"])
var.append( np.squeeze(f.variables[var_name]) - offset)
f = NetCDFFile("../ex_g20km_25ka_paleo_min10.nc")
lat2 = np.squeeze(f.variables["lat"])
lon2 = np.squeeze(f.variables["lon"])
var.append( np.squeeze(f.variables[var_name]) - offset)
var.append( var[1] - var[0]) 

# projection
map = Basemap(width=3e6,height=3e6,resolution='l',projection='laea',\
        lat_ts=60,lat_0=72,lon_0=-40)
map.drawcoastlines()
map.drawparallels(np.arange(-80.,81.,20.))
map.drawmeridians(np.arange(-180.,181.,20.))
x,y = map(lon,lat)

fig = plt.figure(figsize=[12,4])
# temperature
for t in range(3):
    plt.subplot(1,3,t+1)
    cs  = map.contourf(x,y,var[t][yr,:,:],cmap="bwr")
    cbr = map.colorbar(cs)
    plt.title(titext[t],fontsize=13)
    plt.clim(clim[t])
plt.suptitle(var_name)
#plt.savefig(filename, dpi=300,format="eps")
plt.show()

