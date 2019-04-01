import os, sys, time, subprocess, argparse, logging, traceback, itertools
import numpy as np
import pandas as pd
from glob import glob
from PIL import Image
from keras import backend as K
from keras.preprocessing import image

K.clear_session()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def byte2img(filename):
    """
        - Plots given bytecode file (consisting hexadecimal numbers without the PE header) to grayscale images
        - params
            - filename - the path to the bytecode file to be converted
        - return
            - img - An instance of a PIL Image representing the converted grayscale image
    """
    try:
        with open(filename, 'r') as f:
            arr = []
            for line in f:
                vals = line.split()
                del vals[0]
                arr.append(vals)
            
            max_len = max([len(vals) for vals in arr])
            
            new_arr = []
            for vals in arr:
                new_arr.append([val.replace('?', '0') for val in vals])
            
            for vals in new_arr:
                if '?' in vals:
                    print(vals)
            
            hexstring = ''.join(list(itertools.chain.from_iterable(new_arr)))
            
            byte_arr = bytearray.fromhex(hexstring)
            width = 1024
            rem = len(byte_arr) % width
            byte_arr_len = len(byte_arr) - rem
            byte_arr = byte_arr[:byte_arr_len]
            byte_arr = np.asarray(byte_arr)
            np_arr = np.reshape(byte_arr, (len(byte_arr)//width, width))
            np_arr = np.uint8(np_arr)
            img = Image.fromarray(np_arr)
            return img
    except Exception as error:
        logging.error(traceback.format_exc())

def resize_from_img(img, imgname, size=(128, 128)):
    """
        - Resize an existing PIL Image instance to the specified size and save it to the filesystem
        - params
            - img - An instance of the PIL Image
            - imgname - the path to the image file to write to (The directory should exist - The image need not exist)
            - size - the dimension to resize the image to in the format (width, height) - default is 128 by 128
        - return
            - None
    """
    try:
        img = img.resize(size, Image.LANCZOS)
        img.save(imgname)
    except Exception as error:
        logging.error(traceback.format_exc())

def valid_dir(dir_string):
    if not os.path.isdir(dir_string):
        msg = "%r is not a valid directory" % dir_string
        raise argparse.ArgumentTypeError(msg)
    else:
        bytecode_files = []
        for filename in os.listdir(dir_string):
            if filename.endswith('.bytes'):
                bytecode_files.append(filename)
        if len(bytecode_files) < 1:
            msg = "%r does not contain bytecode files (.bytes)" % dir_string
            raise argparse.ArgumentTypeError(msg)
        return dir_string

def convert_bytecodes_to_images(bytecode_files, bytecodes_dir, test_case_images_dir):
    if not os.path.exists(test_case_images_dir):
        os.mkdir(test_case_images_dir)
    
    image_set = []

    start_convert_images = time.monotonic()

    for filename in bytecode_files:
        image_set.append([ byte2img(os.path.join(bytecodes_dir, filename+'.bytes')), filename ])

    end_convert_images = time.monotonic()
    
    print()
    print('Time taken to convert bytecodes to images and save them to filesystem (in seconds): ', (end_convert_images - start_convert_images))
    print('Number of images converted: ', len(image_set))
    print()
    
    for image in image_set:
        resize_from_img(image[0], os.path.join(test_case_images_dir, image[1]+'.png'))

cmd_args_parser = argparse.ArgumentParser()
cmd_args_parser.add_argument('-d', '--directory', '--dir', required=True, type=valid_dir, metavar='directory')

cmd_args = cmd_args_parser.parse_args()

bytecodes_dir = cmd_args.directory
test_case_images_dir = os.path.join(bytecodes_dir, 'test_case_images')

bytecode_files = [ os.path.splitext(os.path.basename(file))[0] for file in sorted( glob( os.path.abspath(bytecodes_dir)+'/*.bytes' ) ) ]

convert_bytecodes_to_images(bytecode_files, bytecodes_dir, test_case_images_dir)