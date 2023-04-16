# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:50:18 2023

@author: Virgil
"""


'''
SOURCES:
https://electronics.stackexchange.com/questions/601136/ltspice-modeling-an-led
https://ltwiki.org/files/SPICEdiodeModel.pdf

Semiconductor device modeling with SPICE
by Massobrio, Giuseppe
'''

import numpy as np
from scipy.special import lambertw
import matplotlib.pyplot as plt

Id1 = 1e-3 #[A]
Id2 = 30e-3  #[A]
Id3 = 1000e-3 #[A]

V1 = 1.25      #[V]
V2 = 1.5       #[V]
V3 = 2.875       #[V]
Vth = 0.0259   #[V]

'''
Solving for necessary parameters
'''
A1 = Id1-Id2
B1 = Vth * np.log(Id1/Id2)

A2 = Id1-Id3
B2 = Vth * np.log(Id1/Id3)


'''
Ideality factor (N)
'''
N = (A1 * (V1-V3) - A2 * (V1-V2)) / (A1*B2 - A2*B1)


'''
Internal series resistance (Rs)
'''
Rs = (B1 * (V1-V3) - B2 * (V1-V2)) / (A2*B1 - A1*B2)


'''
Saturation current
'''
Isat = Id1 * np.exp(-(V1-Rs*Id1)/(N*Vth))


'''
Plotting IV characteristic of diode
'''
#VF from known currents
Idv = np.array([Id1,Id2,Id3])
VF = Rs * Idv + N * Vth * np.log(Idv/Isat)
plt.figure()
plt.semilogy(VF, Idv,'ro')


#Mapping the IV characteristic over a wider voltage interval


Id = np.arange(1e-4,10,0.0001)


plt.semilogy(Rs * Id + N * Vth * np.log(Id/Isat),Id,'b-',lw=2)
plt.grid(visible=True,which='both')
plt.ylim([1e-4,10])
plt.xlim([0,3.5])

plt.title("Simulated IV characteristic of LED VSLY5940")
plt.xlabel('$V_{F}\;[V]$')
plt.ylabel('$I_{F}\;[A]$')
plt.show()
print(f"Rs:{Rs}[ohm]\nIsat:{Isat}[A]\nN:{N}")

#Testing the accuracy of our model

VFt = np.array([2,2.5])
Idt = np.real(N * Vth / Rs * lambertw((Rs*Isat)/(N*Vth)*np.exp(VFt/(N*Vth))))
plt.figure()
plt.semilogy(VFt,Idt,'rs')
plt.semilogy(Rs * Id + N * Vth * np.log(Id/Isat),Id,'b-',lw=2)
plt.grid(visible=True,which='both')
plt.ylim([1e-4,10])
plt.xlim([0,3.5])

plt.title("Simulated IV characteristic of LED VSLY5940")
plt.xlabel('$V_{F}\;[V]$')
plt.ylabel('$I_{F}\;[A]$')
