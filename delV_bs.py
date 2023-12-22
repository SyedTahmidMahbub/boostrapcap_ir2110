import numpy as np

D = 0.4
Tperiod = 100e-6
Ton = D * Tperiod
V0 = 11.403

Cboostrap = 1e-6
Qg_FET = 45e-9
Rg_on = 1031
Ibs = 280e-6

dV_Qg = -Qg_FET/Cboostrap
dV_Rg = -V0 * (1 - np.exp(-Ton/Rg_on/Cboostrap))
dV_Ibs = -Ibs/Cboostrap * Ton

V_final = V0 + dV_Qg + dV_Rg + dV_Ibs
print("Droop sources:")
print(f"  Gate charge: {dV_Qg :.3f} V")
print(f"  Gate resistor: {dV_Rg :.3f} V")
print(f"  Ibs: {dV_Ibs :.3f} V")

print(f"Droops from {V0 :.3f} V to {V_final :.3f} V")
