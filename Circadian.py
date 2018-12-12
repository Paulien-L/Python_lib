'''
Dynamical system implementing Goldbeter circadian rhythm model.
Generates plot of rate reactions over time.
'''

import numpy as np
from scipy.integrate import odeint
from matplotlib.pyplot import show, figure

#Define parameters
vs, vm, vd = 0.76, 0.65, 0.95
ks, k1, k2 = 0.38, 1.9, 1.3
V1, V2, V3, V4 = 3.2, 1.58, 5, 2.5

Km, Kd, Kl = 0.5, 0.2, 1
K1, K2, K3, K4 = 2, 2, 2, 2

n = 4

#Defining starting values
MP0, P00, P10, P20, PN0 = 0.5, 0.5, 0.5, 0.5, 0.5

t = np.linspace(0, 72, 200)

def deriv(y, t, vs, vm, vd, ks, k1, k2, V1, V2, V3, V4, Km, Kd, Kl, K1, K2, K3, K4, n):
    MP, P0, P1, P2, PN = y
    dMPdt = (vs*(Kl**n/((Kl**n)+(PN**n)))) - (vm*(MP/(Km+MP)))
    dP0dt = (ks*MP) - (V1*(P0/(K1+P0))) + (V2*(P1/(K2+P1)))
    dP1dt = (V1*(P0/(K1+P0))) - (V2*(P1/(K2+P1))) - (V3*(P1/(K3+P1))) + (V4*(P2/(K4+P2)))
    dP2dt = (V3*(P1/(K3+P1))) - (V4*(P2/(K4+P2))) - (k1*P2) + (k2*PN) - (vd*(P2/(Kd+P2)))
    dPNdt = (k1*P2) - (k2*PN)
    return dMPdt, dP0dt, dP1dt, dP2dt, dPNdt

y0 = [MP0, P00, P10, P20, PN0]

#Integrate equations over time grid with odeint
sol = odeint(deriv, y0, t, args=(vs, vm, vd, ks, k1, k2, V1, V2, V3, V4, Km, Kd, Kl, K1, K2, K3, K4, n))
MP, P0, P1, P2, PN = sol.T

PT = P0, P1, P2, PN

#Plot integrated functions
fig1 = figure(facecolor='w')
ax1 = fig1.add_subplot(111, axisbelow=True)
ax1.plot(t, MP, 'b', alpha=0.5, lw=2, label='PER mRNA')
ax1.plot(t, P0, 'r', alpha=0.5, lw=2, label='unphosporylated PER')
ax1.plot(t, P1, 'g', alpha=0.5, lw=2, label='phosphorylated PER')
ax1.plot(t, P2, 'y', alpha=0.5, lw=2, label='diphosphorylated PER')
ax1.plot(t, PN, 'm', alpha=0.5, lw=2, label='nuclear PER')
ax1.set_xlabel('Time/h')
ax1.set_ylabel('PER forms')
legend1 = ax1.legend()
legend1.get_frame().set_alpha(0.5)
show()