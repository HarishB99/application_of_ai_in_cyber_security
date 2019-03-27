#!/bin/bash

mkdir "$(pwd)/test_cases"

for i in $(ls -a ./test_cases_exe/*.exe); do
    filename=$(basename $i);
    filename="${filename%.*}"
    xxd $i | cut -d' ' -f-9 > "$(pwd)/test_cases/$filename.bytes";
done