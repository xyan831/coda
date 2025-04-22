# setup local python environment


## setup mamba powershell commands:

download miniforge
```
Invoke-WebRequest -Uri "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe" -OutFile "Miniforge3-Windows-x86_64.exe"
```

install miniforge
```
Start-Process -FilePath "Miniforge3-Windows-x86_64.exe" -ArgumentList "/S /InstallationType=JustMe /AddToPath=0 /RegisterPython=0" -Wait
```

remove installer
```
Remove-Item "Miniforge3-Windows-x86_64.exe"
```


##miniforge commands:

create environment
```
mamba create --name ENV_NAME python=3.11
```

get environment list
```
mamba env list
```

activate environment
```
mamba activate ENV_NAME
```

deactivate environment
```
mamba deactivate
```


##powershell commands:

create environment
```
conda create --name ENV_NAME python=3.11
```

get environment list
```
conda env list
```

activate environment
```
conda activate ENV_NAME
```

deactivate environment
```
conda deactivate
```
