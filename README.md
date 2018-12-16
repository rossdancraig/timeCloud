# timeCloud
Django-based website and Android app to record and visualise 
how users spend their time.

## Setup
1) First make sure you have Python and pip3 installed:
```
sudo apt-get update
sudo apt-get install python3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo apt-get -y install python3-pip
```
Verify that they were installed correctly:
```
python --version 
pip3 --version 
```


2) Create a virtual environment to keep consistent environment
variables and tool versions:
```
sudo apt install virtualenv
virtualenv --python=\`which python3\` [VIRTUAL_ENV_NAME]
```
To get out of virtualenv simply type `deactivate` in terminal.


3) Once inside your virtualenv, install Django (web framework) and 
Postgres (database mananger) and Python packages:
[Postgres Installation Instructions](https://www.postgresql.org/download/)

```
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common postgresql-contrib
sudo pip3 install psycopg2
sudo pip3 install psycopg2-binary
sudo pip3 install Django
```
Check that Django was installed correctly:
`python3 -m django --version`
