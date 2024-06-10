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
