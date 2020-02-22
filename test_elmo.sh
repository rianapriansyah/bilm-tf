#!/bin/bash
#
#SBATCH --job-name=test_elmo
#SBATCH --output=test_elmo.txt
#
#SBATCH --nodes=1
#SBATCH --time=4320:00

srun python bin/run_test.py \
    --test_prefix='/home/m418662/elmo/test/*' \
    --vocab_file /home/m418662/vocabulary.txt \
    --save_dir /home/m418662/elmo/output
