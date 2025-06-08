#!/bin/bash

export PATH=~/anaconda3/bin:$PATH
source /u/user/yeobi97/anaconda3/etc/profile.d/conda.sh

#echo "making output directory "
#mkdir out_eeetrain
#echo "output directory making finished"

echo "preparing for eee evaluation"

echo "start conda setup"
conda activate tabula

echo "finished conda setup"

nvidia-smi

cd /u/user/yeobi97/JKPS_WZG/WZG/final_trial/run/Eval_train

python3 Eval.py --epoch 200 --batch 1024	
echo "Training start"

