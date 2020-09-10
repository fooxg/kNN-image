import numpy as np

def knn_matrix(scale = 20, k = 2):
    weights=np.zeros((scale,scale,2*k+1,2*k+1))

    for y in range(scale):
        for x in range(scale):
            xr=x+2*k*scale
            yr=y+2*k*scale
            mink = 2*k
            tem=[]
            for j in range(-k, k+1):
                for i in range(-k,k+1):
                    tem.append(2**(-0.5*((xr/scale-(mink+i))**2+(yr/scale-(mink+j))**2)))
            weights[y,x] = np.array(tem).reshape(-1,2*k+1)

    return weights
