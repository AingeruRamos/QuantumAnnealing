#!/bin/bash

# Job name
#SBATCH --job-name=plannam

# Define the files which will contain the Standard and Error output
#SBATCH --output=outputs/M_%A.out
#SBATCH --error=outputs/M_%A.err

# Number of tasks that compose the job
#SBATCH --ntasks=1

# Advanced use
# #SBATCH --cpus-per-task=20
# #SBATCH --threads-per-core=2
# #SBATCH --ntasks-per-core=2

# Required memory (Default 2GB)
#SBATCH --mem-per-cpu=50G

# Select one partition
# ML-CPU
# ML-GPU
#SBATCH --partition=KAT
##SBATCH --gpu=1

# If you are using arrays, specify the number of tasks in the array
#SBATCH --array=1-1

priscilla exec python3 main.py 31 1200
