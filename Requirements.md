# Application Dependency Documentation
This document outlines all the required Python packages needed to run the application. It provides a direct way to install them using pip, Python’s package installer.

## Source
The packages are hosted on PyPI, accessible via:

URL: https://pypi.org/simple
SSL Verification: Enabled

## Required Python Version
Python 3.12

# Installation Instructions
To install these dependencies, make sure you have Python 3.12 or higher installed on your system. It is recommended to use a virtual environment to avoid conflicts with other packages.

## Setting Up a Virtual Environment
For Unix/macOS:
python3 -m venv myenv
source myenv/bin/activate

For Windows:
python -m venv myenv
myenv\Scripts\activate

# Installing Dependencies
After setting up and activating the virtual environment, install the required packages by running the following command:

pip install blinker==1.7.0 click==8.1.7 flask==3.0.2 itsdangerous==2.1.2 jinja2==3.1.3 markupsafe==2.1.5 peewee psycopg2==2.9


List of Packages and Versions
Here is a detailed list of all the packages required to run the application, along with their specific versions:

blinker = "1.7.0"
click = "8.1.7"
flask = "3.0.2"
itsdangerous = "2.1.2"
jinja2 = "3.1.3"
markupsafe = "2.1.5"
peewee = "any version (latest)"
psycopg2 = "2.9.9"
werkzeug = "3.0.1"
Flask-Cors = "4.0.0"
peewee-migrations = "0.3.32"

# Frontend Configuration
The frontend of the application is premade using Node.js. Below are the steps and commands needed to set up and manage the frontend environment.

### Project Setup
Install all the dependencies required for the project:

npm install

### Development Commands
Compiles and hot-reloads for development:

npm run serve

### Compiles and minifies for production:
npm run build

### Lints and fixes files:
npm run lint
