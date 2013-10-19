#! /bin/bash

if [ $# -ne 3 ] ; then
    echo "Usage: bash $0 [PUZZLE_SIZE] [BLOCK_SIZE] [IMAGE_NAME]"
    exit
fi

mkdir ../temp
echo $1 > ../temp/puzzle_info.txt
echo $2 >> ../temp/puzzle_info.txt
echo $3 >> ../temp/puzzle_info.txt

# call C++ puzzle processor
make
./hack

python execute.py

rm -r ../temp