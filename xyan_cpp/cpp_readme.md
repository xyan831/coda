# session config: add mingw32/bin to PATH

windows powershell
```
$env:PATH="C:\Users\xyan8\Documents\1_coda\mingw32\bin;$env:PATH"
```

# compile/execute commands

normal compile
```
g++ main.cpp -o run
```

debugging compile
```
g++ -std=c++17 -Wall -Wextra -pedantic -Weffc++ main.cpp -o run
```

execute code
```
./run
```

