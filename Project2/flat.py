import numpy as np
import math as m

def flats(canvas, vertices, vcolors):
    ykmin = [0,0,0]
    ykmax = [0,0,0]
    xkmin = [0,0,0]
    xkmax = [0,0,0]

    for i in range(3):
        ykmin[i] = min(vertices[i][1],vertices[(i+1)%3][1])
        ykmax[i] = max(vertices[i][1],vertices[(i+1)%3][1])
        xkmin[i] = min(vertices[i][0],vertices[(i+1)%3][0])
        xkmax[i] = max(vertices[i][0],vertices[(i+1)%3][0])
    
    ymin = min(ykmin)
    ymax = max(ykmax)
    xmin = min(xkmin)
    xmax = max(xkmax)
    
    e = np.zeros((4,2))  #pinakas energwn akmwn
    x = np.zeros((2,2))  #pinakas oriakwn shmeiwn
    G = [0,0]
    
    color = (np.sum(vcolors,axis=0))/3
    
    
    if ymin == ymax:                       
        if xmin == xmax:                   #ean exw apla shmeio
            canvas[ymin,xmin] = color
            return canvas
        else:                              #ean exw orizontia eytheia
            for z in range(xmin,xmax):
                canvas[ymin,z] = color
            return canvas
    elif xmin == xmax:                       #ean exw katheti eytheia
        for y in range(ymin,ymax):
            canvas[y,xmin] = color
        return canvas

    c1 = 0                                 #diakrisi trigwnou
    for i in range(3):
        if vertices[i][1] == ymin:
            e[c1] = vertices[i]
            c1 += 2

    if c1 == 4:                            #to trigwno exei katw pleyra paralili ston xx'
        x [0] = e[0]
        x [1] = e[2]
        for i in range(3):
            if vertices[i][1] != ymin:
                e[1] = vertices[i]
                e[3] = vertices[i]
        if e[0][0] > e[2][0]:
            e[[0,2]] = e[[2,0]]        
    elif c1 == 2:                          #to trigwno exei koryfh katw
        c2 =1
        e[2] = e[0]
        x[0] = e[0]
        x[1] = e[0]
        for i in range(3):
            if vertices[i][1] != ymin:
                e[c2] = vertices[i]
                c2 += 2
        if e[1][0] > e[3][0]:
            e[[1,3]] = e[[3,1]]
    

    G = [(e[1][0]-e[0][0])/(e[1][1]-e[0][1]), (e[3][0]-e[2][0])/(e[3][1]-e[2][1])]

    x = x[x[:,0].argsort()]
    xmn = m.ceil(x[0][0])
    xmx = m.ceil(x[1][0])   

    for y in range(ymin,ymax):
        

        for z in range(xmn,xmx):
            canvas[y,z] = color
        
        if  y+1 > e[1][1]:
            e[0] = e[1]
            e[1] = e[3]
            x[0] = e[0]
            G = [(e[1][0]-e[0][0])/(e[1][1]-e[0][1]), (e[3][0]-e[2][0])/(e[3][1]-e[2][1])]
        elif y+1 > e[3][1]:
            e[2] = e[3]
            e[3] = e[1]
            x[1] = e[2] 
            G = [(e[1][0]-e[0][0])/(e[1][1]-e[0][1]), (e[3][0]-e[2][0])/(e[3][1]-e[2][1])]


        x[0][0] = x[0][0] + (G[0])
        x[0][1] +=1
        x[1][0] = x[1][0] + (G[1])
        x[1][1] +=1 
        
        x = x[x[:,0].argsort()]

        if x[1][0] % 1 > 0.5 :
           xmx = m.ceil(x[1][0])
        else:
           xmx = m.floor(x[1][0])
        
        if x[0][0] % 1 > 0.5 :
           xmn = m.ceil(x[0][0])
        else:
           xmn = m.floor(x[0][0])
 
    return canvas