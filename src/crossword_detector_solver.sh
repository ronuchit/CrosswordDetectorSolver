#! /bin/bash

if [ $# -ne 2 ] ; then
    echo "Usage: bash $0 [IMAGE_FILE_NAME] [NUM_BLOCKS]"
    exit
fi

mkdir ../temp
echo $1 > ../temp/puzzle_info.txt
echo $2 >> ../temp/puzzle_info.txt

# call C++ puzzle processor
make
./hack
rm hack

python execute.py

javac Character.java
javac CrosswordMaker.java
java CrosswordMaker

rm -r ../temp