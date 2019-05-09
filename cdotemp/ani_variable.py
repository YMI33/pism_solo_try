from mpl_toolkits.basemap import Basemap
import os
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from matplotlib import pyplot as plt

var_name = "ice_surface_temp"
titext = var_name 
offset = 0
level = np.arange(230,280,5)
clim = [230,280]
yr     = 0

f = NetCDFFile("../testfile/ex_g20km_25ka_0thk.nc")
lat2 = np.squeeze(f.variables["lat"])
lon2 = np.squeeze(f.variables["lon"])
var  = np.squeeze(f.variables[var_name]) - offset

# projection
map = Basemap(width=3e6,height=3e6,resolution='l',projection='laea',\
        lat_ts=60,lat_0=72,lon_0=-40)
map.drawcoastlines()
map.drawparallels(np.arange(-80.,81.,20.))
map.drawmeridians(np.arange(-180.,181.,20.))
x,y = map(lon2,lat2)

fig = plt.figure(figsize=[6,4])
# temperature
for yr in range(250):
    cs  = map.contourf(x,y,var[yr,:,:],level,cmap="bwr")
    cbr = map.colorbar(cs)
    titext = str(yr*100-25000) + "yr"
    plt.title(titext,fontsize=13)
    plt.clim(clim[0],clim[1])
    filename = "./ex_comp/"+var_name+str(1000+yr)
    plt.savefig(filename, dpi=150,format="png")

cmd = "convert -delay 15 ./ex_comp/"+var_name+"* /Users/zxie0012/Documents/ice_sheet_model/solo_model_test/variable_test/    evo_0thk_"+var_name+".gif" 
os.system(cmd)
