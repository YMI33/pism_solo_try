# for thickness experiment
# cdo -expr,'thk=0' ../pism_Greenland_5km_v1.1.nc ../testfile/temp.nc
# cdo replace ../pism_Greenland_5km_v1.1.nc ../testfile/temp.nc ../testfile/input_file_0thk.nc

# for calving experiment
#cdo setmisstoc,0 -ifthen -gec,-350 -selname,topg ../pism_Greenland_5km_v1.1.nc -expr,'thk=1' ../pism_Greenland_5km_v1.1.nc ../testfile/temp.nc
#cdo -merge -expr,'topg=-1' ../pism_Greenland_5km_v1.1.nc ../testfile/temp.nc ../testfile/mask_for_calving.nc

# for temperature input
amp=20

cdo -selname,ice_surface_temp ../pism_Greenland_5km_v1.1.nc  ../testfile/temp/temp0.nc
cdo -selname,precipitation ../pism_Greenland_5km_v1.1.nc  ../testfile/temp/ptemp0.nc
jloop=0
for((iloop=1;iloop<=1000;iloop++));
do
    phase=`echo "scale=10;"$amp"*s(-"$iloop"/50*3.1415)"|bc -l`
    mon="-"$iloop
    echo $phase
    cdo -mergetime -setyear,$mon -addc,$phase -selname,ice_surface_temp ../pism_Greenland_5km_v1.1.nc ../testfile/temp/temp$jloop.nc ../testfile/temp/temp$iloop.nc
    cdo -mergetime -setyear,$mon -selname,precipitation ../pism_Greenland_5km_v1.1.nc ../testfile/temp/ptemp$jloop.nc ../testfile/temp/ptemp$iloop.nc
    rm ../testfile/temp/temp$jloop.nc ../testfile/temp/ptemp$jloop.nc
    let jloop=$jloop+1
done
#cdo -merge ../testfile/temp/ptemp$jloop.nc ../testfile/temp/temp$jloop.nc ../testfile/sin_forcing_tem_pre.nc
