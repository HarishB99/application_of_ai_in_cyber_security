## Application of AI in Cyber Security

The general objective of this project is to investigate the various deep learning techniques available to solve selected cyber security related problems.

The objective of [this](https://github.com/HarishB99/application_of_ai_in_cyber_security) particular project is to make use of deep learning techniques to classify malware quickly without resorting to manual analysis of source codes and behaviour of the malware.

## Dataset

The dataset used for this project was retrieved from the Kaggle website, more specifically from their [Microsoft Malware Classification Challenge (BIG 2015)](https://www.kaggle.com/c/malware-classification/data) website

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

### LSTM

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
