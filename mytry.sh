mpiexec -n 4 pismr -i pism_Greenland_5km_v1.1.nc -bootstrap \
-Mx 76 -My 141 -Mz 101 -Mbz 11 -z_spacing equal -Lz 4000 -Lbz 2000 -skip -skip_max 10 \
-grid.recompute_longitude_and_latitude false -grid.registration corner -ys -25000 -ye 0 \
-regrid_file g20km_10ka_hy.nc -regrid_vars litho_temp,thk,enthalpy,tillwat,basal_melt_rate_grounded \
-atmosphere searise_greenland,delta_T,paleo_precip -surface pdd -atmosphere_paleo_precip_file pism_dT.nc \
-atmosphere_delta_T_file pism_dT.nc \
-calving ocean_kill -ocean_kill_file pism_Greenland_5km_v1.1.nc -sia_e 3.0 -stress_balance sia \
-ts_file ts_g20km_25ka_paleo.nc -ts_times -25000:yearly:0 \
-extra_file ex_g20km_25ka_paleo.nc -extra_times -25000:100:0 \
-extra_vars diffusivity,temppabase,ice_surface_temp,bmelt,tillwat,velsurf_mag,mask,thk,topg,usurf,hardav,velbase_mag \
-o g20km_25ka_paleo.nc

