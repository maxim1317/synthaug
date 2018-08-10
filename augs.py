# import imgaug as ia
from imgaug import augmenters as iaa

#------------------------------------------------------------------------------

def increasecolor(self, aug):
    '''
        Increase each pixel’s R-value (redness) by 10 to 100:
    '''
    aug = iaa.WithChannels(0, iaa.Add((10, 100)))
    return aug
#------------------------------------------------------------------------------

def superpixels(self, aug):
    '''
        Generate about 64 superpixels per image. Replace each one with a probability of 50% by its average pixel color.
    '''
    aug = iaa.Superpixels(p_replace=0.5, n_segments=64)
    return aug

#------------------------------------------------------------------------------

def hueincrease(self, aug):
    '''
        Change the colorspace from RGB to HSV, then add 50-100 to the first channel, then convert back to RGB. This increases the hue value of each image.        
    '''
    aug = iaa.Sequential([
        iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="HSV"),
        iaa.WithChannels(0, iaa.Add((50, 100))),
        iaa.ChangeColorspace(from_colorspace="HSV", to_colorspace="RGB")
    ])
    return aug
#------------------------------------------------------------------------------

def greyscale(self, aug):
    '''
        Change images to grayscale and overlay them with the original image by varying strengths, effectively removing 0 to 100% of the color
    '''
    aug = iaa.Grayscale(alpha=(0.0, 1.0))
    return aug
#------------------------------------------------------------------------------

def gaussblur(self, aug):
    '''
        lur each image with a gaussian kernel with a sigma of 3.0
    '''
    aug = iaa.GaussianBlur(sigma=(0.0, 3.0))
    return aug
#------------------------------------------------------------------------------

def averageblur(self, aug):
    '''
        Blur each image using a mean over neihbourhoods that have a random size between 2x2 and 11x11
    '''
    aug = iaa.AverageBlur(k=(2, 11))
    return aug
#------------------------------------------------------------------------------

def averageblur2(self, aug):
    '''
        Blur each image using a mean over neihbourhoods that have random sizes, which can vary between 5 and 11 in height and 1 and 3 in width
    '''
    aug = iaa.AverageBlur(k=((5, 11), (1, 3)))
    return aug
#------------------------------------------------------------------------------

def medianblur(self, aug):
    '''
        Blur each image using a median over neihbourhoods that have a random size between 3x3 and 11x11
    '''
    aug = iaa.MedianBlur(k=(3, 11))
    return aug
#------------------------------------------------------------------------------

def sharpen(self, aug):
    '''
        Sharpen an image, then overlay the results with the original using an alpha between 0.0 and 1.0
    '''
    aug = iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
    return aug
#------------------------------------------------------------------------------

def emboss(self, aug):
    '''
        Emboss an image, then overlay the results with the original using an alpha between 0.0 and 1.0
    '''
    aug = iaa.Emboss(alpha=(0.0, 1.0), strength=(0.5, 1.5))
    return aug
#------------------------------------------------------------------------------

def addval(self, aug):
    '''
        Add random values between -40 and 40 to images, with each value being sampled once per image and then being the same for all pixel
    '''
    aug = iaa.EdgeDetect(alpha=(0.0, 1.0))
    return aug
#------------------------------------------------------------------------------

def addvalcolor(self, aug):
    '''
        dd random values between -40 and 40 to images. In 50% of all images the values differ per channel (3 sampled value). In the other 50% of all images the value is the same for all channels
    '''
    aug = iaa.Add((-40, 40), per_channel=1)
    return aug
#------------------------------------------------------------------------------

def noise(self, aug):
    '''
        Add random values between -40 and 40 to images, with each value being sampled per pixel
    '''
    aug = iaa.AddElementwise((-40, 40))
    return aug
#------------------------------------------------------------------------------

def colornoise(self, aug):
    '''
        d random values between -40 and 40 to images, with each value being sampled per pixel
    '''
    aug = iaa.AddElementwise((-40, 40), per_channel=0.5)
    return aug
#------------------------------------------------------------------------------

def gaussiannoise(self, aug):
    '''
        Add gaussian noise to an image, sampled once per pixel from a normal distribution N(0, s), where s is sampled per image and varies between 0 and 0.05*255
    '''
    return aug
#------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''
            # aug = iaa.AdditiveGaussianNoise(scale=(0, 0.05*255))
#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug
# #------------------------------------------------------------------------------

# def superpixels(self, aug):
#     '''

#     '''
#     return aug

AUG_DICT = {
    1  : increasecolor,
    2  : superpixels,
    3  : hueincrease,
    4  : greyscale,
    5  : gaussblur,
    6  : averageblur,
    7  : averageblur2,
    8  : medianblur,
    9  : sharpen,
    10 : emboss,
    11 : addval,
    12 : addvalcolor,
    13 : noise,
    14 : colornoise,
    15 : gaussiannoise,
}

AUG_LIST = [i for i in range(1, 15)]