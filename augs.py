# import imgaug as ia
from imgaug import augmenters as iaa
import random

#------------------------------------------------------------------------------

def f1():
    '''
        Increase each pixel’s R-value (redness) by 3 to 50:
    '''
    aug = iaa.WithChannels(random.sample([0, 1, 2], 1)[0], iaa.Add((3, 50)))
    desc = 'AddRandColor' 
    return aug, desc
#------------------------------------------------------------------------------

def f2():
    '''
        Multiply each image with a random value between 0.8 and 1.2
    '''
    # aug = iaa.Superpixels(p_replace=0.5, n_segments=64)
    aug = iaa.Multiply((0.8, 1.2))
    desc = 'Multiply' 
    return aug, desc

#------------------------------------------------------------------------------

def f3():
    '''
        Normalize contrast by a factor of 0.6 to 1.4, sampled randomly per image        
    '''
    aug = iaa.ContrastNormalization((0.6, 1.4))
    desc = 'ContrastNormalization' 
    return aug, desc
#------------------------------------------------------------------------------

def f4():
    '''
        Change images to grayscale and overlay them with the original image by varying strengths, effectively removing 0 to 80% of the color
    '''
    aug = iaa.Grayscale(alpha=(0.0, 0.8))
    desc = '' 
    return aug, desc
#------------------------------------------------------------------------------

def f5():
    '''
        Blur each image with a gaussian kernel with a sigma of 3.0
    '''
    aug = iaa.GaussianBlur(sigma=(0.0, 3.0))
    desc = 'GaussBlur' 
    return aug, desc
#------------------------------------------------------------------------------

def f6():
    '''
        Blur each image using a mean over neihbourhoods that have a random size between 2x2 and 11x11
    '''
    aug = iaa.AverageBlur(k=(2, 11))
    desc = 'AverageBlur' 
    return aug, desc
#------------------------------------------------------------------------------

def f7():
    '''
        Blur each image using a mean over neihbourhoods that have random sizes, which can vary between 5 and 11 in height and 1 and 3 in width
    '''
    aug = iaa.AverageBlur(k=((5, 11), (1, 3)))
    desc = 'AverageBlur2' 
    return aug, desc
#------------------------------------------------------------------------------

def f8():
    '''
        Blur each image using a median over neihbourhoods that have a random size between 3x3 and 11x11
    '''
    aug = iaa.MedianBlur(k=(3, 11))
    desc = 'MedianBlur' 
    return aug, desc
#------------------------------------------------------------------------------

def f9():
    '''
        Sharpen an image, then overlay the results with the original using an alpha between 0.0 and 1.0
    '''
    aug = iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
    desc = 'Sharpen' 
    return aug, desc
#------------------------------------------------------------------------------

def f10():
    '''
        Emboss an image, then overlay the results with the original using an alpha between 0.0 and 1.0
    '''
    aug = iaa.Emboss(alpha=(0.0, 1.0), strength=(0.5, 1.5))
    desc = 'Emboss' 
    return aug, desc
#------------------------------------------------------------------------------

def f11():
    '''
        Normalize contrast by a factor of 0.7 to 1.2, sampled randomly per image and for 50% of all images also independently per channel
    '''
    aug = iaa.ContrastNormalization((0.7, 1.2), per_channel=0.5)
    desc = 'ColorContrastNormalization' 
    return aug, desc
#------------------------------------------------------------------------------

def f12():
    '''
        Add random values between -20 and 20 to images. In 50% of all images the values differ per channel (3 sampled value). In the other 50% of all images the value is the same for all channels
    '''
    aug = iaa.Add((-20, 20), per_channel=1)
    desc = 'RandAdd' #thefuck 
    return aug, desc
#------------------------------------------------------------------------------

def f13():
    '''
        Add random values between -20 and 20 to images, with each value being sampled per pixel
    '''
    aug = iaa.AddElementwise((-20, 20))
    desc = 'Noise' 
    return aug, desc
#------------------------------------------------------------------------------

def f14():
    '''
        Add random values between -20 and 20 to images, with each value being sampled per pixel
    '''
    aug = iaa.AddElementwise((-20, 20), per_channel=0.5)
    desc = 'ColorNoise' 
    return aug, desc
#------------------------------------------------------------------------------
