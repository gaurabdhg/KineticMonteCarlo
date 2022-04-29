import numpy as np

def zfull(lim,flc,z):
    hlc=flc/2
    #limx=limy=8
    xcood=np.arange(0,lim,flc)
    ycood=np.arange(0,lim,hlc)
    
    cood=list()
    county=0

    for i in ycood:
        if county>=555: 
            continue
        countx=0
        for k in xcood:

            if (county & 1):
                if (k+hlc)>lim-flc : 
                    continue
                cood.append([k+hlc,i,z])
                #cood.append([[countx,county],[k+hlc,i]])
            else:
                cood.append([k,i,z])
                #cood.append([[countx,county],[k,i]])


            countx +=1
        county+=1
    return cood

def zhalf(lim,flc,z):
    hlc=flc/2
    #limx=limy=8
    xcood2=np.arange(0,lim,flc)
    ycood2=np.arange(-hlc,lim,hlc)
    #zcood=np.arange(0,8,.5)
    cood2=list()
    county=0
    for i in ycood2:
        if county>555: continue
        countx=0
        for k in xcood2:
            if i<0: continue
            if (county & 1 ):
                if (k+hlc>lim-flc): continue
                #cood2.append([[countx,county-1],[k+hlc,i]])
                cood2.append([k+hlc,i,z])
            else:
                #cood2.append([[countx,county-1],[k,i]])
                cood2.append([k,i,z])
            countx +=1
        county+=1
    return cood2
