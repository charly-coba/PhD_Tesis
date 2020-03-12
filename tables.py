import numpy as np

from tabulate import tabulate



#
# survey, redshift, R, Ngal,spatial_res,FoV
#

muse = ["AMUSING++", "0.001<z<0.1", 3000, 700, "seeing limited","60x60","4800--9300"]
califa = ["CALIFA", "0.005<z<0.03", "850,1650", 667, 2.5,"78x73", "3745--7500"]
manga = ["MaNGA", "0.025<z<0.15", "1400-2600", 1e4, "2.54,2.48","7-32", "4000--9000"]
sami = ["SAMI", "0.004<z<0.092", "1700,4500", 1559, 2.16,"15x15", "3700--7300"]


table = [sami,manga,califa,muse]
headers=["Survey","redshift", "R", "N_gal", "FWHM (arcsec)","FoV (arcsec)","lambda_range (Angs)"]

print(tabulate(table,headers = headers,tablefmt="latex_booktabs"))
