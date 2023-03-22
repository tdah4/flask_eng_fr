# coding-project-template
If you get AttributeError: module 'ssl' has no attribute 'TLSVersion'
This error comes up when the virtual environment is not created.

Run the following commands:

pip install virtualenv

virtualenv -p /usr/bin/python3.8 virtualenv_name

Now at last we just need to activate it, using the command

source virtualenv_name/bin/activate

Then install your python packages:

python3 -m pip install python-dotenv

python3 -m pip install ibm_watson

python3 -m pip install Flask 

