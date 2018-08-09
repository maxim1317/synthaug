import argparse

import imgaug as ia
from imgaug import augmenters as iaa

from paths import *

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number' , type=int , help='enter number of output images')
    parser.add_argument('-a', '--augs'   , type=int , help='enter number of augmentations per image', default=1)
    parser.add_argument('-p', '--path'   , help='enter path to images')
    parser.add_argument('-o', '--opath'  , help='enter directory to write augmented images', default=None)
    parser.add_argument('-e', '--exact'  , help='perform exact transformation(s)\n if more than 1, separate with commas (i.e 1,5,8)', default=None)
    parser.add_argument('-t', '--transf' , type=int , help='turn on transformation augmentations', default=0)


    args = parser.parse_args()

    augs = AUG_LIST
    if args.transformations == 1:
        augs.append(TRS_LIST)
    if args.exact != None:
        augs = [int(i) for i in args.exact.split(',')]

if __name__ == "__main__":
    main()
