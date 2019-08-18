#!/bin/bash

#SBATCH -J moverJob
#SBATCH -o moverJob-%j.out
#SBATCH -e moverJob-%j.err
#SBATCH -N 1
#SBATCH -n 16
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL

python mover.py

echo "Executing on $HOSTNAME"

sleep 5