## Installation of Anaconda distribution on Ubuntu 18.04

* Refer to the following website for instructions on how to install the anaconda distribution on Linux OS: http://docs.anaconda.com/anaconda/install/linux/

## Post-Installation of Anaconda distribution of Ubuntu 18.04

* To avoid strange errors during installation of new python packages using conda, run the following two commands in the terminal:

	* `conda upgrade conda`
	* `conda upgrade --all`

## Installing Keras with Tensorflow

* Run the following commands in the terminal:

	* `conda install -y tensorflow`
	* `conda install -y keras`

* Note that -y simply means install without prompts --> This flag is optional

## Installing matplotlib

* The matplotlib is a module that comes as part of the standard scientific Python suite (like the one that comes with the Anaconda distribution). Some deep learning related code samples which you may encounter might make use of this modul to plot graphs to portray the accuracy metrics measuring the performance of the deep learning neural network model created.

* Though this module comes pre-installed with Anaconda, either the previous two steps might have corrupted the module or the module was not properly installed by Anaconda (the latest version 5.3.1 as of the time of this writing). In any case, if you try to use matplotlib in your code and it gives you error saying it can't find the module, run the following:

	* ~~`conda install -f matplotlib -y`~~
	* `conda install --force-reinstall matplotlib -y` --> For later versions of Anaconda released since December 2018

* Note that -y simply means install without prompts --> This flag is optional

## Installing imbalanced-learn

* The imbalanced-learn module was used in this project as the dataset itself was imbalanced. In other words, for the malware classification task that was to be performed by the neural netowkr, the dataset containing malware samples didi not contain equal number of samples of each family.

* In this case, imbalanced-learn module has methods to oversample and undersample the data so that the neural network can look at more or less equal number of samples of each malware family, hence, increasing the classification accuracy of the neural network model as it is able to learn the associations more accurately.

* To install imbalanced-learn using conda, run the following:

	* `conda install -c conda-forge imbalanced-learn -y`

* Note that if the above does not work, try the other alternative commands listed [here](https://anaconda.org/conda-forge/imbalanced-learn/)

* Also note that -y simply means install without prompts --> This flag is optional

## Installing pandas

* The pandas module was mainly used in this project to read in files of thee csv format

* Although this can be done manualyy using the already available built-in methods in Python, reading csv files using the pandas module makes the process more convenient

* To install pandas using conda, run the following:

	* `conda install -c anaconda pandas`

* Note that -y simply means install without prompts --> This flag is optional

## Installing scikit-learn

* The scikit-learn module was mainly used in this project to measure the confusion matrix of the predicted results of the neural network model, one of the metrics that was used to evaluate the performance of the model

* To install it using conda, run the following:

	* `conda install -c anaconda scikit-learn`

* Note that -y simply means install without prompts --> This flag is optional

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

## Starting Jupyter Notebook on your local machine

* Running the installation script for Anaconda installs Jupyter Notebook for you by default

* To start this application on your project's root directory, run the following:

	* `cd /path/to/project_root_dir`
	* `jupyter notebook &`

* Note that if you run the last command without the ampersand (&), you will have to open a new terminal to run other commands while the notebook is running

* To make this process more convenient, one can choose to write a bash script instead:

	* start.sh
	
	```shell
	#!/bin/bash
	#
	# Name of script: start.sh
	#
	
	cd /path/to/project_root_dir
	jupyter notebook
	```

* Then, run the following to provide permissions to your own user account to execute this script:

	* `chmod u+x start.sh`

* Now, assuming you have created this script in your home directory, you can run it (regardless of your current working directory) as follows:

	* `~/start.sh`
