# DEPRECATED
Python Readme
===============================================================================

The Python utilities here were created using Python 2.7. I have not tried them 
with Python 3.x.

bdictutil.py is the command to do vocabulary analysis, HTML gloss generation,
and list corpus entries. You can use it by
downloading the Python packages under this directory. Run the command with
the parameter 'help' to get information on how to use it.

The modules in the bdict package use the config.yaml file to minize the parameters
passed in on the command line and to help support unit testing.

There is a dependency on Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/) 
for parsing HTML web documents.

$ sudo pip install beautifulsoup4

There is also a dependency on regex

$ sudo apt-get install python-dev
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python get-pip.py
$ sudo pip install regex

Basic use:

$ python bdictutil.py

gives help