import skimage
from skimage import io,transform
image_path='/Users/vivekadrakatti/Downloads/26d6f39c-b619-4d26-8139-713cb01917f2'
coll=skimage.io.ImageCollection(image_path + '/*.jpg')
print(coll)
for i in range(len(coll)):
    image=skimage.transform.resize(coll[i],[300,300])
    str_i='Condensed'+str(i)+'.jpg'
    skimage.io.imsave(str_i,image)
