#!/bin/bash

pass=`ls ../storage/add_storage`

echo ${pass}

for card in "add_storage"/${pass}; do

echo "calculating ...${card}"
combine -M Significance "add_storage"/${card} -t -1 --expectSignal=1 | grep Significance:

done
