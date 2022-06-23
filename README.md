# Home Interface
***An open source [Melon](https://www.divemelon.com) project***

### Setting up your programming environment

I *HIGHLY* recommend [VSCode](https://code.visualstudio.com/download). On installation, be sure to include the `code` command in your PATH (if you're on Windows).

  - Open the current directory in VSCode

```
code .
```

# Getting Started

**Home Interface** is primarily written in [Python](https://www.python.org/downloads/) v3.8.

  - Initialize the development environment with [venv](https://docs.python.org/3/library/venv.html)

```
python3 -m venv ${HOME}/Developer/home_interface
```

  - Change directory

```
cd ${HOME}/Developer/home_interface
```

  - Start Virtual Environment

```
./Scripts/activate
```

# Overview

This repository is the interface that the end user will use. The vision is a simple terminal prompt that allows the user to monitor anything by request.

The goal of this project is to allow off the shelf microcontrollers to be implemented into the Building Automation System's user interface (this repository).

Development is currently in progress on the Spine Network -- this is the backend that allows microcontrollers (i.e. Arduinos) to be categorized by their function (i.e. temp, lights, AC, etc.)
