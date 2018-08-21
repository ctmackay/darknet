
import os
import sys
from argparse import ArgumentParser
import shutil


from os import listdir
from os.path import isfile, join




def ensureDir(d):
    if not d[-1] == '/':
        d += '/'
    if not os.path.exists(d):
        os.makedirs(d)


def usage():
    print "Usage: python2 create_dataset.py -d <dataset_path> [-f <format> -h <image_height> -w <image_width>] <output_dir>"
    exit()


def get_args():
    parser = ArgumentParser(add_help=False)
    parser.add_argument("data", nargs=1, help="Output directory for dataset")
    parser.add_argument('--help', action='help', help='Show this help message and exit')
    parser.add_argument('-d', '--dataset', type=str, default=None, help="Dataset directory path")
    parser.add_argument('-ls', '--labelsource', type=str, default=None, help="labels directory path")

    parser.add_argument('-if', '--inputformat', type=str, default="darknet", help="labels format")
    parser.add_argument('-f', '--format', type=str, default="kitti",
                        help="Desired format: kitti (default), voc (i.e., Pascal VOC), darknet")

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()

    if not args.data:
        print "Please specify the output directory!"
        usage()

    if not args.labelsource:
        print "Please specify the output directory!"
        usage()

    source = args.labelsource
    # print(source)

    outdir = args.data[0]
    if not args.dataset:
        print "Please specify the path to the dataset directory!"
        usage()
    indir = args.dataset

    ensureDir(outdir)
    images = [f for f in listdir(indir) if isfile(join(indir, f))]

    for file in images:
        new_filename = os.path.splitext(file)[0] + ".txt"
        print(new_filename)
        outfile_path = os.path.join(os.getcwd(), outdir, new_filename)
        print(outfile_path)
        srcfile = os.path.join(source, new_filename)
        print(srcfile)
        shutil.copy(srcfile, outfile_path)

    print(images)
