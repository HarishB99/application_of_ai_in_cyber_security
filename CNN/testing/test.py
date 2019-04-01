import os, sys, time, subprocess, argparse, logging, traceback, itertools, shutil
import numpy as np
import pandas as pd
from glob import glob
from PIL import Image
from keras import models
from keras import backend as K
from keras.preprocessing import image

K.clear_session()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

label_mapping = {
    0: 'Ramnit',
    1: 'Lollipop',
    2: 'Kelihos_ver3',
    3: 'Vundo',
    4: 'Simda',
    5: 'Tracur',
    6: 'Kelihos_ver1',
    7: 'Obfuscator.ACY',
    8: 'Gatak'
}

def load_image_as_np(filename):
    """
        - Loads an image from the filesystem as a 3D numpy array
        - params
            - filename - the path to the image file to be loaded
        - return
            - a 3D numpy array representing the loaded image
    """
    try:
        img = image.load_img(filename, color_mode='grayscale')  # for newer versions, use "color_mode='grayscale'"; For older versions, use "grayscale=True"
        return np.atleast_3d(img)
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

def load_images_for_prediction(bytecode_files, test_case_images_dir):
    test_case_images = [ load_image_as_np(os.path.join(test_case_images_dir, (filename+'.png'))) for filename in bytecode_files ]
    test_case_images_set = np.asarray(test_case_images)
    test_case_images_set = test_case_images_set.astype('float32') / 255
    return test_case_images_set

def load_model(model_file):
    return models.load_model(model_file)

cmd_args_parser = argparse.ArgumentParser()
cmd_args_parser.add_argument('-d', '--directory', '--dir', required=True, type=valid_dir, metavar='directory')

cmd_args = cmd_args_parser.parse_args()

model_file = './final_trained_model.h5'
bytecodes_dir = cmd_args.directory
test_case_images_dir = os.path.join(bytecodes_dir, 'test_case_images')

bytecode_files = [ os.path.splitext(os.path.basename(file))[0] for file in sorted( glob( os.path.abspath(bytecodes_dir)+'/*.bytes' ) ) ]

test_case_images_set = load_images_for_prediction(bytecode_files, test_case_images_dir)
model = load_model(model_file)

labels = { filename: (int(family) - 1) for filename, family in pd.read_csv('./trainLabels.csv').get_values() }

start_prediction = time.monotonic()

predicted_labels_arr = model.predict_classes(test_case_images_set, batch_size=512)

end_prediction = time.monotonic()

# print()
print('Time taken to predict families of malware samples (in seconds): ', (end_prediction - start_prediction))
print('Number of malware samples processed: ', len(bytecode_files))
print()

predicted_labels = predicted_labels_arr.tolist()
actual_labels = [ labels.get(filename, filename) for filename in bytecode_files ]

# label_mapping = { label: family for label, family in pd.read_csv('./label_mapping.csv').get_values() }

ramnit_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'ramnit', 'images' )
ramnit_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'ramnit', 'bytecodes' )

lollipop_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'lollipop', 'images' )
lollipop_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'lollipop', 'bytecodes' )

kelihos3_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'kelihos_ver3', 'images' )
kelihos3_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'kelihos_ver3', 'bytecodes' )

vundo_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'vundo', 'images' )
vundo_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'vundo', 'bytecodes' )

simda_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'simda', 'images' )
simda_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'simda', 'bytecodes' )

tracur_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'tracur', 'images' )
tracur_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'tracur', 'bytecodes' )

kelihos1_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'kelihos_ver1', 'images' )
kelihos1_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'kelihos_ver1', 'bytecodes' )

obfuscator_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'obfuscator_acy', 'images' )
obfuscator_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'obfuscator_acy', 'bytecodes' )

gatak_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'gatak', 'images' )
gatak_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'gatak', 'bytecodes' )

misclassified_image_dir = os.path.join( os.path.abspath(bytecodes_dir), 'misclassified', 'images' )
misclassified_bytecodes_dir = os.path.join( os.path.abspath(bytecodes_dir), 'misclassified', 'bytecodes' )

def create_dir(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

create_dir(ramnit_image_dir)
create_dir(ramnit_bytecodes_dir)

create_dir(lollipop_image_dir)
create_dir(lollipop_bytecodes_dir)

create_dir(kelihos3_image_dir)
create_dir(kelihos3_bytecodes_dir)

create_dir(vundo_image_dir)
create_dir(vundo_bytecodes_dir)

create_dir(simda_image_dir)
create_dir(simda_bytecodes_dir)

create_dir(tracur_image_dir)
create_dir(tracur_bytecodes_dir)

create_dir(kelihos1_image_dir)
create_dir(kelihos1_bytecodes_dir)

create_dir(obfuscator_image_dir)
create_dir(obfuscator_bytecodes_dir)

create_dir(gatak_image_dir)
create_dir(gatak_bytecodes_dir)

create_dir(misclassified_image_dir)
create_dir(misclassified_bytecodes_dir)

def destination_of_bytecode(label):
    if label == 0:
        return {
            "final_image_dir": ramnit_image_dir,
            "final_bytecodes_dir": ramnit_bytecodes_dir
        }
    if label == 1:
        return {
            "final_image_dir": lollipop_image_dir,
            "final_bytecodes_dir": lollipop_bytecodes_dir
        }
    if label == 2:
        return {
            "final_image_dir": kelihos3_image_dir,
            "final_bytecodes_dir": kelihos3_bytecodes_dir
        }
    if label == 3:
        return {
            "final_image_dir": vundo_image_dir,
            "final_bytecodes_dir": vundo_bytecodes_dir
        }
    if label == 4:
        return {
            "final_image_dir": simda_image_dir,
            "final_bytecodes_dir": simda_bytecodes_dir
        }
    if label == 5:
        return {
            "final_image_dir": tracur_image_dir,
            "final_bytecodes_dir": tracur_bytecodes_dir
        }
    if label == 6:
        return {
            "final_image_dir": kelihos1_image_dir,
            "final_bytecodes_dir": kelihos1_bytecodes_dir
        }
    if label == 7:
        return {
            "final_image_dir": obfuscator_image_dir,
            "final_bytecodes_dir": obfuscator_bytecodes_dir
        }
    if label == 8:
        return {
            "final_image_dir": gatak_image_dir,
            "final_bytecodes_dir": gatak_bytecodes_dir
        }
    
start_sorting = time.monotonic()    

for i, file in enumerate(bytecode_files):
    if predicted_labels[i] == actual_labels[i]:
        final_dirs = destination_of_bytecode(predicted_labels[i])
    else:
        final_dirs = {
            "final_image_dir": misclassified_image_dir,
            "final_bytecodes_dir": misclassified_bytecodes_dir
        }
    
    os.rename(os.path.join(bytecodes_dir, file+'.bytes'), os.path.join(final_dirs["final_bytecodes_dir"], file+'.bytes'))
    os.rename(os.path.join(test_case_images_dir, file+'.png'), os.path.join(final_dirs["final_image_dir"], file+'.png'))
        
end_sorting = time.monotonic()

shutil.rmtree(test_case_images_dir)

print('Time taken to sort bytecodes based on prediction (in seconds): ', (end_sorting - start_sorting))
print('Number of bytecodes sorted: ', len(bytecode_files))
print()

# predicted_labels_mapped = [ label_mapping.get(label, label) for label in predicted_labels ]

# final_predicted_labels = [ [bytecode_files[i], label] for i, label in enumerate(predicted_labels_mapped) ]

# for final_predicted_label in final_predicted_labels:
#     print('Filename: ', (final_predicted_label[0]+'.bytes'))
#     print('Predicted malware family: ', (final_predicted_label[1]))
#     print()

