IPython 0.12 includes a wonderful Notebook interface.


This (trivial) django app provides the command 

    ./manage.py notebook

to launch the IPython notebook as a django shell.

It's done in a really hacky way. See http://mail.scipy.org/pipermail/ipython-dev/2012-January/008526.html for clues how to do it better.


Installation (on Ubuntu)
-----------------------
Install the dependencies

    sudo aptitude install libzmq1 libzmq-dev
    pip install --upgrade ipython tornado pyzmq
    
Then clone this repository into your django project and add it to the INSTALLED_APPS list in your settings file.


Licence
-------
Public domain