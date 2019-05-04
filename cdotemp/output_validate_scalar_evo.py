from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from matplotlib import pyplot as plt

var_name = "delta_T"
titext = ["Control run","10K up Exp.","Exp.-Ctr."]
offset = 0
filename = "./ex_comp/Comparison_min100exp_ctrrun_"+var_name+".eps"

var = []
#f = NetCDFFile("../ts_g20km_25ka_paleo.nc")
f = NetCDFFile("../pism_dT.nc")
var.append( np.squeeze(f.variables[var_name]) - offset)
print(f)
tim = f.variables["time"]
#f = NetCDFFile("../ts_g20km_25ka_paleo_min10.nc")
f = NetCDFFile("../pism_dT_add10.nc")
var.append( np.squeeze(f.variables[var_name]) - offset)
var.append( var[1] - var[0]) 

fig = plt.figure(figsize=[12,4])
# temperature
for t in range(2):
    plt.subplot(1,2,t+1)
    cs  = plt.plot(tim,var[t],color="k")
    plt.title(titext[t],fontsize=13)
    plt.xlim(-25000,0)
plt.suptitle(var_name)
#plt.savefig(filename, dpi=300,format="eps")
plt.show()

