#!/bin/bash

export PATH=~/anaconda3/bin:$PATH
source /u/user/yeobi97/anaconda3/etc/profile.d/conda.sh

#echo "making output directory "
#mkdir out_eeetrain
#echo "output directory making finished"

echo "starting conda setup"
conda activate tabula

nvidia-smi

cd /u/user/yeobi97/JKPS_WZG/WZG/final_trial/run/Train

python3 test_mmm_train.py --epoch 10 --batch 1024 
echo "Training start"

