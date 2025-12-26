#!/bin/bash

# for linux with miniconda3 installed
# choose folder to activate as conda env
# for folder not in conda path for disk space

home_path="path/to/home"
conda_path="$home_path/miniconda3"
conda_load="$conda_path/etc/profile.d/conda.sh"
env_path="$home_path/path/to/env"

# Load Conda into the shell
source "$conda_load"

# Activate env
conda activate "$env_path"

# run in command line
#source activate_env.sh

# run in command line if file has problems
# sed -i 's/\r$//' activate_env.sh

