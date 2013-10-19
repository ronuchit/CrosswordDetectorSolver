#! /bin/bash

if [ $# -ne 3 ] ; then
    echo "Usage: bash $0 [PUZZLE_SIZE] [BLOCK_SIZE] [IMAGE_NAME]"
    exit
fi

echo $1 > puzzle_info.txt
echo $2 >> puzzle_info.txt
echo $3 >> puzzle_info.txt

# call C++ puzzle processor
make
./hack

# call Python top-level function
python execute.py