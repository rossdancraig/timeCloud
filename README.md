# timeCloud
Django-based website and Android app to record and visualise 
how users spend their time.

## Installing Tools and Packages
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
virtualenv --python=`which python3` [VIRTUAL_ENV_NAME]
source [VIRTUAL_ENV_NAME]/bin/activate
```
To get out of virtualenv simply type `deactivate` in terminal.


3) Once inside your virtualenv, install Django (web framework) and 
Postgres (database mananger) and Python packages:
[Postgres Installation Instructions](https://www.postgresql.org/download/)

```
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common postgresql-contrib
pip install psycopg2 psycopg2-binary
pip install Django
```
Check that Django was installed correctly:
```
python -m django --version
```

## Configuring a new App and Database
The following is a summary of steps taken from the 
[Official Django Beginner Tutorial](https://docs.djangoproject.com/en/2.1/intro/).
Be sure to first enter into your virtual environment from earlier.

```
django-admin startproject [PROJECT_NAME]
```

From the `PROJECT_NAME` dir you can run `python manage.py runserver` and view the 
result on your browser (see terminal result for instructions).



```
python manage.py startapp [APP_NAME]
```

[Configure Postgres and create a database](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES)
[Configure the  `PROJECT_NAME/settings.py`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES) 
file to use this database and update `TIME_ZONE` (ex: `America/Toronto`)
Also add this line to the `INSTALLED_APPS` paths 
(see `APP_NAME/apps.py` file for exact auto-generated Config class name):
```
'APP_NAME.apps.AppNameConfig',
```

```
python manage.py migrate
```

