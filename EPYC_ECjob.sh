#!/bin/bash

#SBATCH -J rlECJob
#SBATCH -o rlEC-%j.out
#SBATCH -e rlEC-%j.err
#SBATCH -N 1
#SBATCH -n 64
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL
#SBATCH -C EPYC_7351

python paralleHDR.py

echo "Executing on $HOSTNAME"

sleep 5
