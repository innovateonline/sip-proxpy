sip-proxpy
==========
This is a fork of proxpy as used in our DAVID-SIP projects. Proxpy was written 
by Roberto Paleari and Allessandro Reina with patches by Yeuk Hon Wong 

The only reason for this fork is that we need to have a installable reference
where we manage the changes.  Please refer to the `original source of proxpy
<tps://code.google.com/p/proxpy/>`_ or the fork on GitHub by `Yeuk Hon Wong
<https://github.com/yeukhon/proxpy >`_  for the latest version of the original
code base. 

The one feature that drew us to proxpy is the plugin architecture that the
authors incorporated. It makes proxpy an ideal test ground for proxying in
python. However, please note that most of the functionality works in FireFox,
but not in Chrome (other browsers were not tested).

Installation
-------------
The easiest way to install this is to use PIP::

     $ pip install git+git://github.com/innovateonline/sip-proxpy.git

Note that you will need to set up a 'plugins' folder somewhere (with a name of
your choice) where the proxpy plugins are stored. You may want to download the
plugin examples separately to place them in a convenient location to run the 
example below. 

Custom HTTP Headers to shiny-server-pro
-----------------------------------------------------
The reference implementation of a proxy that rewrites request headers is `Jeff
Allens version in nodejs <https://gist.github.com/trestletech/7160493>`_ and
this is the reason for the 'something' http_header to be included in the test
app (`shiny-httpheader-test
<https://github.com/innovateonline/shiny-httpheader-test>`_). The
shinycustomerheader.py plugin script does the same thing, but using Python.

Running the example
++++++++++++++++++++
After installing sipproxpy you can run your the example plugin as the basis for
creating your own::

     $ sipproxpy -p 8001 -r localhost:3838 -x plugins/shinycustomheader.py

or replace 'localhost:3838' with the URL or IP address of the location where
you have installed shiny-server-pro. 

