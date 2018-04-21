'''
Pharmacokinetic four-compartment model simulation.
Compartments simulated: gut (G), central (C), periphery (P), excretion (E)
Based on SIR-model example
'''

import numpy as np
from scipy.integrate import odeint
from matplotlib.pyplot import show, figure

#Define initial values of compartments and rate constants
G0, C0, P0, E0 = 1.8, 0, 0, 0
kg, kc, kp, ke = 5, 2, 2, 0.4

#Set space of simulation
t = np.linspace(0, 3, 200)

def deriv(y, t, kg, kc, kp, ke):
    G, C, P, E = y
    dGdt = -(kg*G)
    dCdt = (kg*G) - ((kc+ke)*C) + (kp*P)
    dPdt = (kc*C) - (kp*P)
    dEdt = (ke*C)
    return dGdt, dCdt, dPdt, dEdt

y0 = [G0, C0, P0, E0]

#Integrate equations over time grid with odeint
sol = odeint(deriv, y0, t, args=(kg, kc, kp, ke))
G, C, P, E = sol.T

#Plot G(t), C(t), P(t), E(t)
fig = figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, G, 'b', alpha=0.5, lw=2, label='Gut')
ax.plot(t, C, 'r', alpha=0.5, lw=2, label='Central')
ax.plot(t, P, 'g', alpha=0.5, lw=2, label='Periphery')
ax.plot(t, E, 'y', alpha=0.5, lw=2, label='Excretion')
ax.set_xlabel('Time')
ax.set_ylabel('Concentration')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
show()
