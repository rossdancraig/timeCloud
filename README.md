# timeCloud
Django-based website and Android app to record and visualise 
how users spend their time.

# Setup
1) First make sure you have Python and pip3 installed:
```
sudo apt-get update
sudo apt-get install python3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
python --version #Verify that it's version 3.6.X
sudo apt-get -y install python3-pip
pip3 --version #Verify that you get some output
```
2) Create a virtual environment to keep consistent environment
variables and tool versions:
```
sudo apt install virtualenv
virtualenv --python=\`which python3\` [VIRTUAL_ENV_NAME]
```
To get out of virtualenv simply type `deactivate` in terminal.


