from numpy import array
from PIL import Image
from random import randint
from random import choices
from datetime import datetime as dt
from pathlib import Path

def hitoTab(lH, lV, n):
    Tab, Vtab, Htab=[], [], []
    
    #ranges
    tH, tV=(n+1)*len(lH), (n+1)*len(lV)

    #halfway transformation
    for i in range(len(lV)):
        Vtab.append([])
        if lV[i]==1:
            for j in range(tH):#vtab
                if j%(2*(n+1)) in range(n+2): Vtab[i].append(1)
                else: Vtab[i].append(0)
        else:
            for j in range(tH):
                if j%(2*(n+1)) in [0]+[i for i in range(n+1,2*(n+1))]: Vtab[i].append(1)
                else: Vtab[i].append(0)
    for i in range(len(lH)):#htab
        Htab.append([])
        if lH[i]==1:
            for j in range(tV):
                if j%(2*(n+1)) in range(n+2): Htab[i].append(1)
                else: Htab[i].append(0)
        else:
            for j in range(tV):
                if j%(2*(n+1)) in [0]+[i for i in range(n+1,2*(n+1))]: Htab[i].append(1)
                else: Htab[i].append(0)

    #0 filler
    zVFill=[0 for i in range(tH)]
    zHFill=[0 for i in range(tV)]

    for i in range(len(Vtab)):#vtab
        for j in range(1, n+1):
            Vtab.insert((n+1)*i+j, zVFill)
    for i in range(len(Htab)):#htab
        for j in range(1, n+1):
            Htab.insert((n+1)*i+j, zHFill)

    #composing
    for i in range(len(Vtab)):
        Tab.append([])
        for j in range(len(Htab)):
            Tab[i].append(Vtab[i][j] or Htab[j][i])

    return Tab, (Htab, Vtab)

def export(horizental_list, vertical_list, name=None, formatting='png',emptySpace=4,scale=1):
    hTab=hitoTab(horizental_list, vertical_list, emptySpace)[0]
    output=Image.fromarray(array([[not(j)*255 for j in hTab[i]] for i in range(len(hTab))]))
    output=output.resize((scale*len(horizental_list), scale*len(vertical_list)))
    if name==None: name=f'Hitomezashi {dt.now().strftime("%Y%m%d%H%M%S%f")}'
    output.save(f"{name}.{formatting}")

def genrand(cH, cV, quantity=1, n=4 ,s=1, zwH=0.5, zwV=0.5, rH=0, rV=0):
    path = Path(Path(__file__).parent.resolve().joinpath(f'RandHito_{dt.now().strftime("%Y%m%d%H%M%S%f")} c, r, zweight {cH, cV} {rH, rV} {zwH, zwV}'))
    path.mkdir(exist_ok=True)
    for i in range(quantity): export([choices((0,1), (zwH, 1-zwH))[0] for i in range(randint(cH-rH, cH+rH))], [choices((0,1), (zwV, 1-zwV))[0] for i in range(randint(cV-rV, cV+rV))], f'{path}\\Hitomizashi-{i}', emptySpace=n, scale=s)
