import random,math

def alcods(plane):
    p=int(0.1*len(plane))
    alcoods=random.choices(plane,k=p)
    return alcoods

def Nofsites(rho,na,v,amu):

    return rho*na*v/amu

def defectnos(Nos,Evf,Tempr,Kb):

    return math.exp(-Evf/(Tempr*Kb))/Nos


def defectcods(grid,dfoo):
    
    return random.choices(grid,k=dfoo)
