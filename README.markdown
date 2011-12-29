IPython 0.12 includes a wonderful Notebook interface.


Using the IPython notebook as a django shell
--------------------------------------------
This (trivial) django app provides the command 

    ./manage.py notebook

to launch the IPython notebook as a django shell.


Installation (on Linux)
-----------------------
Install the dependencies

    sudo aptitude install libzmq1 libzmq-dev
    pip install --upgrade ipython tornado pyzmq
    
Then clone this repository into your django project and add it to the INSTALLED_APPS list in your settings file.


Licence
-------
Public domain