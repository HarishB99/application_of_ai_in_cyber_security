import os, sys, time
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from PIL import Image
from keras import models
# from keras import layers
from keras import backend as K
# from keras.utils import to_categorical
from keras.preprocessing import image
# from imblearn.over_sampling import SMOTE
# from sklearn.metrics import accuracy_score, confusion_matrix
# from sklearn.model_selection import StratifiedKFold

sys.path.insert(0, os.path.abspath('../utils/'))
import util as utils
# get_ipython().run_line_magic('matplotlib', 'inline')

K.clear_session()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def convert_bytecodes_to_images(bytecodes_files, bytecodes_dir, test_case_images_dir):
    if not os.path.exists(test_case_images_dir):
        os.mkdir(test_case_images_dir)
    
    image_set = []

    start_convert_images = time.monotonic()

    for filename in bytecodes_files:
        image_set.append([ utils.byte2img(os.path.join(bytecodes_dir, filename+'.bytes')), filename ])

    end_convert_images = time.monotonic()
    
    print()
    print('Time taken to convert bytecodes to images: ', (end_convert_images - start_convert_images))
    print('Number of images converted: ', len(image_set))
    print()
    
    for image in image_set:
        utils.resize_from_img(image[0], os.path.join(test_case_images_dir, image[1]+'.png'))

def load_images_for_prediction(bytecodes_files, test_case_images_dir):
    test_case_images = [ utils.load_image_as_np(os.path.join(test_case_images_dir, (filename+'.png'))) for filename in bytecodes_files ]
    test_case_images_set = np.asarray(test_case_images)
    test_case_images_set = test_case_images_set.astype('float32') / 255
    return test_case_images_set

def load_model(model_file):
    return models.load_model(model_file)

model_file = '../final_trained_model.h5'
bytecodes_dir = './test_cases/'
test_case_images_dir = os.path.abspath('./test_case_images/')

bytecodes_files = [ os.path.splitext(os.path.basename(file))[0] for file in sorted(os.listdir(bytecodes_dir)) ]

convert_bytecodes_to_images(bytecodes_files, bytecodes_dir, test_case_images_dir)
test_case_images_set = load_images_for_prediction(bytecodes_files, test_case_images_dir)
model = load_model(model_file)

predicted_labels = model.predict_classes(test_case_images_set, batch_size=128)

label_mapping = { label: family for label, family in pd.read_csv('./label_mapping.csv').get_values() }

predicted_labels_mapped = [ label_mapping.get(label, label) for label in predicted_labels ]

final_predicted_labels = [ [bytecodes_files[i], label] for i, label in enumerate(predicted_labels_mapped) ]

for final_predicted_label in final_predicted_labels:
    print('Filename: ', (final_predicted_label[0]+'.bytes'))
    print('Predicted malware family: ', (final_predicted_label[1]))
    print()

