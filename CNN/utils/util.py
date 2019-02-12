import os, array, itertools, sys, traceback, logging
import numpy as np
from PIL import Image
from keras.preprocessing import image

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


def load_image_as_np(filename):
    """
        - Loads an image from the filesystem as a 3D numpy array
        - params
            - filename - the path to the image file to be loaded
        - return
            - a 3D numpy array representing the loaded image
    """
    try:
        img = image.load_img(filename, grayscale=True)  # for newer versions, use "color_mode='grayscale'" instead of "grayscale=True"
        return np.atleast_3d(img)
    except Exception as error:
        logging.error(traceback.format_exc())


def resize_from_file(filename, dest, size=(128, 128)):
    """
        - Resize an existing image from the filesystem to the specified size and save it back to the filesystem
        - params
            - filename - the path to the image file to be resized
            - dest - the path to the image file to write to (The directory should exist - The image need not exist)
            - size - the dimension to resize the image to in the format (width, height) - default is 128 by 128
        - return
            - None
    """
    try:
        imgname = os.path.basename(filename)
        img = image.load_img(filename, grayscale=True)  # for newer versions, use "color_mode='grayscale'" instead of "grayscale=True"
        img = img.resize(size, Image.LANCZOS)
        img.save(os.path.join(dest, imgname))
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

