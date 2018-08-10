import argparse
import os
import random

from augs  import *
from utils import *
from paths import *

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number' , type=int , help='enter number of output images')
    parser.add_argument('-a', '--augs'   , type=int , help='enter number of augmentations per image', default=1)
    parser.add_argument('-p', '--path'   , help='enter path to images', default=None)
    parser.add_argument('-o', '--opath'  , help='enter directory to write augmented images', default=None)
    parser.add_argument('-e', '--exact'  , help='perform exact transformation(s)\n if more than 1, separate with commas (i.e 1,5,8)', default=None)
    parser.add_argument('-t', '--transf' , type=int , help='turn on transformation augmentations', default=0)


    args  = parser.parse_args()

    augs  = AUG_LIST
    ipath  = JPG_PATH
    opath = path

    if args.transformations == 1:
        augs.append(TRS_LIST)
    if args.exact != None:
        augs = [int(i) for i in args.exact.split(',')]
    if args.path != None:
        ipath  = args.path
        opath = ipath

    IMAGES = [os.path.join(ipath, f) for f in os.listdir(ipath)]

    for image in IMAGES:
        xml_to_xy(image)




if __name__ == "__main__":
    main()
