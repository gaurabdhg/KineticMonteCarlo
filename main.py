import numpy as np
from fccgridmaker import zhalf,zfull
from supportmodules import *

#define the constants
density=8.96 #g/cm**3
avogadro=6.023*10**23 #atoms/mol
boltzmann=8.62*10**-5 #ev/atom K
Temp=np.linspace(300,600,51) #K
Time=1 #second
Atomicmass=63.5 #g/mol
Energy_vf=1.27 #ev/atom
Energy_vm=0.74 #ev/atom
length=100*10**-7 #cm  100nm
cubeside=100
radius=1.27*10**-8  #127picometer
b=.254          #.254nm or  2.54 amgstorm min distance between atoms
lattice=3.6*10**-8 #3.6 angstrom
lc=.36    #.36 nm
gasconstant=8.3144 #J/ K mol

N=Nofsites(density,avogadro,length,Atomicmass)

z=list()
alpositions=list()
zcount=len(z)
limit=200

while zcount<limit:
    z.append(zfull(100,lc))
    if limit<100:
        alpositions.append((alcods(z[-1])))
    z.append(zhalf(100,lc))
    if limit<100:
        alpositions.append((alcods(z[-1])))
    zcount +=lc

ND=list()   #defect numbers
dcods=list() #defect coordinates

for x in range(50):
    ND.append(defectnos(N,Energy_vf,Temp[x],boltzmann))
print(ND)
r=0   #temporary storage variable
for p in ND:
    dcods.append(defectcods(z,int(p-r)))
    r=p

for i,j in zip(np.linspace(0,1,51),Temp):
    probability=jumprob(boltzmann,j)
    for k in dcods:
        random.ramdom




