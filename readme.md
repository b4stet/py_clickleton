# py_clickleton

A simple skeleton to structure a CLI application using click.

## To adapt
- package name, from `clickleton/` to the name of your tool
- imports, from `clickleton` to the chosen one
- `setup.py`: adapt the fields


## Requirements
```
$ python3 -m venv cli_env
$ source ./cli_env/bin/activate
$ pip3 install -r requirements.txt
```

## Install
```
$ source ./cli_env/bin/activate
$ pip3 install .
```

## Uninstall
```
$ pip3 uninstall py_clickleton
```

## Usage
```
$ python3 -m clickleton.cli --help
$ python3 -m clickleton.cli <command> --help
$ python3 -m clickleton.cli <command> <subcommand> --help
```

