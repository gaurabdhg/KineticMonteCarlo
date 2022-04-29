import random
import math

def alcods(plane):
    p=int(0.1*len(plane))
    alcoods=random.choices(plane,k=p)
    return alcoods

def Nofsites(rho,na,l,amu):

    return rho*na*l**3/amu

def defectnos(Nos,Evf,Tempr,Kb):

    return math.exp(-Evf/(Tempr*Kb))/Nos


def defectcods(grid,dfoo):
    
    return random.choices(grid,k=dfoo)


def jumprob(kB,dT):
    return math.exp(-137100/kB*dT)


