#!/bin/bash

pass=`ls ./card_storage`

echo ${pass}

for card in "card_storage"/${pass}; do

echo "calculating ...${card}"
combine -M Significance "card_storage"/${card} -t -1 --expectSignal=1 | grep Significance: 

done
