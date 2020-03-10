#!/bin/bash
#
#SBATCH --job-name=test_elmo
#SBATCH --output=test_elmo.txt
#
#SBATCH --nodes=1
#SBATCH --time=4320:00

srun python bin/dump_weights.py \
    --save_dir /home/m418662/elmo/output
	--outfile /home/m418662/elmo/weights.hdf5
