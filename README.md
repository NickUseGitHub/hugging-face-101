## Prerequisite
- pyenv -- python version manager
- uv -- python package manager
- requires-python = ">=3.13"


#### pyenv installation
```
$ brew install pyenv
```

#### UV installation
```
$ brew install uv
```

##### UV install packages
```
uv sync
```

#### Create python virtual environment
##### Use pyenv to create python version in your project's folder
```
$ pyenv virtualenvs # to list your envs
$ pyenv virtualenv <PYTHON_VERSION> <ENV_NAME> # to create virtual envs
$ pyenv activate <ENV_NAME> # to activate virtual envs
```

##### Use these command to create venv for project's virtual environments
```
$ python -m venv .venv
```


### To run webserver via fastAPI
```
$ uv run fastapi dev src/main.py --app app 
```
