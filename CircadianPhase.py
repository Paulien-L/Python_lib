'''
Dynamical system implementing Goldbeter circadian rhythm model.
Generates phase space plot.
'''


import numpy as np
from scipy.integrate import odeint
from matplotlib.pyplot import *

#Define parameters
vs, vm, vd = 0.76, 0.65, 0.95
ks, k1, k2 = 0.38, 1.9, 1.3
V1, V2, V3, V4 = 3.2, 1.58, 5, 2.5

Km, Kd, Kl = 0.5, 0.2, 1
K1, K2, K3, K4 = 2, 2, 2, 2

n = 4

#Defining starting values
MP0a, P00a, P10a, P20a, PN0a = 0.1, 0.25, 0.25, 0.25, 0.25
MP0b, P00b, P10b, P20b, PN0b = 1.9, 0.8, 0.8, 0.8, 0.8

#Range of time
t = np.linspace(0, 150, 300)

def deriv(y, t, vs, vm, vd, ks, k1, k2, V1, V2, V3, V4, Km, Kd, Kl, K1, K2, K3, K4, n):
    MP, P0, P1, P2, PN = y
    dMPdt = (vs*(Kl**n/((Kl**n)+(PN**n)))) - (vm*(MP/(Km+MP)))
    dP0dt = (ks*MP) - (V1*(P0/(K1+P0))) + (V2*(P1/(K2+P1)))
    dP1dt = (V1*(P0/(K1+P0))) - (V2*(P1/(K2+P1))) - (V3*(P1/(K3+P1))) + (V4*(P2/(K4+P2)))
    dP2dt = (V3*(P1/(K3+P1))) - (V4*(P2/(K4+P2))) - (k1*P2) + (k2*PN) - (vd*(P2/(Kd+P2)))
    dPNdt = (k1*P2) - (k2*PN)
    return dMPdt, dP0dt, dP1dt, dP2dt, dPNdt

y0a = [MP0a, P00a, P10a, P20a, PN0a]
y0b = [MP0b, P00b, P10b, P20b, PN0b]

#Integrate equations over time grid with odeint
sola = odeint(deriv, y0a, t, args=(vs, vm, vd, ks, k1, k2, V1, V2, V3, V4, Km, Kd, Kl, K1, K2, K3, K4, n))
solb = odeint(deriv, y0b, t, args=(vs, vm, vd, ks, k1, k2, V1, V2, V3, V4, Km, Kd, Kl, K1, K2, K3, K4, n))

MPa, P0a, P1a, P2a, PNa = sola.T
MPb, P0b, P1b, P2b, PNb = solb.T

PTa = P0a + P1a + P2a + PNa
PTb = P0b + P1b + P2b + PNb

fig = figure(facecolor='w')
subplt = fig.add_subplot(111, axisbelow=True)
subplt.plot(PTa, MPa)
subplt.plot(PTb, MPb)
subplt.set_xlabel('Total PER protein')
subplt.set_ylabel('PER mRNA')
show()