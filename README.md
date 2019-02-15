## Application of AI in Cyber Security

* The general objective of this project is to investigate the various deep learning techniques available to solve selected cyber security related problems.

* The objective of [this](https://github.com/HarishB99/application_of_ai_in_cyber_security) particular project is to make use of deep learning techniques to classify malware quickly without resorting to manual analysis of source codes and behaviour of the malware.

## Dataset

* The dataset used for this project was retrieved from the Kaggle website, more specifically from their [Microsoft Malware Classification Challenge (BIG 2015)](https://www.kaggle.com/c/malware-classification/data) website

## Getting Started

* Firstly, clone this github repo to your home directory (or any other directory you want to). We will call this directory INSTALL_PATH:

	* `git clone https://github.com/HarishB99/application_of_ai_in_cyber_security.git`
	```shell
	cd INSTALL_PATH  # Where INSTALL_PATH is the path in which you will be cloning this git repo
	git clone https://github.com/HarishB99/application_of_ai_in_cyber_security.git
	cd application_of_ai_in_cyber_security/
	```

### CNN - Convolutional Neural Network

* Install the p7zip-full package on Ubuntu Linux (This was the linux distribution that was used for this project)

	* `sudo apt install -y p7zip-full`

* The p7zip-full package is installed to make use of the utilities in this package to extract 7-zip archive files.

* Create a directory at the root of this git repo named `dataset_bytes`

	```shell
	cd INSTALL_PATH/application_of_ai_in_cyber_security
	mkdir dataset_bytes
	```

* Download `train.7z` from the [challenge website](https://www.kaggle.com/c/malware-classification/data) (Note that you will have to create an account with Kaggle to download the file.)

* The [challenge website](https://www.kaggle.com/c/malware-classification/data) states that the 

> dataset is almost half a terabyte uncompressed

* Hence, 
