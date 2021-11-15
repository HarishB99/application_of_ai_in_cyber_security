## Application of AI in Cyber Security

The general objective of this project is to investigate the various deep learning techniques available to solve selected cyber security related problems.

The objective of [this](https://github.com/HarishB99/application_of_ai_in_cyber_security) particular project is to make use of deep learning techniques to classify malware quickly without resorting to manual analysis of source codes and behaviour of the malware.

## Dataset

The dataset used for this project was retrieved from the Kaggle website, more specifically from their [Microsoft Malware Classification Challenge (BIG 2015)](https://www.kaggle.com/c/malware-classification/data) website

## Updating local codebase

* Simply run the following command in your git repository to get the latest version of the codebase:

	* `git pull origin master`

## Activating and deactivating conda environment

* The conda environment is where your Python notebooks and codes are usually executed. It contains all the python packages that has been installed onto the computer.

* To activate it, run the following:

	* `conda activate`

* To deactivate it, simply run the following:
	
	* `conda deactivate`

* If your conda environment has been activated, you should be able to see your terminal prompt change, like so:
	
	* `(<conda environment name>) user@domain $`

* For example, the default and main conda environment is named 'base':
	
	* `(base) student@localhost $`

* Note that you will have to activate your conda environment, if you have installed a newer version of the Anaconda Python distribution, before proceeding to run the following commands.

## Getting Started

Firstly, clone this github repo to your home directory (or any other directory you want to) of the Linux Virtual Machine you are using (A Virtual Machine that was running the Ubuntu Linux distribution was used for this project.). We will call this directory INSTALL_PATH:

```shell
cd INSTALL_PATH  # Where INSTALL_PATH is the path in which you will be cloning this git repo
git clone https://github.com/HarishB99/application_of_ai_in_cyber_security.git
cd application_of_ai_in_cyber_security/
```

### Generic Instructions

Install the p7zip-full package on Ubuntu Linux (This was the linux distribution that was used for this project)

* `sudo apt install -y p7zip-full`

The p7zip-full package is installed to make use of the utilities in this package to extract 7-zip archive files.

Download `train.7z` from the [challenge website](https://www.kaggle.com/c/malware-classification/data) (Note that you will have to create an account with [Kaggle](https://www.kaggle.com/) to download the file.)

Please note the call to `keras.preprocessing.image.load_image()` function in the two functions in `CNN/utils/utils.py`, namely `load_image_as_np()` and `resize_from_file()`. For newer versions of the `keras.preprocessing.image` library, you will have to use `color_mode='grayscale'` to load grayscale images. For older versions, you need to use `grayscale=True`. This reminder is also documented in the comments for the two calls to the said library made in `CNN/utils/utils.py`.

### CNN - Convolutional Neural Network

Before you proceed to execute the Python notebooks in the `CNN/` folder, perform the following:

Create a directory at the root of this git repo named `dataset_bytes`

```shell
cd INSTALL_PATH/application_of_ai_in_cyber_security
mkdir dataset_bytes
```

Extract the `.bytes` files in train.7z into `INSTALL_PATH/application_of_ai_in_cyber_security/dataset_bytes/` (The best way I can think of is to extract all the files into a separate folder and move all the `.bytes` files into the directory mentioned)

Now, `INSTALL_PATH/application_of_ai_in_cyber_security/dataset_bytes/` should only contain `.bytes` files

You are now ready to execute the Python notebooks in the `CNN/` directory

Please note that you will have to execute the codes in `CNN/byte_to_image_converter.ipynb` to convert the `.bytes` files into `.png` files before executing `CNN/main.ipynb`

### LSTM - Long Short Term Memory

Before you proceed to execute the Python notebooks in the `LSTM/` folder, perform the following:

Create a directory at the root of this git repo named `dataset_asm_files_subset`

```shell
cd INSTALL_PATH/application_of_ai_in_cyber_security
mkdir dataset_asm_files_subset
```

Extract a subset of the `.asm` files in train.7z into `INSTALL_PATH/application_of_ai_in_cyber_security/dataset_asm_files_subset/` (The best way I can think of is to extract all the files into a separate folder and move the first few `.asm` files that you wish to be processed by the model into the directory mentioned)

Now, `INSTALL_PATH/application_of_ai_in_cyber_security/dataset_asm_files_subset/` should only contain `.asm` files

You are now ready to execute the Python notebooks in the `LSTM/` directory

You can simply execute `LSTM/main.ipynb` to run the program

### Testing CNN model

The purpose of this testing program is to classify samples malware bytecodes (`.bytes` files with their PE headers removed) into their respective malware families.

Before you proceed to execute the Python notebooks in the `CNN/testing/` folder, perform the following:

<!-- Create a directory inside the `CNN/testing/` folder of this git repo named `test_cases_exe`

Copy over the executable files (.exe) which you want the model to analyse and predict into this directory you have created (which is `CNN/testing/test_cases_exe` in this git repo) -->

Execute `CNN/testing/byte_to_image_converter.ipynb` or `CNN/testing/byte_to_image_converter.py` to convert the `.bytes` files into `.png` files before executing `CNN/main.ipynb`. For this, you will have to create a directory somewhere in your filesystem to store these bytecodes (`.bytes` files with their PE headers removed) that you want the program to classify. We will refer to this directory as `BYTECODES_DIR`. 

```shell
cd INSTALL_PATH/application_of_ai_in_cyber_security/CNN/testing/
python byte_to_image_converter.py -d BYTECODES_DIR
```

If you are executing the Python notebook instead (`CNN/testing/byte_to_image_converter.ipynb`), you will have to edit the variable `arguments_list` in cell 9 to match the above.

You are now ready to execute the Python notebooks in the `CNN/testing/` directory

You can simply execute `CNN/testing/malware_sorter.ipynb` or `CNN/testing/malware_sorter.py` to run the program. It is simpler to run the latter.

`python malware_sorter.py -d BYTECODES_DIR`

If you are executing the Python notebook instead (`CNN/testing/malware_sorter.ipynb`), you will have to edit the variable `arguments_list` in cell 10 to match the above.
