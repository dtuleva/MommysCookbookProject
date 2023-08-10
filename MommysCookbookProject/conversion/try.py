import numpy as np
from PIL import Image

img = Image.open('icon-remove-22.jpg')
array = np.array(img)

print(array.shape)

array_2 = array // 3

img_out = Image.fromarray(array_2)
img_out.save('one.png')

