# import argparse
import os
import numpy as np
import random
# import random
from imgaug import augmenters as iaa
from PIL import Image

from augs  import *
from utilities import *
from paths import *

def main():

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n', '--number' , type=int , help='enter number of output images')
    # parser.add_argument('-a', '--augs'   , type=int , help='enter number of augmentations per image', default=1)
    # parser.add_argument('-p', '--path'   , help='enter path to images', default=None)
    # parser.add_argument('-o', '--opath'  , help='enter directory to write augmented images', default=None)
    # parser.add_argument('-e', '--exact'  , help='perform exact transformation(s)\n if more than 1, separate with commas (i.e 1,5,8)', default=None)
    # parser.add_argument('-t', '--transf' , type=int , help='turn on transformation augmentations', default=0)


    # args  = parser.parse_args()

    # augs  = AUG_LIST
    # ipath  = JPG_PATH
    # opath = path

    # if args.transformations == 1:
    #     augs.append(TRS_LIST)
    # if args.exact != None:
    #     augs = [int(i) for i in args.exact.split(',')]
    # if args.path != None:
    #     ipath  = args.path
    #     opath = ipath

    JPG_PATH = '/home/oberon/vidz/hollywood/jpgs_proper/'
    XML_PATH = '/home/oberon/vidz/hollywood/xmls_merged/'

    imgs = [f for f in os.listdir(JPG_PATH)]
    # print(imgs)

    aug_list = [f1, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]

    # imgs = random.sample(imgs, 90)

    for img in range(0, len(imgs)):
        rand_aug = random.sample(aug_list, 1)


        imag = np.array(Image.open(JPG_PATH + imgs[img]))
        aug = rand_aug[0]()
        xml = xml_to_xy(XML_PATH + imgs[img][:-4]+'.xml')
        xml.filename = imgs[img][:-4]+'_'+str(aug_list.index(rand_aug[0]) + 1)+'.jpg'
        imag_aug = aug.augment_image(imag)
        Image.fromarray(np.uint8(imag_aug)).save(JPG_PATH+xml.filename)
        xy_to_xml(XML_PATH, xml)

if __name__ == "__main__":
    main()
