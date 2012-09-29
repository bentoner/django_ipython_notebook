IPython 0.12 includes a wonderful Notebook interface.


This (trivial) django app provides the command 

    ./manage.py notebook

to launch the IPython notebook as a django shell.

It's done here in a really hacky way. It's done better in https://github.com/jnovinger/django_ipython_notebook but that doesn't work for me.

Installation (on Ubuntu)
-----------------------
Install the dependencies

    sudo aptitude install libzmq1 libzmq-dev
    pip install --upgrade ipython tornado pyzmq
    
Then clone this repository into your django project and add it to the INSTALLED_APPS list in your settings file.


Licence
-------
Public domain