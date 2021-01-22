import numpy
from PIL import Image
 
def create_image(name):
    width = 128
    height = 128
    
    filename = 'img_pass/{0}.jpg'.format(name)
    rgb_array = numpy.random.rand(height,width,3) * 255
    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
    image.save(filename)
    return 1