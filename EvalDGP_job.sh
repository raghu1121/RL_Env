#!/bin/bash

#SBATCH -J EvalDGPdb
#SBATCH -o EvalDGPdb-%j.out
#SBATCH -e EvalDGPdb-%j.err
#SBATCH -N 1
#SBATCH -n 24
#SBATCH --account=TUK-Amlafoc
#SBATCH --mail-type=ALL


python EvalDGPdb.py

echo "Executing on $HOSTNAME"

sleep 5