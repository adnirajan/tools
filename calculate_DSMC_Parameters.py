#!/bin/python3
# Python Scirpt to estimate input parameters to SPARTA
# Nirajan Adhikari (03-03-2020)

import math

print ("Hello! Parameter setup scripts")

# Constants
NA = 6.0221409E+26 #/* in terms of kmol */
Kb = 1.38064852E-23 #/* Boltzmann Constant */
Ru = 8.31434E+3    #/* Universal_Gas_Constant J/kmol-K*/

# Freestream Conditions
P_inf = 535.85*2.47	#Pa
T_inf = 300.0		#K
V_inf = 100.0 		#m/s
L_ref = 0.2e-3		#m 
MW    = 28.0  	#kg/kmol
d_ref  = 4.17E-10 	#m

# Domain Boundaries
Lx = 8.0e-3
Ly = 2.0e-3

# Calculate Parameters
# number density
rho_inf	= P_inf /(Ru/MW * T_inf)
n_inf	= NA/MW * rho_inf
print("rho = ", '{:.3e}'.format(rho_inf), " number_density = ", '{:.3e}'.format(n_inf))
print("m = ", '{:.3e}'.format(MW/NA))

# Mean_Free_Path
mfp = 1.0/(2.0**0.5 * n_inf * math.pi * d_ref**2.0) # Hard-Sphere Lamba_HS
Kn = mfp/L_ref
print("mfp = ", '{:.2e}'.format(mfp), " Knudsen number = ", '{:.2e}'.format(Kn))

# Grid Size
NCXmin = Lx/(mfp/3.0) # Grid size should be atleast 1/3rd mfp
NCYmin = Ly/(mfp/3.0)
print("Grid Size: NCXmin = ", int(NCXmin), " NCYmin = ", int(NCYmin))

# Time Step
# Collision controlled time step
C_avg = math.sqrt(8.0 * Kb * T_inf /(math.pi * MW/NA)) # Thermal Velocity
mct = mfp/C_avg # mct = tau_c,HS = Lambda_HS/C_avg

# Grid controlled time step
dx = Lx/NCXmin
mtt = dx/V_inf	# mtt = tau_tt = dx/V_inf
print("mct = ", '{:.2e}'.format(mct), " mtt = ", '{:.2e}'.format(mtt), " dt = min(mct,mtt) = ", '{:.2e}'.format(min(mct,mtt)));

# Fnum
V = Lx * Ly * 1.0;
Nreal = V * n_inf;
NSim = 100.0 * NCXmin * NCYmin * 1.0 # Each cell contain 100 simulated particles (coarse)
Fnum = Nreal/NSim
print("Fnum (100 simulators/cell) = ", '{:.3e}'.format(Fnum))
