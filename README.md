# TMA4121
<h1>Numerical analysis of Poission equation</h1>

I denne numeriske analysen har jeg tatt for meg poissonligningen for å modellere det elektriske potensialet rundt en punktladning. 
Området jeg har sett på er sirkulært med da punktladningen i sentrum. Jeg har valgt å vise potensialet i 2D-figur ettersom jeg slet med å vise 3D figur i python...
Jeg begynte med å søke rundt på ulike PDE-er som ikke var direkte pensum og kom frem til Poisson-ligningen. Det var i tillegg spennende når jeg fant et eksempel direkte
knyttet opp mot elektronikk-studiene.

Jeg begynte med å finne noen gode kilder, blant annet: R. E. Hunt (2002), Cambridge university, http://ael.cbnu.ac.kr/lectures/graduate/adv-em-1/2018-1/lecture-notes/electrostatics-1/ch4-electrostatics-1-appendix-C-numerical-sol-poisson.pdf, og wikipediasiden om Poisson ligningen https://en.wikipedia.org/wiki/Poisson%27s_equation. Jeg brukte også litt mer indirekte denne siden for inspirasjon: https://www.studysmarter.co.uk/explanations/physics/electromagnetism/poisson-equation/.
Jeg fant også noen som numerisk hadde løst den: http://ael.cbnu.ac.kr/lectures/graduate/adv-em-1/2018-1/lecture-notes/electrostatics-1/ch4-electrostatics-1-appendix-C-numerical-sol-poisson.pdf, men jeg må si at jeg skjønte ikke mye av den numeriske løsningen her.

Hunt (side 19-22) forklarte veldig nøye alt som trengtes å forstå for å løse problemet numerisk. Det var her jeg tok meste inspirasjonen fra, i tillegg til at den viktigste kodelinjen hentet jeg herifra som er kommentert direkte i koden.

Når det gjelder selve python-kodingen og matplotlib bruken brukte jeg jevnlig matplotlib sin egen side: https://matplotlib.org/stable/, blant annet får å vise grafen og "colorbar"-en riktig og med farger jeg syntes passet. 

Her er koden og resultat:
"""
@author: Isak Olav Sjøberg

"""
import numpy as np
from matplotlib import pyplot as plt

Nx, Ny = 100, 100
radius = 0.5 

x = np.linspace(-1, 1, Nx)
y = np.linspace(-1, 1, Ny)
R = np.sqrt(x**2 + y**2) 
f = np.zeros((Ny, Nx))
f[Ny//2, Nx//2] = 1e5  #VIKTIG- Setter punktladningen i midten av sirkelen til å være 1*10^5
f[R > radius] = 0  
delta_x = 1.0 / (Nx - 1)
delta_x2 = delta_x**2  
u = np.zeros((Ny, Nx))

for i in range(5000):
    u_old = u.copy() #u.copy() er en måte å kopiere ett array på, veldig nttig. 
                    #Her f.eks får vi da hele tiden det gamle arrayet slik at vi hele tiden får lagret det.
    u[1:-1, 1:-1] = (u_old[1:-1, 2:] + u_old[1:-1, :-2] + u_old[2:, 1:-1] + u_old[:-2, 1:-1] - f[1:-1, 1:-1] * delta_x2) / 4
    #Linjen over er basert på denne fra cambridge university: Φi+1,j + Φi−1,j + Φi,j+1 + Φi,j−1 − 4Φi,j = σ(xi, yj)δx2.
    
fig = plt.figure(dpi=150) #DPI = dots per pixel som betyr basically at hvis du doble dpi-en så dobles antall dotter på figuren.
ax = fig.add_subplot()
contour = ax.contourf(x, y, u, 40, cmap='magma')
fig.colorbar(contour)  #Relative mål
ax.set_title('Elektrostatisk potensialfordeling')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()


Resultat:
![image](https://github.com/isakosjoberg/TMA4121/assets/154343100/d1abbace-b162-45ee-8df5-fdea25f36d62)




