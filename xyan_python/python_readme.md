# session config windows powershell

add miniconda bin to PATH
```
$env:PATH="C:\Users\xyan8\Documents\1_coda\miniconda\condabin;$env:PATH"
```

activate environment for powershell
```
cmd /c "activate normal && powershell"
```

# setup local python environment

get environment info
```
conda env list
conda info --envs
```

create environment
```
conda create --name normal python=3.12
```

use conda-forge to avoid anaconda terms of service
```
conda create -n normal python=3.12 -c conda-forge --override-channels
```

activate environment
```
conda activate normal
```

deactivate environment
```
conda deactivate
```

