## Prerequisites

Before starting, install the following tools:

- Python 3.12 or later
- Pip package manager

For more information on these tools, see the public documentation on
[Python](https://www.python.org/downloads/) or
[Pip](https://pip.pypa.io/en/stable/installing/)

### Setup development PC
From the root of your cloned repo, generate a virtual environment with a
specific version of python.

Windows
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

Linux / MacOS
```bash
python3 -m venv .venv
. ./.venv/bin/activate
```

Next install any necessary packages.

```bash
pip install -r requirements.txt
```

## Running the Flask App Locally

From the root of your cloned repo run the following:

```bash
flask run --debug
```

## Development Process

### Steps

1. Create empty project
2. Create minimal Flask app
2. Add to GitHub
2. Create Azure app service

### References

* https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application
* https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?toc=%2Fazure%2Fdeveloper%2Fpython%2Ftoc.json&bc=%2Fazure%2Fdeveloper%2Fpython%2Fbreadcrumb%2Ftoc.json&tabs=flask%2Cwindows%2Cvscode-aztools%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift

