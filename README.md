# Legends of Learning - Godot web build template builder
This is a little project meant to simplify building a web build template for Godot.
It is meant to create a build template used to create a very small functional web build of Godot games, while still using the latest Godot version.

## Prerequisites
The following tools are required for compiling the web build template:
- Python (preferably 3.12 or higher)

## Setup
When first using this project, initialize the submodules needed for compilation:
```commandline
git submodule update --init --recursive
```

Setup a virtual environment and activate it
```commandline
python -m venv venv
.\venv\bin\activate
```

Install the requirements with pip
```commandline
pip install -r requirements
```

## Usage
To compile the godot web build, first make sure you have activated your python virtual environment:
```commandline
.\venv\bin\activate
```

Then compile the godot web build template with the bat file on windows:
```commandline
.\make_web_build_template.bat
```