#!/bin/bash

#SBATCH -J rlEvalDgp
#SBATCH -o rlEvalDgp-%j.out
#SBATCH -e rlEvalDgp-%j.err
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL
#SBATCH -C EPYC_7351
#SBATCH --ntasks-per-core=1

python EvalDGPdb.py

echo "Executing on $HOSTNAME"

sleep 5
