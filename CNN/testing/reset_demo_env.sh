#!/bin/bash

if [ $# -eq 0 ]; then
	echo "usage: $0 dirpath"
	exit 1
fi

if [ -d "$1" ]; then
	if [ -r "$1" ] && [ -w "$1" ]; then
		mkdir $1/bytecodes
		mkdir $1/images
		for i in $(ls "$1"); do
			mv $1/$i/bytecodes/*.bytes $1/bytecodes/ 2> /dev/null
			mv $1/$i/images/*.png $1/images/ 2> /dev/null
		done

		rm -rf $1/gatak/
		rm -rf $1/ramnit/
		rm -rf $1/kelihos_ver*/
		rm -rf $1/lollipop/
		rm -rf $1/misclassified/ 2> /dev/null
		rm -rf $1/obfuscator_acy/
		rm -rf $1/simda/
		rm -rf $1/tracur/
		rm -rf $1/vundo/
		
		mv $1/bytecodes/*.bytes $1/
		rm -rf $1/bytecodes
		
		rm -f $1/statistics.csv

		echo "Reset successful"
	else
		echo "No read and write permissions on directory $1"
	fi
else
	echo "No such directory found: $1"
fi
