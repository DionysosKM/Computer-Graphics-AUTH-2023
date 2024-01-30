import numpy as np
import math as m
import interpolate_vectors as iv

def Gourauds(canvas, vertices, vcolors):
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
    
    e = np.zeros((4,2))    
    x = np.zeros((2,2))
    G = [0,0]
    
    
    if ymin == ymax:                       #ean exw apla shmeio
        if xmin == xmax:
            color = vcolors[0]
            canvas[ymin,xmin] = color
            return canvas
        else:                              #ean exw orizontia eytheia
            for z in range(int(xmin),int(xmax)):
                for i in range(3):
                    if vertices[i][0] == [xmin] and vertices[i][1]==[ymin]:
                       cl1 = vcolors[i]
                    elif vertices[i][0] == [xmax] and vertices[i][1] == [ymin]:   
                       cl2 = vcolors[i] 
                color = iv.interpolate_vectors([xmin,ymin],[xmax,ymin],cl1,cl2,z,1)
                canvas[int(ymin),z] = color
            return canvas
    elif xmin == xmax:                       #ean exw katheti eytheia
        for y in range(int(ymin),int(ymax)):
            for i in range(3):
                    if vertices[i][0] == [xmin] and vertices[i][1] == [ymin]:
                       cl1 = vcolors[i]
                    elif vertices[i][0] == [xmin] and vertices[i][1] == [ymax]:   
                       cl2 = vcolors[i] 
            color = iv.interpolate_vectors([xmin,ymin],[xmin,ymax],cl1,cl2,y,2)
            canvas[y,int(xmin)] = color
        return canvas

    c1 = 0
    for i in range(3):
        if vertices[i][1] == ymin:
            e[c1] = vertices[i]
            c1 += 2

    if c1 == 4:
        x [0] = e[0]
        x [1] = e[2]
        for i in range(3):
            if vertices[i][1] != ymin:
                e[1] = vertices[i]
                e[3] = vertices[i]
    elif c1 == 2:
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

    if e[0][0] > e[2][0]:
        e[[0,2]] = e[[2,0]]    

    G = [(e[1][0]-e[0][0])/(e[1][1]-e[0][1]), (e[3][0]-e[2][0])/(e[3][1]-e[2][1])]

    x = x[x[:,0].argsort()]
    xmn = m.ceil(x[0][0])
    xmx = m.ceil(x[1][0])   

    for y in range(int(ymin),int(ymax)):
        

        #xmn = m.ceil(x[0][0])
        #xmx = m.ceil(x[1][0])

        for i in range(3):
            if vertices[i][0] == e[0][0] and vertices[i][1] == e[0][1]:
                cl3 = vcolors[i]
            if vertices[i][0] == e[1][0] and vertices[i][1] == e[1][1]:
                cl4 = vcolors[i]
            if vertices[i][0] == e[2][0] and vertices[i][1] == e[2][1]:
                cl5 = vcolors[i]
            if vertices[i][0] == e[3][0] and vertices[i][1] == e[3][1]:
                cl6 = vcolors[i]   
        
        cl1 = iv.interpolate_vectors(e[0],e[1],cl3,cl4,y,2)
        cl2 = iv.interpolate_vectors(e[2],e[3],cl5,cl6,y,2)          
       
        for z in range(xmn,xmx):
            color = iv.interpolate_vectors([xmn,y],[xmx,y],cl1,cl2,z,1)
            canvas[y,z] = color
        
        if xmin == xmax:
            color = iv.interpolate_vectors([xmn,y],[xmx,y],cl1,cl2,z,1)
            canvas[y,xmn] = color

        if  y+1 > e[1][1]:
            e[0] = e[1]
            e[1] = e[3]
            G = [(e[1][0]-e[0][0])/(e[1][1]-e[0][1]), (e[3][0]-e[2][0])/(e[3][1]-e[2][1])]
        elif y+1 > e[3][1]:
            e[2] = e[1]
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