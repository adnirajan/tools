/*********************************************************************
 *  *    UDF for Calculating Thermal Conductivity wth Constant Prandtl#  * *
 *  UDF 
 *  UDF 
 *  Models: 
 *   	
 *  Notes: 
		
 *  		Problems: 
 *  Nirajan Adhikari (10-11-2019)
 *********************************************************************/
#include "udf.h"
#include "sg.h"
/* Constants Definition */
#define PRANDTL 0.71
/* Thermal conductivity using constant Prandtl number */
DEFINE_PROPERTY(thermal_conductivity_const_prandtl, c, t)
{
#if !RP_HOST /* Does nothing in Serial */
	real Pr = PRANDTL;
	real ktc;
	real u_mu;
	real u_cp;
	u_cp = C_CP(c,t);
	u_mu = C_MU_L(c,t); 
	ktc = u_mu * u_cp / Pr;
	return ktc;
#endif
}
