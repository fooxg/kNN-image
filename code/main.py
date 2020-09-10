import numpy as np
from PIL import Image
from knn_matrix import knn_matrix

sizeX = 50  # 13
sizeY = 29  # 10
scale = 20
k = 2

types=np.load('map.npy')
mat=knn_matrix()

forest=((types-1)*(types-2)/2).astype(np.int8)
field=(types*(2-types)).astype(np.int8)
urban=(types*(types-1)/2).astype(np.int8)
fiu=np.array([forest,field,urban]).astype(np.int8)

resX = sizeX*scale
resY = sizeY*scale

pixels=np.zeros((resY,resX,3))


for x in range(resX-1):
    for y in range(resY-1):
        weights = [0, 0, 0]
        xx = x//scale
        yy = y//scale
        weights = np.sum(fiu[:,yy-min(k,yy):yy+k+min(3,sizeY-yy)-2,xx-min(k,xx):xx+k+min(3,sizeX-xx)-2]*mat[y-yy*scale,x-xx*scale,-min(0,yy-2):5+min(0,sizeY-yy-3),-min(0,xx-2):5+min(0,sizeX-xx-3)],axis=(1,2))
        bestType = np.argmax(weights)
        if bestType == 0:
            pixels[y,x] = [152, 205, 153]  
        else:
            if bestType == 1:
                pixels[y,x] = [255, 238, 158]
            else:
                pixels[y,x] = [204, 204, 204]


##imgm=Image.fromarray(255*t)
##no=1*(t)[::5,::5]
##
##sizeX = no.shape[1]
##sizeY = no.shape[0]
##
##pixels=np.zeros((sizeY*scale,sizeX*scale),dtype=bool)
##
##for xx in range(2,sizeX-2):
##    for yy in range(2,sizeY-2):
##        pixels[yy*scale:yy*scale+scale,xx*scale:xx*scale+scale] = np.sum(no[yy-k:yy+k+1,xx-k:xx+k+1]*mat,(2,3)) < dmat


img=Image.fromarray(pixels.astype(np.uint8),'RGB')
img.save("refined.png")
