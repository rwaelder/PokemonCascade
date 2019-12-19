#!/bin/bash

for file in *.png
do 
base="${file%.*}"
mkdir $base
python3 tilePackToTiles.py $file
done