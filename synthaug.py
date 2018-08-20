# import argparse
import os
import numpy as np
import random
from PIL import Image

from augs import *
from utilities import *
# from paths import *


def main():

    JPG_PATH = '/home/oberon/vidz/person_ds/person_ds/jpg_personDS_402_hd/'
    XML_PATH = '/home/oberon/vidz/person_ds/person_ds/xml_personDS_402_hd/'

    aug_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14]

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n', '--number' , type=int , help='enter number of images per augmentation', default=0)
    # # parser.add_argument('-a', '--augs'   , type=int , help='enter number of augmentations per image', default=1)
    # parser.add_argument('-p', '--path'   , help='enter path to images', default=None)
    # parser.add_argument('-x', '--xml'   , help='enter path to xmls', default=None)
    # # parser.add_argument('-o', '--opath'  , help='enter directory to write augmented images', default=None)
    # parser.add_argument('-e', '--exact'  , help='perform exact transformation(s)\n if more than 1, separate with commas (i.e 1,5,8)', default=None)
    # # parser.add_argument('-t', '--transf' , type=int , help='turn on transformation augmentations', default=0)

    # args  = parser.parse_args()

    # # augs  = AUG_LIST
    # # ipath  = JPG_PATH
    # # opath = path

    # if args.path != None:
    #     JPG_PATH = args.path
    # if args.xml != None:
    #     XML_PATH = args.xml
    # if args.exact != None:
    #     tmp = args.exact.split(",")
    #     aug_tmp = []
    #     for t in tmp:
    #         aug_tmp.append(aug_list[t])
    #     aug_list = aug_tmp

    imgs = [f for f in os.listdir(JPG_PATH)]
    print(imgs)

    to_be_affected = len(imgs)//len(aug_list)

    # if args.number != 0:
    #     to_be_affected = args.number

    for ind in range(len(aug_list)):
        f = aug_list[ind]
        for j in range(to_be_affected):
            
            rand_name = random.sample(imgs, 1)[0]
            rand_img = np.array(Image.open(JPG_PATH + rand_name))
            fname = rand_name[:-4]
            aug, desc = f()
            img_aug = aug.augment_image(rand_img)
            new_name = fname + '_{}'.format(desc)
            Image.fromarray(img_aug).save(JPG_PATH + new_name + '.jpg')

            with open(XML_PATH + fname + '.xml') as xmlf:
                lines = xmlf.read().replace(fname + '.jpg', new_name + '.jpg')
                with open(XML_PATH + new_name + '.xml', 'w') as xml_out:
                    xml_out.write(lines)

if __name__ == "__main__":
    main()
