#!/bin/bash

#SBATCH -J rlECJob
#SBATCH -o rlEC-%j.out
#SBATCH -e rlEC-%j.err
#SBATCH -N 1
#SBATCH -n 24
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL

python paralleHDR.py
#python -m scoop EChdr_scoop.py
echo "Executing on $HOSTNAME"

sleep 5
