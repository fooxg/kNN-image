from PIL import Image
import numpy as np

from knn_matrix import knn_matrix

def main(img):
    
    scale = 20
    k = 2

    t  = Image.open(img)
    t  = np.array(t,dtype=bool)[:,:,0]
    no = 1*(t)
    
    mat   = knn_matrix(scale = scale,k = k)
    dmat  = np.sum(mat,(2,3))/2
    
    sizeX = no.shape[1]
    sizeY = no.shape[0]

    pixels=np.zeros((sizeY*scale,sizeX*scale),dtype=bool)

    for xx in range(2,sizeX-2):
        for yy in range(2,sizeY-2):
            pixels[yy*scale:yy*scale+scale,xx*scale:xx*scale+scale] = np.sum(no[yy-k:yy+k+1,xx-k:xx+k+1]*mat,(2,3)) > dmat

    return Image.fromarray(pixels)
    

if __name__ == '__main__':
    img = main("turtle.png")
    img.save("scaled.png")
    img.show()
