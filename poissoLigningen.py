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
