#!/bin/bash

for i in $(ls -a ./test_cases_exe/*.exe); do
    filename=$(basename $i);
    filename="${filename%.*}"
    mkdir "$(pwd)/test_cases"
    xxd $i | cut -d' ' -f-9 > "$(pwd)/test_cases/$filename.bytes";
done