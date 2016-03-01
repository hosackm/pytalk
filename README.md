pytalk
======

This repository holds the materials for the Tech Talk that I gave on February
26, 2016 at Dolby Laboratories.  The contents include:

* Jupyter Notebook with Python examples
* Slides for presentation created using jupyter-nbconvert
* script.txt is what I was reading from when I wasn't improvising
* Directories with example code I ran during the presentation

Viewing the Slides
==================

The slides are generated using the Jupyter tool nbconvert.  They require
reveal.js and therefore must be viewed on a hosted server.  If you would like
to view them type the following:

````bash
    cd /the/directory/this/readme/is/in
    # If you're using Python 2
    python -m HTTPSimpleServer
    # If you're using Python 3
    python -m http.server
````

Then navigate to: http://localhost:8000/Tech%20Talk.slides.html.

Running the Jupyter Notebook
============================

The Jupyter notebook (Tech Talk.ipynb) can be viewed and interacted with
in a web browser.

To do so, install Jupyter followin the installation
instructions on 
(their website)[http://jupyter.readthedocs.org/en/latest/install.html].

Then you can run:

````bash
    jupyter-notebook
````

and navigate to Tech Talk.ipynb inside your browser of choice.
