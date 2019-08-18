#!/bin/bash

#SBATCH -J cleanJob
#SBATCH -o cleanJob-%j.out
#SBATCH -e cleanJob-%j.err
#SBATCH -N 1
#SBATCH -n 4
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL

python cleanHDR.py

echo "Executing on $HOSTNAME"

sleep 5
