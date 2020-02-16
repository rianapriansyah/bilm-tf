#!/bin/bash
#
#SBATCH --job-name=train_elmo
#SBATCH --output=train_elmo.txt
#
#SBATCH --nodes=1
#SBATCH --time=4320:00

srun python bin/train_elmo.py \
    --train_prefix='/home/m418662/elmo/train/*' \
    --vocab_file /home/m418662/vocabulary.txt \
    --save_dir /home/m418662/elmo/output
