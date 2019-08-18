#!/bin/bash

#SBATCH -J pathDGPdb
#SBATCH -o pathDGPdb-%j.out
#SBATCH -e pathDGPdb-%j.err
#SBATCH -N 1
#SBATCH -n 24
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL

python pathDGPdb.py

echo "Executing on $HOSTNAME"

sleep 5